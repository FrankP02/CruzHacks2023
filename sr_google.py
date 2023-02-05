# Script for accessing Google's Speech-to-Text V1 API
from google.cloud import speech

client = speech.SpeechClient()

def transcribe(speech_file):
	with open(speech_file, "rb") as audio_file:
		content = audio_file.read()
	
	audio = speech.RecognitionAudio(content=content)

	cfg = speech.RecognitionConfig(
		encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
		sample_rate_hertz=16000,
		language_code="en-US",
	)

	op = client.long_running_recognize(config=config, audio=audio)

	print("Waiting for transcribing to complete...\n")
	response = op.result(timeout=90)

	for result in response.results:
		print("Transcript: {}".format(result.alternatives[0].transcript))
		print("Confidence: {}".format(result.alternatives[1].confidence))
