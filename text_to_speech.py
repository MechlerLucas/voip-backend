import azure.cognitiveservices.speech as speechsdk
import wave
import random
import string
import os
import json
from user_funcions import insert_all

speech_key, service_region = "eb419a4b91894d9ea583eb0a08315546", "brazilsouth"

#Função para criação de audio e armazenamento em db e S3
def text_to_speech(user, text, voice_name, voice_speed, pitch):
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    # Set the voice name, refer to https://aka.ms/speech/voices/neural for the full list.
    speech_config.speech_synthesis_voice_name = voice_name

    # Create SSML with adjusted rate and pitch
    ssml = f'''
        <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="pt-BR">
            <voice name="{voice_name}">
                <prosody pitch="{pitch}%" rate="{voice_speed}">
                    {text}
                </prosody>
            </voice>
        </speak>
    '''
    print("Generated SSML:", ssml)  # Print the generated SSML

    # Synthesize the SSML text to speech.
    result = speech_synthesizer.speak_ssml_async(ssml).get()

    filename = None  # Initialize filename as None

    # Check result.
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + ".wav"
        audio_data = result.audio_data

        audio_file_path = os.path.join("audio", filename)
        with wave.open(audio_file_path, 'wb') as wavfile:
            wavfile.setnchannels(1)
            wavfile.setsampwidth(2)
            wavfile.setframerate(16000)
            wavfile.writeframes(audio_data)

        print("Audio saved to", audio_file_path)

        id_audio = insert_all(user, filename, text, voice_name)

    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
        print("Did you update the subscription info?")
        
    result={'id_audio':id_audio,'filename':filename}

    return result



async def load_voices():
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    
    voices_result = speech_synthesizer.get_voices_async().get()
    voices = voices_result.voices

    formatted_voices = format_voices(voices)
    return {'voices': formatted_voices}

def format_voices(voices):
    formatted_voices = []
    
    for voice in voices:
        if voice.locale == "pt-BR":
            formatted_voice = voice.name.replace("Microsoft Server Speech Text to Speech Voice (pt-BR, ", "pt-BR-")
            formatted_voice = formatted_voice.replace(")", "")
            formatted_voices.append(formatted_voice)
        if  voice.locale == "en-US":
            formatted_voice = voice.name.replace("Microsoft Server Speech Text to Speech Voice (en-US, ", "en-US-")
            formatted_voice = formatted_voice.replace(")", "")
            formatted_voices.append(formatted_voice)
    
    return formatted_voices