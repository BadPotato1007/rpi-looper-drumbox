




print('Starting up...')



##################################################################
##                             IMPORTS                          ##
##################################################################


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



##################################################################
##                    DECLARING THE CONNECTIONS                 ##
##################################################################



############## RECORDING BUTTONS ##############

btn1 = Button(2)
btn2 = Button(3)
btn3 = Button(4)
btn4 = Button(5)
btn5 = Button(6)
btn6 = Button(7)
btn7 = Button(8)
btn8 = Button(9)

################### GREEN LEDS ###################

r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0
r7 = 0
r8 = 0
r9 = 0
r10 = 0
r11 = 0
r12 = 0
r13 = 0
r14 = 0
r15 = 0
r16 = 0


################## GREEN LEDS ##################

g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
g6 = 0
g7 = 0
g8 = 0
g9 = 0
g10 = 0
g11 = 0
g12 = 0
g13 = 0
g14 = 0
g15 = 0
g16 = 0


################### BLUE LEDS ##################

b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0
b8 = 0
b9 = 0
b10 = 0
b11 = 0
b12 = 0
b13 = 0
b14 = 0
b15 = 0
b16 = 0

#################### THE LCD ###################

import drivers
from time import sleep

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()

# Main body of code
while True:
    # Remember that your sentences can only be 16 characters long!
    print("Writing to display")
    display.lcd_display_string("Greetings Human!", 1)  # Write line of text to first line of display
    display.lcd_display_string("Demo Pi Guy code", 2)  # Write line of text to second line of display
    sleep(2)                                           # Give time for the message to be read
    display.lcd_display_string("I am a display!", 1)   # Refresh the first line of display with a different message
    sleep(2)                                           # Give time for the message to be read
    display.lcd_clear()                                # Clear the display of any data
    sleep(2)                                           # Give time for the message to be read
        

