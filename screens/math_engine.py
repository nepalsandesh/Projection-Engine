import pygame 
from ui import Button, Panel
from screens.MathEngine.Calculus_Engine.calculus_engine import Render


class MathEngine:
    def __init__(self, screen, resolution, clock, FPS=60):
        self.screen = screen
        self.resolution = resolution
        self.WIDTH = resolution[0]
        self.HEIGHT = resolution[1]
        self.running = True
        self.clock = clock
        self.FPS = 60
        
        # panel
        self.panel = Panel((810,300), 450, 500, (25, 25, 50))
        
        
        # BUTTONS
        self.TrigonometryButton = Button(self.WIDTH//2 - 100, self.HEIGHT//3, 350, 60, "Trigonometry Visualization")
        self.CalculusButton = Button(self.WIDTH//2 - 100, self.HEIGHT//3 + 100, 350, 60, "Calculus Engine")
        
        # Engines
        self.CalculusEngine = Render(self.resolution, 20, self.screen, self.clock, self.FPS)
             
        
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
                    
    def displayMenu(self):
        """Displays each buttons and runs the corresponding function if clicked"""
        
        self.panel.render(self.screen)
        
        if self.CalculusButton.Draw(self.screen):
            self.CalculusEngine.run()
        elif self.TrigonometryButton.Draw(self.screen):
            print("Trigonometry button clicked")

 
    
    def run_menu(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.clear_screen()
            self.check_events()

            self.displayMenu()
            pygame.display.update()
            
        self.running = True
            
        
        # setiing self.running to True because to make it would again be True for next time 
        
            
            
            
            