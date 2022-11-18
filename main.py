import pyaudio
import numpy as np
import time
import os
from gpiozero import LED, Button, RotaryEncoder

greenled1 = LED(3)
greenled2 = LED(5)
greenled3 = LED(7)
greenled4 = LED(11)

