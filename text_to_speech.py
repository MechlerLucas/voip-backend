# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

import azure.cognitiveservices.speech as speechsdk
import wave

def text_to_speech(text, voice_name):
    # Creates an instance of a speech config with specified subscription key and service region.
    # Replace with your own subscription key and service region (e.g., "westus").
    speech_key, service_region = "538b25cfe5434badbd242b83178f261c", "brazilsouth"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
    speech_config.speech_synthesis_voice_name = voice_name

    # Creates a speech synthesizer using the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    # Synthesizes the received text to speech.
    result = speech_synthesizer.speak_text_async(text).get()

    # Checks result.
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        audio_data = result.audio_data
        with wave.open('output.wav', 'wb') as wavfile:
            wavfile.setnchannels(1)
            wavfile.setsampwidth(2)
            wavfile.setframerate(16000)
            wavfile.writeframes(audio_data)

        print("Audio saved to output.mp3")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
        print("Did you update the subscription info?")
