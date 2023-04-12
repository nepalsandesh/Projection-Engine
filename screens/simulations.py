import pygame 
from ui import Button


class Simulation:
    def __init__(self, screen, resolution, clock, FPS=60):
        self.screen = screen
        self.WIDTH = resolution[0]
        self.HEIGHT = resolution[1]
        self.running = True
        self.clock = clock
        self.FPS = 60
        
        # BUTTONS
        self.SHMbutton = Button(self.WIDTH//2 - 100, self.HEIGHT//3, 300, 60, "Simple Harmonic Motion")
        self.ChaosAttractorButton = Button(self.WIDTH//2 - 100, self.HEIGHT//3+100, 300, 60, "Chaos and Attractor")
        self.GameofLifeButton = Button(self.WIDTH//2 - 100, self.HEIGHT//3+200, 300, 60, "Conways Game of Life")
        
        
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
                    pygame.draw.circle(self.screen, (255,255,255), (500, 500), 10)
                    pygame.display.flip()
                
            elif self.ChaosAttractorButton.Draw(self.screen):
                pass
            elif self.GameofLifeButton.Draw(self.screen):
                pass
            
            pygame.display.update()
        
        # setiing self.running to True because after exiting it would again be True for next time 
        self.running = True
            
            
            
            