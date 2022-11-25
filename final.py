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


# recording buttons
btn1 = Button(2)
btn2 = Button(3)
btn3 = Button(4)
btn4 = Button(5)
btn5 = Button(6)
btn6 = Button(7)
btn7 = Button(8)
btn8 = Button(9)

#the leds
shift_register = pi74HC595(7, 37, 22)

#some more vars
btn_pressed = 0
rotor = RotaryEncoder(16, 20, wrap=True)
beat_time = 4
beat_tempo = 120
rec1 = 0
beat_count = 0




# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)


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
    led()
    



def mix():
    audio1 = AudioSegment.from_file("rec1_file.wav") #your first audio file
    audio2 = AudioSegment.from_file("rec2_file.wav") #your second audio file
    audio3 = AudioSegment.from_file("rec3_file.wav")
    audio4 = AudioSegment.from_file("rec4_file.wav")
    audio5 = AudioSegment.from_file("rec5_file.wav")
    audio6 = AudioSegment.from_file("rec6_file.wav")
    audio7 = AudioSegment.from_file("rec7_file.wav")
    audio8 = AudioSegment.from_file("rec8_file.wav")
    if rec1 == 3:
        
        mixed = audio2.overlay(audio3)
        mixed = mixed.overlay(audio4)
        mixed = mixed.overlay(audio5)
        mixed = mixed.overlay(audio6)
        mixed = mixed.overlay(audio7)
        mixed = mixed.overlay(audio8)
        mixed.export("mixed.wav", format='wav') #export mixed  audio file
    elif rec2 == 3:
        mixed = audio1.overlay(audio3)
        mixed = mixed.overlay(audio4)
        mixed = mixed.overlay(audio5)
        mixed = mixed.overlay(audio6)
        mixed = mixed.overlay(audio7)
        mixed = mixed.overlay(audio8)
        mixed.export("mixed.wav", format='wav') #export mixed  audio file
    elif rec3 == 3:
        mixed = audio1.overlay(audio2)
        mixed = mixed.overlay(audio4)
        mixed = mixed.overlay(audio5)
        mixed = mixed.overlay(audio6)
        mixed = mixed.overlay(audio7)
        mixed = mixed.overlay(audio8)
        mixed.export("mixed.wav", format='wav') #export mixed  audio file
    elif rec4 == 3:
        mixed = audio1.overlay(audio2)
        mixed = mixed.overlay(audio3)
        mixed = mixed.overlay(audio5)
        mixed = mixed.overlay(audio6)
        mixed = mixed.overlay(audio7)
        mixed = mixed.overlay(audio8)
        mixed.export("mixed.wav", format='wav') #export mixed  audio file
    elif rec5 == 3:
        mixed = audio1.overlay(audio2)
        mixed = mixed.overlay(audio3)
        mixed = mixed.overlay(audio4)
        mixed = mixed.overlay(audio6)
        mixed = mixed.overlay(audio7)
        mixed = mixed.overlay(audio8)
        mixed.export("mixed.wav", format='wav') #export mixed  audio file
    elif rec6 == 3:
        mixed = audio1.overlay(audio2)
        mixed = mixed.overlay(audio3)
        mixed = mixed.overlay(audio4)
        mixed = mixed.overlay(audio5)
        mixed = mixed.overlay(audio7)
        mixed = mixed.overlay(audio8)
        mixed.export("mixed.wav", format='wav') #export mixed  audio file
    elif rec7 == 3:
        mixed = audio1.overlay(audio2)
        mixed = mixed.overlay(audio3)
        mixed = mixed.overlay(audio4)
        mixed = mixed.overlay(audio5)
        mixed = mixed.overlay(audio6)
        mixed = mixed.overlay(audio8)
        mixed.export("mixed.wav", format='wav') #export mixed  audio file
    elif rec8 == 3:
        mixed = audio1.overlay(audio2)
        mixed = mixed.overlay(audio3)
        mixed = mixed.overlay(audio4)
        mixed = mixed.overlay(audio5)
        mixed = mixed.overlay(audio6)
        mixed = mixed.overlay(audio7)
        mixed.export("mixed.wav", format='wav') #export mixed  audio file
    
                 
    
def led():
    lcd.message('tempo '+ beat_tempo + '    ' + beat_time + '\n' + beat_count )
    time.sleep(1)
    lcd.clear()

def srec1():
    if rec1 == 0:
        rec1 = 1
        record()
    elif rec1 == 1:
        rec1 = 2
        play()
    elif rec1 == 2:
        rec1 = 3
        btn_pressed = 1
        stop()
    print("Button 1 was pressed")

def srec2():
    if rec2 == 0:
        rec2 = 1
        record()
    elif rec2 == 1:
        rec2 = 2
        play()
    elif rec2 == 2:
        rec2 = 3
        btn_pressed = 2
        stop()
    print("Button 2 was pressed")

def srec3():
    if rec3 == 0:
        rec3 = 1
        record()
    elif rec3 == 1:
        rec3 = 2
        play()
    elif rec3 == 2:
        rec3 = 3
        btn_pressed = 3
        stop()
    print("Button 3 was pressed")

def srec4():
    if rec4 == 0:
        rec4 = 1
        record()
    elif rec4 == 1:
        rec4 = 2
        play()
    elif rec4 == 2:
        rec4 = 3
        btn_pressed = 4
        stop()
    print("Button 4 was pressed")

def srec5():
    if rec5 == 0:
        rec5 = 1
        record()
    elif rec5 == 1:
        rec5 = 2
        play()
    elif rec5 == 2:
        rec5 = 3
        btn_pressed = 5
        stop()
    print("Button 5 was pressed")

def srec6():
    if rec6 == 0:
        rec6 = 1
        record()
    elif rec6 == 1:
        rec6 = 2
        play()
    elif rec6 == 2:
        rec6 = 3
        btn_pressed = 6
        stop()
    print("Button 6 was pressed")

def srec7():
    if rec7 == 0:
        rec7 = 1
        record()
    elif rec7 == 1:
        rec7 = 2
        play()
    elif rec7 == 2:
        rec7 = 3
        btn_pressed = 7
        stop()
    print("Button 7 was pressed")

def srec8():
    if rec8 == 0:
        rec8 = 1
        record()
    elif rec8 == 1:
        rec8 = 2
        play()
    elif rec8 == 2:
        rec8 = 3
        btn_pressed = 8
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