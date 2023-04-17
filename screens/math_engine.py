import pygame 
from ui import Button


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
        self.FunctionVisualizationButton = Button(self.WIDTH//2 - 100, self.HEIGHT//3+100, 350, 60, "Function Visualization")
             
        
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
        if self.TrigonometryButton.Draw(self.screen):
            print("Trigonometry button clicked")
        elif self.FunctionVisualizationButton.Draw(self.screen):
            print("Function Visualizer clicked")
 
    
    def run_menu(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.clear_screen()
            self.check_events()

            self.displayMenu()
            pygame.display.update()
            
        self.running = True
            
        
        # setiing self.running to True because to make it would again be True for next time 
        
            
            
            
            