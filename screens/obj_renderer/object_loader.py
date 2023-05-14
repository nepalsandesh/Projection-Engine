from ui import Panel
from screens.simulations_screens.ui import Button, Panel, TextUI
import pygame
import os
import glob
from .render import SoftwareRender


file_panel = Panel((1920/2-300, 1080/4), 600, 600, (25,25,155),alpha=50)
txt = TextUI("Click on any object to Render", (file_panel.position[0] +150, file_panel.position[1]-40), (50,125,125))

files = glob.glob('resources/*.obj')

def run(screen, resolution, clock, FPS):
    while True:
        x,y = file_panel.position[0] + 50, file_panel.position[1] + 50
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or pygame.K_BACKSPACE:
                    return
        screen.fill((0,0,0)) 
        file_panel.render(screen)
        txt.render(screen)
        for file in files:
            obj_file = (os.path.split(file))[1]            
            b = Button(x, y, 500, 40, text=str(obj_file))
            b.render(screen)
            y += 50

            if b.Update():
                SoftwareRender(screen, resolution, clock, FPS, str(obj_file)).run()
                
        

        pygame.display.flip()