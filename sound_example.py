import pygame.mixer
from pygame.mixer import Sound
from gpiozero import Button  
from signal import pause   

pygame.mixer.init()

Sound("samples/vinyl_rewind.wav").play()

pause()
