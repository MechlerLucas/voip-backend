import azure.cognitiveservices.speech as speechsdk
import wave
import random
import string
import os
from user_funcions import insert_all

speech_key, service_region = "538b25cfe5434badbd242b83178f261c", "brazilsouth"
#Função para teste de audio
def text_to_demo(voice_name, text):

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # Note: the voice setting will not overwrite the voice element in input SSML.
    speech_config.speech_synthesis_voice_name = voice_name

    # use the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    speech_synthesizer.speak_text_async(text).get()


#Função para criação de audio e armazenamento em db e S3
def text_to_speech(user, text, voice_name):

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
    speech_config.speech_synthesis_voice_name = voice_name

    # Creates a speech synthesizer using the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    # Synthesizes the received text to speech.
    result = speech_synthesizer.speak_text_async(text).get()

    # Checks result.
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + ".wav"
        audio_data = result.audio_data

        audio_file_path = os.path.join("audio", filename)
        audio_data = result.audio_data
        with wave.open(audio_file_path, 'wb') as wavfile:
            wavfile.setnchannels(1)
            wavfile.setsampwidth(2)
            wavfile.setframerate(16000)
            wavfile.writeframes(audio_data)

        print("Audio saved to", audio_file_path)

        insert_all(user, filename, text, voice_name)

    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
        print("Did you update the subscription info?")
