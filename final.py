from pydub import AudioSegment
from pydub.playback import play
from gpiozero import LED, Button, RotaryEncoder

# rec numbers meanings
# 0 = empty
# 1 = recording
# 2 = playing
# 3 = muted


# recording buttons
btn1 = Button(2)
btn2 = Button(3)
btn3 = Button(4)
btn4 = Button(5)
btn4 = Button(6)
btn4 = Button(7)
btn4 = Button(8)
btn4 = Button(9)
btn4 = Button(10)


# some more vars
rec1 = 0
rec2 = 0
rec3 = 0
rec4 = 0
rec5 = 0
rec6 = 0
rec7 = 0
rec8 = 0


rotor = RotaryEncoder(16, 20, wrap=True)

beat_time = 4
beat_tempo = 120

def set_timeperiod():
    beat_tempo = rotor.steps
    beat_time = beat_tempo/15
    print("set the bet time to "+ beat_tempo +" and the beat tempo to "+ beat_tempo)
    

rotor.when_rotated = set_timeperiod




btn1.when_pressed = srec1
btn2.when_pressed = srec2
btn3.when_pressed = srec3
btn4.when_pressed = srec4