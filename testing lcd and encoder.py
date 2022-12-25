import time
import Adafruit_CharLCD as LCD
from threading import Event
from gpiozero import RotaryEncoder, Button
rotor = RotaryEncoder(16, 20, wrap=True, max_steps=180)
rotor.steps = 160

done = Event()

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

def text():
    lcd.clear()
    text = rotor.steps
    text_string = str(text)
    print(text)
    sr = 'tempo: ' + text_string + ' BPM'
    lcd.message(sr)

rotor.when_rotated = text
done.wait()
