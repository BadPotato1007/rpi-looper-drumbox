from pydub import AudioSegment
from pydub.playback import play

blankaudio = AudioSegment.from_file("1sec.mp3") #the blank audio file
audio1 = AudioSegment.from_file("rec1_file.wav") #your first audio file
audio2 = AudioSegment.from_file("rec2_file.wav") #your second audio file
audio3 = AudioSegment.from_file("rec3_file.wav")
audio4 = AudioSegment.from_file("rec4_file.wav")
audio5 = AudioSegment.from_file("rec5_file.wav")
audio6 = AudioSegment.from_file("rec6_file.wav")
audio7 = AudioSegment.from_file("rec7_file.wav")
audio8 = AudioSegment.from_file("rec8_file.wav")

mixed = blankaudio.overlay(audio1)
mixed = mixed.overlay(audio2)
mixed = mixed.overlay(audio3)
mixed = mixed.overlay(audio4)
mixed = mixed.overlay(audio5)
mixed = mixed.overlay(audio6)
mixed = mixed.overlay(audio7)
mixed = mixed.overlay(audio8)


mixed.export("mixed.wav", format='wav') #export mixed  audio file
while True:
    play(mixed)                             #play mixed audio file