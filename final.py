from pydub import AudioSegment
from pydub.playback import play
from gpiozero import LED, Button, RotaryEncoder
import pyaudio
import wave


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
btn5 = Button(6)
btn6 = Button(7)
btn7 = Button(8)
btn8 = Button(9)

#some more vars
btn_pressed = 0
rotor = RotaryEncoder(16, 20, wrap=True)
beat_time = 4
beat_tempo = 120


# some more vars
rec1 = 0
rec2 = 0
rec3 = 0
rec4 = 0
rec5 = 0
rec6 = 0
rec7 = 0
rec8 = 0

#the functions




def set_timeperiod():
    beat_tempo = rotor.steps
    beat_time = beat_tempo/15
    print("set the bet time to "+ beat_tempo +" and the beat tempo to "+ beat_tempo)
    






def recording():
    audio1 = AudioSegment.from_file("rec1_file.wav") #your first audio file
    audio2 = AudioSegment.from_file("rec2_file.wav") #your second audio file
    audio3 = AudioSegment.from_file("rec3_file.wav")
    mixed = audio1.overlay(audio2) 
    mixed1 = mixed.overlay(audio3)         #combine , superimpose audio files
    #If you need to save mixed file
    mixed1.export("mixed.wav", format='wav') #export mixed  audio file
    if rec


def srec1():
    if rec1 == 0:
        rec1 = 1
        btn_pressed = 1
        record()
    elif rec1 == 1:
        rec1 = 2
        btn_pressed = 1
        play()
    elif rec1 == 2:
        rec1 = 3
        btn_pressed = 1
        stop()
    print("Button 1 was pressed")

def srec2():
    if rec2 == 0:
        rec2 = 1
        btn_pressed = 1
        record()
    elif rec2 == 1:
        rec2 = 2
        btn_pressed = 1
        play()
    elif rec2 == 2:
        rec2 = 3
        btn_pressed = 1
        stop()
    print("Button 2 was pressed")

def srec3():
    if rec3 == 0:
        rec3 = 1
        btn_pressed = 1
        record()
    elif rec3 == 1:
        rec3 = 2
        btn_pressed = 1
        play()
    elif rec3 == 2:
        rec3 = 3
        btn_pressed = 1
        stop()
    print("Button 3 was pressed")

def srec4():
    if rec4 == 0:
        rec4 = 1
        btn_pressed = 1
        record()
    elif rec4 == 1:
        rec4 = 2
        btn_pressed = 1
        play()
    elif rec4 == 2:
        rec4 = 3
        btn_pressed = 1
        stop()
    print("Button 4 was pressed")

def srec5():
    if rec5 == 0:
        rec5 = 1
        btn_pressed = 1
        record()
    elif rec5 == 1:
        rec5 = 2
        btn_pressed = 1
        play()
    elif rec5 == 2:
        rec5 = 3
        btn_pressed = 1
        stop()
    print("Button 5 was pressed")

def srec6():
    if rec6 == 0:
        rec6 = 1
        btn_pressed = 1
        record()
    elif rec6 == 1:
        rec6 = 2
        btn_pressed = 1
        play()
    elif rec6 == 2:
        rec6 = 3
        btn_pressed = 1
        stop()
    print("Button 6 was pressed")

def srec7():
    if rec7 == 0:
        rec7 = 1
        btn_pressed = 1
        record()
    elif rec7 == 1:
        rec7 = 2
        btn_pressed = 1
        play()
    elif rec7 == 2:
        rec7 = 3
        btn_pressed = 1
        stop()
    print("Button 7 was pressed")

def srec8():
    if rec8 == 0:
        rec8 = 1
        btn_pressed = 1
        record()
    elif rec8 == 1:
        rec8 = 2
        btn_pressed = 1
        play()
    elif rec8 == 2:
        rec8 = 3
        btn_pressed = 1
        stop()
    print("Button 8 was pressed")




rotor.when_rotated = set_timeperiod


btn1.when_pressed = srec1
btn2.when_pressed = srec2
btn3.when_pressed = srec3
btn4.when_pressed = srec4
btn5.when_pressed = srec5
btn6.when_pressed = srec6
btn7.when_pressed = srec7
btn8.when_pressed = srec8