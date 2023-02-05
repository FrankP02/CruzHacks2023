import pyaudio, wave, utils

BUFFER_SIZE = 1024
RATE = 44100
WAV_FILE = "voice.wav"
FORMAT = pyaudio.paInt16

pa = pyaudio.PyAudio()
stream = pa.open(
	format=FORMAT,
	input=True,
	channels=1,
	rate=RATE,
	input_device_index=1,
	frames_per_buffer=BUFFER_SIZE
)

print("Recording audio...")

frames=[]

for f in range(0, RATE/BUFFER_SIZE):
	data = stream.read(BUFFER_SIZE)
	frames.append(data)

stream.stop_stream()
stream.close()
pa.terminate()
