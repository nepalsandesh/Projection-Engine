import pygame 


class Gravity:
    """Gravity Simulator Class, renders with run() function"""
    def __init__(self, screen, resolution, clock, FPS=60):         
        # Colors
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.blue = (0,0, 255)

        self.resolution = self.screen_width, self.screen_height = resolution
        self.screen = screen
        pygame.display.set_caption('Gravity Simulator')
        self.clock = clock
        self.FPS = 60
        self.running = True

        self.h0 = 500 # Initial heights in pixel
        self.m = 5 # Mass in kilograms
        self.g = 9.8 # Acceleration due to gravity in m/s^2
        self.dt = 0.1  # Time steps in seconds
        self.v = 0  # Initial velocity in pixel/second
        self.y = self.h0  # Initial position in pixels
        self.e = 0.8  # Coefficients of restitution      
        
        # Set up the simulation objects
        self.mass_size = self.m * 2  # Diameter of mass in pixels
        self.mass_pos = (self.screen_width // 2 - self.mass_size // 2, self.screen_height - self.y - self.mass_size // 2)
        self.ground_height = 100 # Height of the ground in pixels
        self.ground_pos = (0, self.screen_height - self.ground_height)
        self.mass_color = (100,100,255)
        self.ground_color = (125, 125, 30)

        
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False  
                if event.key == pygame.K_BACKSPACE:
                    self.running = False  
    
        
    def run(self):
        """Main loop"""
        while self.running:
            self.clock.tick(self.FPS)
            self.screen.fill(self.black)
            
            # Handle events
            self.handle_events()
            
            # calculate the force due to gravity
            F = self.m * self.g
            # calculate acceleration
            a = F / self.m
            # Update velocity
            self.v -= a * self.dt
            # Update position 
            self.y += self.v * self.dt
            self.mass_pos = (self.screen_width // 2 - self.mass_size // 2, self.screen_height - self.y - self.mass_size // 2 - self.ground_height)  
            # Check for collision with ground
            if self.y <= 0:
                # Update position and velocity based on coefficient of restitution
                self.v = -self.e * self.v
                self.y = -self.e * -self.y
                
            # Render simulation
            
            # draw the ground
            pygame.draw.rect(self.screen, self.ground_color, (self.ground_pos[0], self.ground_pos[1], self.screen_width, self.ground_height))
            
            # draw the mass
            pygame.draw.circle(self.screen, self.mass_color, self.mass_pos, self.mass_size//2)
            
            pygame.display.update()
            