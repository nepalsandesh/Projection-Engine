from .ui import TextUI,  Panel, Button
import pygame

# These are Text UI instances of double pendulum
mass1Index = TextUI("Mass-1 : ", (1605+20,65), (255,255,255,15))
mass2Index = TextUI("Mass-2 : ", (1605+20,105), (255,255,255,15))
length1Index = TextUI("Length-1 : ", (1605+20,145), (255,255,255,15))
length2Index = TextUI("Length-2 : ", (1605+20,185), (255,255,255,15))
gravityIndex = TextUI("Gravity : ", (1605+20,225), (255,255,255,15))


pause_text = TextUI("Press 'space' to Pause",(30,45), (50,165,165))
curve_text = TextUI("Press 'C' to display Position Curve", (pause_text.position[0], pause_text.position[1]+ 25), (50,165,165))
theta1_index = TextUI("Theta-1 : ", (pause_text.position[0], pause_text.position[1]+ 55), (165,165,165))
theta2_index = TextUI("Theta-2 : ", (pause_text.position[0], pause_text.position[1]+ 80), (165,165,165))
fps_Index = TextUI("FPS : ", (pause_text.position[0], pause_text.position[1]+ 105), (165,165,165))