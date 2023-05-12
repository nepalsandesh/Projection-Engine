from ui import Panel
from screens.simulations_screens.ui import Button
import pygame
import os
import glob
from .render import SoftwareRender


file_panel = Panel((1920/2, 1080/4), 300, 400, (255,255,255))

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
        for file in files:
            obj_file = (os.path.split(file))[1]            
            b = Button(x, y, 200, 40, text=str(obj_file))
            b.render(screen)
            y += 50

            if b.Update():
                SoftwareRender(screen, resolution, clock, FPS, str(obj_file)).run()
                
        

        pygame.display.flip()