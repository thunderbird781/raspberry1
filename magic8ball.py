from sense_hat import SenseHat
from time import sleep
import random

#8 ball responses
reply1 = "yes"
reply2 = "maybe"
reply3 = "reply hazy try again later"
reply4 = "dont count on it"
reply5 = "it will never happen"
reply6 = "no"
reply7 = "go complian on the internet"
reply8 = "why"

ball8_list = [reply1,reply2,reply3,reply4,reply5,reply6,reply7,reply8]


sense = SenseHat()
sense.clear()


x,y,z = sense.get_accelerometer_raw().values()
while x<2 and y<2 and z<2:
    x,y,z = sense.get_accelerometer_raw().values()
   

sense.show_message((random.choice(ball8_list)), text_colour=[125, 245, 0] , back_colour=[0, 0, 100], scroll_speed=0.2)
