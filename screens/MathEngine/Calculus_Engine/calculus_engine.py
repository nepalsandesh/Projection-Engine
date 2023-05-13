import pygame
import numpy as np
from sympy import symbols, sin, cos, lambdify, diff
from sympy.parsing.sympy_parser import parse_expr
from .fx_and_dfx import FunctionAndDerivative, WindowCoordinante
from .ui import TextUI,  Button
from .parameters import *

class Render:
    """"Main class for starting and rendering a Calculus Engine"""
    def __init__(self, RESOLUTION, SCALE, screen, clock, FPS):
        self.RESOLUTION = RESOLUTION
        self.WIDTH, self.HEIGHT = self.RESOLUTION
        self.screen = screen
        self.clock = clock
        self.FPS = FPS
        self.SCALE = SCALE
        self.running = True
        
        self.func = WindowCoordinante((1920,1080), self.SCALE, "sin(x)", np.linspace(-50,50,1001))
        self.pause = False
        self.display_derivative =  False
        self.display_tangent = False
        
        self.x_point = -20
        self.tangent_point = None

        self.input_text = self.func.expression
        
        # UI 
        # UI paraeter
        self.panel = Panel(position = (Width-300, 15), w= 500, h= 150, color=(55, 55, 155), alpha=50)


# Text UI
        self.functionIndex = TextUI("f(x) = ", (self.panel.position[0] + 15, self.panel.position[1] + 15), (255, 255, 255), "topleft")
        self.derivativeIndex = TextUI("f'(x) = ", (self.panel.position[0] + 15, self.panel.position[1] + 50), (255, 255, 255), "topleft")
        self.tangentIndex = TextUI("tangent at :", (30, 30), (255, 255, 255), "topleft")

        self.functionIndex.fontSize = 25
        self.derivativeIndex.fontSize = 25
        
        self.functionPanel = Panel((self.panel.position[0] + 85, self.panel.position[1] + 15), 200, 30, (155,155,155))
        
        self.functionText = TextUI(self.input_text, (self.functionPanel.position[0] + 20, self.functionPanel.position[1] + 5), (255, 255, 255))
        self.derivativeText = TextUI(str(self.func.df), (self.functionText.position[0] , self.functionText.position[1] + 30), (255, 255, 255))
        self.tangentPointText = TextUI(str(self.tangent_point), (self.tangentIndex.position[0] + 100 , self.tangentIndex.position[1]), (255, 255, 255))  
        
        self.functionText.fontSize = 20
        
    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_EQUALS]:
            self.func.SCALE += 0.5
        if keys[pygame.K_MINUS]:
            self.func.SCALE -= 0.5
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key == pygame.K_p:
                    self.pause = True if self.pause==False else False
                    
                if event.key == pygame.K_d:
                    self.display_derivative = True if self.display_derivative==False else False
                
                if event.key == pygame.K_t:
                    self.display_tangent = True if self.display_tangent==False else False
                    
                if self.functionPanel.get_hover_status():
                    if event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[0:-1]
                        
                    else:
                        self.input_text += event.unicode
                
                
    def draw(self):
        pygame.draw.line(self.screen, (55,55,55), (0, self.HEIGHT//2), (1920, self.HEIGHT//2), 3)   # x-axis
        pygame.draw.line(self.screen, (55,55,55), (self.WIDTH//2, 0), (self.WIDTH//2, self.HEIGHT), 3)   # y-axis
        
        pygame.draw.lines(self.screen, (50, 50, 100), False, self.func.get_function_coordinates(), 2)   # function curve

        
        if self.display_tangent:
            pygame.draw.lines(self.screen, (105,105,15), False, self.func.get_tangent_coordinates(self.x_point), 5)  # tangent line
            self.tangent_point = self.func.get_tangent_point(self.x_point)
            if self.tangent_point[0] >= 0 and self.tangent_point[0] <= self.WIDTH:
                pygame.draw.circle(self.screen, (255,155,155), self.tangent_point, 7)   # tangent point
            
        if self.display_derivative:
            pygame.draw.lines(self.screen, (25, 50, 25), False, self.func.get_derivative_coordinates(), 2)   # derivative curve

          

    def draw_interaction_panel(self):
        """A function for Interaction."""
        self.panel.render(self.screen)
        self.functionPanel.render(self.screen)
        
        self.functionIndex.render(self.screen)
        self.derivativeIndex.render(self.screen)
        self.tangentIndex.render(self.screen)
        self.functionText.render(self.screen)
        self.derivativeText.render(self.screen)
        
        tangent_point = ("(%f, %f)" %(self.x_point, self.func.f.subs(self.func.x, self.x_point)))
        self.tangentPointText.text = tangent_point
        self.tangentPointText.render(self.screen)

        
    def update_parameters(self):
        self.functionText.text = self.input_text
        run_button = Button(self.panel.position[0]+20, self.panel.position[1]+110, 60, 30, 'RUN').render(self.screen)
        if run_button:
            self.func = WindowCoordinante((1920,1080), self.SCALE, str(self.input_text), np.linspace(-50,50,1001))
            self.derivativeText.text = str(self.func.df)
            self.tangentPointText.text = str(self.tangent_point)
            self.x_point = -20          
        
        
    def run(self):
        while self.running:
            self.clock.tick()
            self.screen.fill((0,0,0))
            pygame.display.set_caption(str(np.round(self.clock.get_fps())))
            
            self.handle_events()
            self.draw()
            self.draw_interaction_panel()   
            
            if  self.pause:
                self.x_point += 0.0 
            if not self.pause:
                self.x_point += 0.01

            self.update_parameters()
            self.panel.get_hover_status()

            pygame.display.flip()
        self.running = True
    

        



# if __name__ == "__main__":
#     width = 1920
#     height = 1080
#     resolution = (width, height)
#     pygame.init()
#     screen = pygame.display.set_mode(resolution)
#     pygame.display.set_caption("Calculus Engine")
#     clock = pygame.time.Clock()
#     FPS = 60
#     app = Render(resolution, 20, screen, clock, FPS)
#     app.run()