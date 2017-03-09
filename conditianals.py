#pressure

from sense_hat import SenseHat

sense = SenseHat()
pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)

if 1013 mbars of less, print 'No higher then average at sea level'
if over 1013 mbars, print 'Higher then average'





































