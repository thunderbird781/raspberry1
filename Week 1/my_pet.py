#makes a walking flamingo on sense_HAT

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

o = (255,125,0) #orange
y = (255,255,0) #yellow
e = (0,0,0) #empty

bonfire1 =[
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,o,e,e,e,e,
    e,e,o,o,o,e,e,e,
    e,o,o,y,o,o,e,e,
    e,o,y,y,y,o,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

bonfire2 =[
    e,e,e,e,e,e,e,e,
    e,e,e,o,e,e,e,e,
    e,e,o,o,o,e,e,e,
    e,o,o,o,o,o,e,e,
    e,o,o,y,o,o,e,e,
    e,o,y,y,y,o,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

sense.clear()

def bonfire():
    for tanno in range(60):
        sense.set_pixels(bonfire1)
        sleep(0.5)
        sense.set_pixels(bonfire2)
        sleep(0.5)

x,y,z = sense.get_accelerometer_raw().values()

while x<2 and y<2 and z<2:
    x,y,z = sense.get_accelerometer_raw().values()


bonfire()


#challenge idea: shake to turn it on; shake to turn it off
sense.clear()
