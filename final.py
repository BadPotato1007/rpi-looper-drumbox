from pydub import AudioSegment
from pydub.playback import play
from gpiozero import LED, Button, RotaryEncoder

# rec numbers meanings
# 0 = empty
# 1 = recording
# 2 = playing
# 3 = muted

rotor = RotaryEncoder(16, 20, wrap=True)

beat_time = 4
beat_tempo = 120

def set_timeperiod():
    beat_tempo = rotor.steps
    beat_time = beat_tempo/15
    print("set the bet time to "+ beat_tempo +" and the beat tempo to "+ beat_tempo)
    

rotor.when_rotated = set_timeperiod
    