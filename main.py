




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

##################################################################
##                        THE CONNECTIONS                       ##
##################################################################
rotor = RotaryEncoder(16, 20, wrap=True) #rotry encoder

lcd_columns = 16 #lcd
lcd_rows = 2 #lcd



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



lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight) #lcd



##################################################################
##                            VARIABLES                         ##
##################################################################
beat_tempo = 100
beat_time = 1
rec_in_file = "rec_in.wav"

##################################################################
##                   THE DIFFERENT PROGRAMS USED                ##
##################################################################





##################################################################
##                        THE ROTRY ENCODER                     ##
##################################################################
def set_timeperiod():
    beat_tempo = rotor.steps
    beat_time = beat_tempo/15
    timeperiod = beat_time/4 
    print("set the bet time to "+ beat_tempo +" and the beat tempo to "+ beat_tempo)






##################################################################
##                          THE LCD CODE                        ##
##################################################################
display = drivers.Lcd()

def display():
    beat_tempo_str = str(beat_tempo)
    beat_time_str = str(beat_time)
    line = ("tempo: " + beat_tempo_str + "    " + beat_time_str + "s") #make the text to display on the lcd
    print("Writing to display...")
    display.lcd_display_string(" DRUMBOX LOOPER ", 1)  # Write line of text to first line of display
    display.lcd_display_string(line, 2)  # Write line of text to second line of display



##################################################################
##                       THE MIXING FUNCTION                    ##
##################################################################

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
        print("--> mixed 1")

    if rec2 == 2:
        mixed = mixed.overlay(audio2)
    else:
        print("--> mixed 2")

    if rec3 == 2:
        mixed = mixed.overlay(audio3)
    else:
        print("--> mixed 3")

    if rec4 == 2:
        mixed = mixed.overlay(audio4)
    else:
        print("--> mixed 4")

    if rec5 == 2:
        mixed = mixed.overlay(audio5)
    else:
        print("--> mixed 5")

    if rec6 == 2:
        mixed = mixed.overlay(audio6)
    else:
        print("--> mixed 6")

    if rec7 == 2:
        mixed = mixed.overlay(audio7)
    else:
        print("--> mixed 7")

    if rec8 == 2:
        mixed = mixed.overlay(audio8)
    else:
        print("--> mixed 8")
    
    print("Mixing audio...")
    mixed.export("mixed.wav", format='wav') #export mixed  audio file
    print("Audio mixed...")



##################################################################
##                         PLAY THE AUDIO                       ##
##################################################################
def play_audio():
    print("Playing audio...")
    mixed_file = AudioSegment.from_file("mixed.wav") #load mixed audio file
    loop_count = 0
    while loop_count<=200:
        play(mixed_file)                             #play mixed audio file
        loop_count = loop_count + 1                  #loop the audio 200 times





##################################################################
##                           UPDATE LEDS                        ##
##################################################################



def update_leds():
    print("updating leds")              #update the leds















##################################################################
##                       RECORDING FUNCTION                     ##
##################################################################




def record():                          #record function
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * beat_time)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(rec_in_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()




##################################################################
##                     THE RECORDING FUNCTIONS                  ##
##################################################################

def rec_func1():                                 #recording function 1
    if rec1 == 0:
        rec1 = 1
        print("recording... CHANNEL 1")
        r1 = 1
        g1 = 0
        b1 = 0
        rec_in_file = "rec1_file.wav"
        record()
        update_leds()
        ###############################
    elif rec1 == 1:
        rec1 = 2
        print("playing... CHANNEL 1")
        r1 = 0
        g1 = 1
        b1 = 0
        play(rec1_file)
        update_leds()
        ###############################
    elif rec1 == 2:
        rec1 = 3
        r1 = 0
        g1 = 0
        b1 = 1
        print("muted... CHANNEL 1")
        update_leds()
        ################################
        
def rec_func2():                                 #recording function 2
    if rec2 == 0:
        rec2 = 1
        print("recording... CHANNEL 2")
        r2 = 1
        g2 = 0
        b2 = 0
        rec_in_file = "rec2_file.wav"
        record()
        update_leds()
        ################################
    elif rec2 == 1:
        rec2 = 2
        print("playing... CHANNEL 2")
        r2 = 0
        g2 = 1
        b2 = 0
        play(rec2_file)
        update_leds()
        ################################
    elif rec2 == 2:
        rec2 = 3
        r2 = 0
        g2 = 0
        b2 = 1
        print("muted... CHANNEL 2")
        update_leds()
        ################################

def rec_func3():                                 #recording function 3
    if rec3 == 0:
        rec3 = 1
        print("recording... CHANNEL 3")
        r3 = 1
        g3 = 0
        b3 = 0
        rec_in_file = "rec3_file.wav"
        record()
        update_leds()
        ################################
    elif rec3 == 1:
        rec3 = 2
        print("playing... CHANNEL 3")
        r3 = 0
        g3 = 1
        b3 = 0
        play(rec3_file)
        update_leds()
    elif rec3 == 2:
        rec3 = 3
        r3 = 0
        g3 = 0
        b3 = 1
        print("muted... CHANNEL 3")
        update_leds()
        ################################

def rec_func4():                                 #recording function 4
    if rec4 == 0:
        rec4 = 1
        print("recording... CHANNEL 4")
        r4 = 1
        g4 = 0
        b4 = 0
        rec_in_file = "rec4_file.wav"
        record()
        update_leds()
        ################################
    elif rec4 == 1:
        rec4 = print("playing... CHANNEL 4")     
        r4 = 0
        g4 = 1
        b4 = 0
        play(rec4_file)
        update_leds()
        ################################
    elif rec4 == 2:
        rec4 = 3
        r4 = 0
        g4 = 0
        b4 = 1
        print("muted... CHANNEL 4")
        update_leds()
        ################################
        

        
           
        
            
        



























#################### RUNNING THE FUNCTIONS ###################
rotor.when_rotated = set_timeperiod
btn1.when_pressed = rec_func1
btn2.when_pressed = rec_func2
btn3.when_pressed = rec_func3
btn4.when_pressed = rec_func4
btn5.when_pressed = rec_func5
btn6.when_pressed = rec_func6
btn7.when_pressed = rec_func7
btn8.when_pressed = rec_func8

