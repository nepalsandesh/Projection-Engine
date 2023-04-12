import pygame 
from constants import *
from ui import Button
from screens.chaos import Chaos


class Render:
    """Main Rendering class"""
    def __init__(self):
        pygame.init()
        self.WIDTH = 1920
        self.HEIGHT = 1080
        self.RESOLUTION = (self.WIDTH, self.HEIGHT)
        self.screen = pygame.display.set_mode(self.RESOLUTION)
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.running = True
        
        # BUTTONS
        self.ChaosEquationButton = Button(WIDTH//2 - 100, self.HEIGHT//3, 200, 60, "Chaos Equation")
        self.SimulationButton = Button(WIDTH//2 - 100, self.HEIGHT//3 + 100, 200, 60, "Simulations")
        self.MathEngineButton = Button(WIDTH//2 - 100, self.HEIGHT//3 + 200, 200, 60, "Math Engine")
        self.ObjRenderButton = Button(WIDTH//2 - 100, self.HEIGHT//3 + 300 , 200, 60, "Object Render")
        self.AlgVizButton = Button(WIDTH//2 - 100, self.HEIGHT//3 + 400 , 200, 60, "Algorithms Visualization")
        
        
        # SCREENS
        self.chaosScreen = Chaos(self.screen, self.clock)
    
    def clear_screen(self):
        self.screen.fill((0,0,0))
        
    def displayMainMenu(self):
        if self.ChaosEquationButton.Draw(self.screen):
            self.chaosScreen.Run()
        elif self.SimulationButton.Draw(self.screen):
            pass
        elif self.MathEngineButton.Draw(self.screen):
            pass
        elif self.ObjRenderButton.Draw(self.screen):
            pass
        elif self.AlgVizButton.Draw(self.screen):
            pass
    
    def check_events(self):
        [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
        
    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.clear_screen()
            self.check_events()
            
            self.displayMainMenu()
            
            pygame.display.update()
            


            
            
            
        
if __name__ == "__main__":
    app = Render()
    app.run()