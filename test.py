from pydub import AudioSegment
from pydub.playback import play

beat_time_milliseconds = 4000

blankaudio = AudioSegment.silent(duration=beat_time_milliseconds) #the blank audio file
audio1 = AudioSegment.from_file("rec1_file.wav") #your first audio file
audio2 = AudioSegment.from_file("rec2_file.wav") #your second audio file


mixed = blankaudio
mixed = mixed.overlay(audio1)
mixed = mixed.overlay(audio2)



mixed.export("mixed.wav", format='wav') #export mixed  audio file
while True:
    play(mixed)                             #play mixed audio file