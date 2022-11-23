from pydub import AudioSegment
from pydub.playback import play

audio1 = AudioSegment.from_file("rec1_file.wav") #your first audio file
audio2 = AudioSegment.from_file("rec2_file.wav") #your second audio file

mixed = audio1.overlay(audio2)          #combine , superimpose audio files
#If you need to save mixed file
mixed.export("mixed.wav", format='wav') #export mixed  audio file
while True:
    play(mixed)                             #play mixed audio file