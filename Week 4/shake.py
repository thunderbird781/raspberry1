
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

x,y,z = sense.get_accelerometer_raw().values()

while x<2 and y<2 and z<2:
    x,y,z = sense.get_accelerometer_raw().values()
    
print ("earthquake")
