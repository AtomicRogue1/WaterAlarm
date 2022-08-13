import time
from playsound import playsound

while True:
    print("Water Break")
    playsound('a.wav', False)
    time.sleep(1.5)
    playsound('b.wav', False)
    time.sleep(60*60)
