import pygame 
from ui import Button
from screens.simulations_screens import doublePendulum, conway

class Simulation:
    def __init__(self, screen, resolution, clock, FPS=60):
        self.screen = screen
        self.resolution = resolution
        self.WIDTH = resolution[0]
        self.HEIGHT = resolution[1]
        self.running = True
        self.clock = clock
        self.FPS = 60
        
        
        
        #SIMULATION BUTTONS
        self.SHMbutton = Button(self.WIDTH//2 - 100, self.HEIGHT//3, 300, 60, "Simple Harmonic Motion")
        self.ChaosAttractorButton = Button(self.WIDTH//2 - 100, self.HEIGHT//3+100, 300, 60, "Chaos and Attractor")
        self.GameofLifeButton = Button(self.WIDTH//2 - 100, self.HEIGHT//3+200, 300, 60, "Conways Game of Life")
        
        #SUB Buttons 
        self.DoublePendulumButton = Button(self.WIDTH//1.5 - 100, self.HEIGHT//3, 300, 60, "Double Pendulum")
        
        
        
    def clear_screen(self):
        self.screen.fill((0,0,0))
        
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
  
    
    def run_menu(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.clear_screen()
            self.check_events()
            
            if self.SHMbutton.Draw(self.screen):
                while self.running:
                    self.clock.tick(self.FPS)
                    self.clear_screen()
                    self.check_events()
                    if self.DoublePendulumButton.Draw(self.screen):
                        double_pendulum = doublePendulum.DoublePendulum(self.screen, self.resolution, self.clock, self.FPS)
                        double_pendulum.render()
                    pygame.display.flip()
                self.running = True
                
            elif self.ChaosAttractorButton.Draw(self.screen):
                while self.running:
                    self.clock.tick(self.FPS)
                    self.clear_screen()
                    self.check_events()
                    pygame.draw.circle(self.screen, (255,255,255), (500, 500), 50)
                    pygame.display.flip()
                self.running = True
                
            elif self.GameofLifeButton.Draw(self.screen):
                Conway = conway.ConwaysGameOfLife(self.screen, self.resolution, self.clock, self.FPS)
                while Conway.running:
                    # self.clock.tick(self.FPS)
                    # self.clear_screen()
                    # self.check_events()
                    Conway.run()
                
            
            pygame.display.update()
        
        # setiing self.running to True because after exiting it would again be True for next time 
        self.running = True
            
            
            
            