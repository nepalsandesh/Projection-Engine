from .ui import TextUI,  Panel, Button
import pygame

# for double pendulum
panel_pendulum = Panel((1920-365, 20), color=(155,155,0))

mass1 = TextUI("Mass-1 : ", (1635, 20+20), (155,155,155))
mass2 = TextUI("Mass-2 : ", (1635, 20+40), (155,155,155))
theta1 = TextUI("Theta-1 : ", (1635, 20+60), (155,155,155))
theta2 = TextUI("Theta-2 : ", (1635, 20+80), (155,155,155))
theta1_value = TextUI("", (1635 + 70, 20+60), (155,155,155))
theta2_value = TextUI("", (1635 + 70, 20+80), (155,155,155))
length1 = TextUI("Length-1 : ", (1635, 20+100), (155,155,155))
length2 = TextUI("Length-2 : ", (1635, 20+100), (155,155,155))



