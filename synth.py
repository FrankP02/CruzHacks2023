import argparse
import google
import os, time, pygame

"""Google Cloud Text-To-Speech API sample application .
Example usage:
    python synthesize_text.py --text "hello"
    python synthesize_text.py --ssml "<speak>Hello there.</speak>"
"""
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file("awesomeware.json")
#key=API_KEY
#client = texttospeech.TextToSpeechClient(credentials=credentials)

# [START tts_synthesize_text]
def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient(credentials=credentials)

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-C",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
    
# [END tts_synthesize_text]

def playAnswer():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


time.sleep(30)
if os.path.exists("output.mp3"):
    os.remove("output.mp3")
else:
    print("File non-existent")