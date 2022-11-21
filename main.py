import pyaudio
import numpy as np
import time
import os
import RPi.GPIO
import pygame
import wave
from gpiozero import LED, Button, RotaryEncoder

# rec numbers meanings
# 0 = empty
# 1 = recording
# 2 = playing


settime = 5
timeperiod = 0.6
def changetempo():
    timeperiod = settime/4 




# play leds
greenled1 = LED(2)
greenled2 = LED(3)
greenled3 = LED(4)
greenled4 = LED(5)

# recording leds
redled1 = LED(6)
redled2 = LED(7)
redled3 = LED(8)
redled4 = LED(9)

# recording buttons
btn1 = Button(10)
btn2 = Button(11)
btn3 = Button(12)
btn4 = Button(13)

# some more vars
rec1 = 0
rec2 = 0
rec3 = 0
rec4 = 0

def srec1():
    if rec1 == 0:
        rec1 = 1
        redled1.on
        # rec function start
    elif rec1 == 1:
        rec1 = 2
        redled1.off
        greenled1.on
        # rec function stop + play
    elif rec1 == 2:
        rec1 = 0
        greenled1.off
        # delete rec file
    print("started recording in channel 1")

def srec2():
    if rec2 == 0:
        rec2 = 1
        redled2.on
        # rec function start
    elif rec2 == 1:
        rec2 = 2
        redled2.off
        greenled1.on
        # rec function stop + play
    elif rec2 == 2:
        rec2 = 0
        rec2 = 0
        greenled2.off
        # delete rec file
    print("started recording in channel 2")

def srec3():
    if rec3 == 0:
        rec3 = 1
        redled3.on
        # rec function start
    elif rec3 == 1:
        rec3 = 2
        redled3.off
        greenled3.on
        # rec function stop + play
    elif rec3 == 2:
        rec3 = 0
        greenled3.off
        # delete rec file
    print("started recording in channel 3")

def srec4():
    if rec4 == 0:
        rec4 = 1
        redled4.on
        # rec function start
    elif rec4 == 1:
        rec4 = 2
        redled4.off
        greenled4.on
        # rec function stop + play
    elif rec4 == 2:
        rec4 = 0
        greenled4.off
        # delete rec file
    print("started recording in channel 1")

btn1.when_pressed = srec1
btn2.when_pressed = srec2
btn3.when_pressed = srec3
btn4.when_pressed = srec4
