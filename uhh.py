print('LOADING...')

from pydub import AudioSegment
from pydub.playback import play
from gpiozero import LED, Button, RotaryEncoder
import pyaudio
import wave
from pi74HC595 import pi74HC595
import Adafruit_CharLCD as LCD


# rec numbers meanings
# 0 = empty
# 1 = recording
# 2 = playing
# 3 = muted

##### DECLARING THE CONNECTIONS

# recording buttons
btn1 = Button(2)
btn2 = Button(3)
btn3 = Button(4)
btn4 = Button(5)
btn5 = Button(6)
btn6 = Button(7)
btn7 = Button(8)
btn8 = Button(9)


