import pygame
from constants import *



def main():
    """Main function for running the System"""
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption('Projection Engine')
    clock = pygame.time.Clock()
    
    engine = RenderEngine(screen, clock, 60)
    engine.run()
    
    pygame.quit()    
    

class RenderEngine:
    """Main Rendering Engine class"""
    def  __init__(self, screen, clock, FPS=60):
        self.screen = screen
        self.clock = clock
        self.FPS = FPS
        n_height = HEIGHT/4
        self.running = True
        
    def clearScreen(self):
        self.screen.fill(BLACK)
        
    def handleEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
        
    
    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.clearScreen()
            self.handleEvent()
            
            pygame.display.update()
            
            
if __name__ == '__main__':
    main()
            
        