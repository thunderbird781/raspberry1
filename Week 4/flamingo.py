#makes a walking flamingo on sense_HAT

from sense_hat import SenseHat
from time import sleep



m = (255,0,255) #magenta
e = (0,0,0) #empty

flamingo1 =[
    e,e,e,e,e,m,m,e,
    e,e,e,e,e,m,e,e,
    e,e,e,m,m,m,e,e,
    e,e,m,m,m,e,e,e,
    e,e,e,m,e,e,e,e,
    e,e,e,m,e,e,e,e,
    e,e,m,e,m,e,e,e,
    e,e,m,e,m,e,e,e
    ]

flamingo2 =[
    e,e,e,e,e,m,m,e,
    e,e,e,e,e,m,e,e,
    e,e,e,m,m,m,e,e,
    e,e,m,m,m,e,e,e,
    e,e,e,m,e,e,e,e,
    e,e,e,m,e,e,e,e,
    e,e,e,m,m,e,e,e,
    e,e,e,m,e,m,e,e
    ]

sense.clear()

def flamingo():
    for i in range(222):
        sense.set_pixels(flamingo1)
        sleep(0.5)
        sense.set_pixels(flamingo2)
        sleep(0.5)

x,y,z = sense.get_accelerometer_raw().values()

while x< and y<2 and z<2:
    x,y,z = sense.get_accelerometer_raw().values()
    

flamingo()



sense.clear()
