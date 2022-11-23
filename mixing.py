from pydub import AudioSegment
from pydub.playback import play

audio1 = AudioSegment.from_file("rec1_file.wav") #your first audio file
audio2 = AudioSegment.from_file("rec2_file.wav") #your second audio file
audio3 = AudioSegment.from_file("rec3_file.wav")
mixed = audio1.overlay(audio2) 
mixed1 = mixed.overlay(audio3)         #combine , superimpose audio files
#If you need to save mixed file
mixed1.export("mixed.wav", format='wav') #export mixed  audio file
while True:
    play(mixed1)                             #play mixed audio file