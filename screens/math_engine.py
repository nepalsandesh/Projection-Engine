import pygame 
from ui import Button
from screens.MathEngine.trigonometry import trigonometry

class MathEngine:
    def __init__(self, screen, resolution, clock, FPS=60):
        self.screen = screen
        self.resolution = resolution
        self.WIDTH = resolution[0]
        self.HEIGHT = resolution[1]
        self.running = True
        self.clock = clock
        self.FPS = 60
        
        
        
        # BUTTONS
        self.TrigonometryButton = Button(self.WIDTH//2 - 100, self.HEIGHT//3, 350, 60, "Trigonometry Visualization")
             
        
    def clear_screen(self):
        self.screen.fill((0,0,0))
        
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_BACKSPACE:
                    self.running = False  
  
    
    def run_menu(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.clear_screen()
            self.check_events()
            
            if self.TrigonometryButton.Draw(self.screen):
                Trigonometry = trigonometry.Trigonometry()
                if Trigonometry.running:
                    Trigonometry.run()
                

            
            pygame.display.update()
        
        # setiing self.running to True because after exiting it would again be True for next time 
        
            
            
            
            