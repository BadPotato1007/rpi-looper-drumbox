from pydub import AudioSegment
from pydub.playback import play
import pyaudio
import wave
from time import sleep
import time

beat_time = float(input('Enter the time in seconds for how long the track should be: '))
recno = input('Enter the track number for the recording ( 1 - 5 ): ')
yn = input('Do you want to play after recording the track? (y/n): ')
rec_in_file = recno + '.wav'
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * beat_time)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(rec_in_file, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()


####################################################################
beat_time_milliseconds = beat_time*1000

blankaudio = AudioSegment.silent(duration=beat_time_milliseconds) #the blank audio file
try:
    audio1 = AudioSegment.from_file("1.wav") #your first audio file
    audio2 = AudioSegment.from_file("2.wav") #your second audio file
    audio3 = AudioSegment.from_file("3.wav") #your third audio file
    audio4 = AudioSegment.from_file("4.wav") #your second audio file
    audio5 = AudioSegment.from_file("5.wav") #your second audio file
except:
    i=1



mixed = blankaudio
try:
    mixed = mixed.overlay(audio1)
except:
    i=1
    

try:
    mixed = mixed.overlay(audio2)
except:
    i=1
    
    
try:
    mixed = mixed.overlay(audio3)
except:
    i=1
    
try:
    mixed = mixed.overlay(audio4)
except:
    i=1

try:
    mixed = mixed.overlay(audio5)
except:
    i=1

        



mixed.export("play.wav", format='wav') #export mixed  audio file
if yn == 'y':
    while True:
        play(mixed)                             #play mixed audio file
elif yn == 'n':
    print("Recording done and saved as play.wav")
    time.sleep(1)
    exit()
    