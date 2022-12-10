




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
import drivers
from time import sleep


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
############ THE AUDIO FILES ############
rec1 = 0
rec2 = 0
rec3 = 0
rec4 = 0
rec5 = 0
rec6 = 0
rec7 = 0
rec8 = 0

############ OTHER CONNECTIONS ############
rotor = RotaryEncoder(16, 20, wrap=True)

################### VARS ##################
beat_tempo = 100
beat_time = 1


##################################################################
##                   THE DIFFERENT PROGRAMS USED                ##
##################################################################





#################### ROTRY ENCODER ###################
def set_timeperiod():
    beat_tempo = rotor.steps
    beat_time = beat_tempo/15
    print("set the bet time to "+ beat_tempo +" and the beat tempo to "+ beat_tempo)






#################### THE LCD ###################
display = drivers.Lcd()

def display():
    beat_tempo_str = str(beat_tempo)
    beat_time_str = str(beat_time)
    line = ("tempo: " + beat_tempo_str + "    " + beat_time_str + "s") #make the text to display on the lcd
    print("Writing to display...")
    display.lcd_display_string(" DRUMBOX LOOPER ", 1)  # Write line of text to first line of display
    display.lcd_display_string(line, 2)  # Write line of text to second line of display



################# MIXING ##################

def mix():
    blankaudio = AudioSegment.from_file("1sec.mp3") #the blank audio file
    audio1 = AudioSegment.from_file("rec1_file.wav") #your first audio file
    audio2 = AudioSegment.from_file("rec2_file.wav") #your second audio file
    audio3 = AudioSegment.from_file("rec3_file.wav")
    audio4 = AudioSegment.from_file("rec4_file.wav")
    audio5 = AudioSegment.from_file("rec5_file.wav")
    audio6 = AudioSegment.from_file("rec6_file.wav")
    audio7 = AudioSegment.from_file("rec7_file.wav")
    audio8 = AudioSegment.from_file("rec8_file.wav")
    if rec1 == 2:
        mixed = blankaudio.overlay(audio1)
    else:
        print("")

    if rec2 == 2:
        mixed = mixed.overlay(audio2)
    else:
        print("")

    if rec3 == 2:
        mixed = mixed.overlay(audio3)
    else:
        print("")

    if rec4 == 2:
        mixed = mixed.overlay(audio4)
    else:
        print("")

    if rec5 == 2:
        mixed = mixed.overlay(audio5)
    else:
        print("")

    if rec6 == 2:
        mixed = mixed.overlay(audio6)
    else:
        print("")

    if rec7 == 2:
        mixed = mixed.overlay(audio7)
    else:
        print("")

    if rec8 == 2:
        mixed = mixed.overlay(audio8)
    else:
        print("")

    mixed.export("mixed.wav", format='wav') #export mixed  audio file
    while True:
        play(mixed)                             #play mixed audio file
        
