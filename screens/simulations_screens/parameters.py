from .ui import TextUI,  Panel, Button
import pygame

# for double pendulum
panel_pendulum = Panel((1920-365, 20), color=(155,155,0))

mass1Index = TextUI("Mass-1 : ", (1555,70), (255,255,255,15))
mass2Index = TextUI("Mass-2 : ", (1555,100), (255,255,255,15))
length1Index = TextUI("Length-1 : ", (1555,130), (255,255,255,15))
length2Index = TextUI("Length-2 : ", (1555,160), (255,255,255,15))
gravityIndex = TextUI("Gravity : ", (1555,190), (255,255,255,15))




