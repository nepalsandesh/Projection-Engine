import pygame
from .ui import RenderText, Button, Panel, TextUI, RadioButton

panel = Panel((20, 20), 300, 400, (55, 55, 100), 80)

# button to append body in bodies 
add_body_button = Button(
    x=panel.position[0] + 100,
    y=panel.position[1] + 350,
    w=100, h=30, text="Add Body",
   
)

(x,y) = panel.position

distance_text_UI = TextUI("Distance: ", position=(x+20, y+20), fontColor=(255,255,255))
distance_plus_button = RadioButton(x+220, y+20, 20, 20, "+")
distance_minus_button = RadioButton(x+250, y+20, 20, 20, "-")

scale_text_UI = TextUI("Scale: ", position=(x+20, y+50), fontColor=(255,255,255))
scale_plus_button = RadioButton(x+220, y+50, 20, 20, "+")
scale_minus_button = RadioButton(x+250, y+50, 20, 20, "-")

display_orbit_text_UI = TextUI("Display Orbit:", position=(x+20, y+ 80), fontColor=(255, 255, 255))
display_orbit_radiobutton = RadioButton(x+220, y+80, 50, 20, "Orbit")

rotation_speed_text_UI = TextUI("Rotation Speed:", position=(x+20, y+110), fontColor=(255, 255, 255))
rotation_speed_plus_button = RadioButton(x+220, y+110, 20, 20, "+")
rotation_speed_minus_button = RadioButton(x+250, y+110, 20, 20, "-")

fps_text_UI = TextUI("FPS: ", position=(x+20, y+ 150), fontColor=(255, 255, 255))

rotate_text_UI = TextUI("Rotate: ", position=(x+20, y+180), fontColor=(255,255,255))
rotate_x_radiobutton = RadioButton(x+130, y+180, 20, 20, "x")
rotate_y_radiobutton = RadioButton(x+160, y+180, 20, 20, "y")
rotate_z_radiobutton = RadioButton(x+190, y+180, 20, 20, "z")

save_images_button = RadioButton(x+20, y+210, 260, 20, "Save Images")