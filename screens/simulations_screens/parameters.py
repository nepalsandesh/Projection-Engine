from .ui import TextUI,  Panel, Button
import pygame

# These are Text UI instances of double pendulum
mass1Index = TextUI("Mass-1 : ", (1605+20,65), (255,255,255,15))
mass2Index = TextUI("Mass-2 : ", (1605+20,105), (255,255,255,15))
length1Index = TextUI("Length-1 : ", (1605+20,145), (255,255,255,15))
length2Index = TextUI("Length-2 : ", (1605+20,185), (255,255,255,15))
gravityIndex = TextUI("Gravity : ", (1605+20,225), (255,255,255,15))


pause_text = TextUI("Press 'space' to Pause",(30,55), (50,165,165))
curve_text = TextUI("Press 'C' to display Position Curve", (pause_text.position[0], pause_text.position[1]+ 25), (50,165,165))
theta1_index = TextUI("Theta-1 : ", (pause_text.position[0], pause_text.position[1]+ 55), (165,165,165))
theta2_index = TextUI("Theta-2 : ", (pause_text.position[0], pause_text.position[1]+ 80), (165,165,165))
fps_Index = TextUI("FPS : ", (pause_text.position[0], pause_text.position[1]+ 105), (165,165,165))

pause_text.fontSize = 18
curve_text.fontSize = 18
theta1_index.fontSize = 18
theta2_index.fontSize = 18
fps_Index.fontSize = 18


# UI instances of Conway
conway_panel = Panel(color=(30,30,55), w=275, h=300, position=(1920-285,10))
scale_panel = Panel((conway_panel.position[0] + 90, conway_panel.position[1]+20), 80, 50, (55,155,155))
conway_panel.alpha = 230

scale_index = TextUI("Scale : ", (conway_panel.position[0]+15, conway_panel.position[1]+35), (255,255,255))
scale_value = TextUI('', (scale_panel.position[0]+15, scale_panel.position[1]+15), (255,255,255))

grid_shape_index = TextUI("Grid shape : ", (conway_panel.position[0]+15, conway_panel.position[1] + 90),(155,200,255))
total_cells_index = TextUI("Total Cells : ", (conway_panel.position[0]+15, conway_panel.position[1] + 120),(155,200,255))
alive_cells_index = TextUI("Total Alive Cells : ", (conway_panel.position[0]+15, conway_panel.position[1] + 150), (155,200,255))
dead_cells_index = TextUI("Total Dead Cells : ", (conway_panel.position[0]+15, conway_panel.position[1] + 180), (155,200,255))
fps = TextUI("FPS : ", (conway_panel.position[0]+15, conway_panel.position[1]+210), (155,200,255))
pause_text_conway = TextUI("Press 'space' to pause", (conway_panel.position[0]+15, conway_panel.position[1]+250), (255,190,255))

grid_shape_index.fontSize = 18
total_cells_index.fontSize = 18
alive_cells_index.fontSize = 18
dead_cells_index.fontSize = 18
fps.fontSize = 18



RunButton = Button(conway_panel.position[0] + 180, conway_panel.position[1]+20, 80, 50, "RUN")
RunButton.initial_color = (100,100,140)
RunButton.text_color = (255,255, 255)
