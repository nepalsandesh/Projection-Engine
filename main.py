import pygame 
from constants import *
from ui import Button
from screens.simulations import Simulation



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
        self.ChaosEquationButton = Button(WIDTH//4 - 100, self.HEIGHT//10, 300, 60, "Chaos Equation")
        self.SimulationButton = Button(WIDTH//4 - 100, self.HEIGHT//10 + 100, 300, 60, "Simulations")
        self.MathEngineButton = Button(WIDTH//4 - 100, self.HEIGHT//10 + 200, 300, 60, "Math Engine")
        self.ObjRenderButton = Button(WIDTH//4 - 100, self.HEIGHT//10 + 300 , 300, 60, "Object Render")
        self.AlgVizButton = Button(WIDTH//4 - 100, self.HEIGHT//10 + 400 , 300, 60, "Algorithms Visualization")
        self.GamesButton = Button(WIDTH//4 - 100, self.HEIGHT//10 + 500 , 300, 60, "Games")
        
        # After Button Click
        self.Simulation = Simulation(self.screen, self.RESOLUTION, self.clock, self.FPS)
        
        
        
    
    def clear_screen(self):
        self.screen.fill((0,0,0))
        
    def displayMenu(self):
        if self.SimulationButton.Draw(self.screen):
            self.Simulation.run_menu()
        elif self.MathEngineButton.Draw(self.screen):
            self.MathEngine.Run()
        elif self.ObjRenderButton.Draw(self.screen):
            self.ObjRender.Run()
        elif self.AlgVizButton.Draw(self.screen):
            self.AlgViz.Run()
        elif self.GamesButton.Draw(self.screen):
            self.Games.Run()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
        
    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.clear_screen()
            self.check_events()
            
            self.displayMenu()
            
            pygame.display.update()
            


            
            
            
        
if __name__ == "__main__":
    app = Render()
    app.run()