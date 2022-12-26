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
#import drivers
from time import sleep
from threading import Event
import RPi.GPIO as gpio 
#from pad4pi import rpi_gpio

##################################################################
##                         SOME DECLARATIONS                    ##
##################################################################
gpio.setmode(gpio.BCM)
shift_register = pi74HC595()

##################################################################
##                             VARIABLES                        ##
##################################################################
done = Event()
lcd_columns = 16
lcd_rows = 2




##################################################################
##                          PI CONNECTIONS                      ##
##################################################################
##LCD
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
#ROTARY ENCODER
rotor = RotaryEncoder(16, 20, wrap=True, max_steps=180)
#SHIFT REGISTER
shift_register.set_ds(7) 
shift_register.set_sh(37)
shift_register.set_st(22)
shift_register.set_daisy_chain(6)

##################################################################
##                          FUNCTIONS                           ##
##################################################################







































#TO KEEP THE PROGRAM RUNNING FOREVER
done.wait()