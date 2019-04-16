import sounddevice as sd
import numpy as np
from subprocess import call

duration = 2000  # seconds
list =  []
volume = 0

def print_sound(indata, outdata, frames, time, status):
    global list
    global volume
    volume_norm = np.linalg.norm(indata)*10
    # print("|" * int(volume_norm))
    list.append(int(volume_norm))
    # print(list)
    if len(list) > 200:
        average = sum(list) / len(list)
        print(average)
        list = []
        if average >= 0:
            if average * 10 >= 0 and average * 10 < 20:
                call(["osascript -e 'set volume output volume 20'"], shell=True)

            elif average * 10 >= 20 and average * 10 < 40:
                call(["osascript -e 'set volume output volume 40'"], shell=True)

            elif average * 10 >= 40 and average * 10 < 60:
                call(["osascript -e 'set volume output volume 45'"], shell=True)

            elif average * 10 >= 60 and average * 10 < 70:
                call(["osascript -e 'set volume output volume 50'"], shell=True)

            elif average * 10 >= 70 and average * 10 < 100:
                call(["osascript -e 'set volume output volume 55'"], shell=True)

            elif average * 10 >= 100 and average * 10 < 120:
                call(["osascript -e 'set volume output volume 60'"], shell=True)

            elif average * 10 >= 120 and average * 10 < 160:
                call(["osascript -e 'set volume output volume 70'"], shell=True)

            elif average * 10 >= 160 and average * 10 < 250:
                call(["osascript -e 'set volume output volume 80'"], shell=True)

            elif average * 10 >= 250:
                call(["osascript -e 'set volume output volume 90'"], shell=True)

with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)

