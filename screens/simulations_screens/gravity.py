import pygame 
from .ui import Panel, Button, TextUI
import numpy as np

class Gravity:
    """Gravity Simulator Class, renders with run() function"""
    def __init__(self, screen, resolution, clock, FPS=60):         
        # Colors
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.blue = (0,0, 255)

        self.resolution = self.width, self.height = resolution
        self.screen = screen
        pygame.display.set_caption('Gravity Simulator')
        self.clock = clock
        self.FPS = 60
        self.running = True

        self.h0 = 1000 # Initial heights in pixel
        self.m = 5 # Mass in kilograms
        self.g = 9.8 # Acceleration due to gravity in m/s^2
        self.dt = 0.1  # Time steps in seconds
        self.v = 0  # Initial velocity in pixel/second
        self.y = self.h0  # Initial position in pixels
        self.e = 0.5  # Coefficients of restitution      
        
        # Set up the simulation objects
        self.mass_size = self.m * 2  # Diameter of mass in pixels
        self.mass_pos = (self.width // 2 - self.mass_size // 2, self.height - self.y - self.mass_size // 2)
        self.ground_height = 100 # Height of the ground in pixels
        self.ground_pos = (0, self.height - self.ground_height)
        self.mass_color = (100,100,255)
        self.ground_color = (125, 125, 30)
        
        # UI 
        self.UIpanel = Panel(position=(self.width-420,20), w=400, h=300, color=(35,35,55))
        
        self.initial_height_index = TextUI("Initial Height : ", (self.UIpanel.position[0]+ 20, self.UIpanel.position[1]+20), (225, 255, 255))
        self.mass_index = TextUI("Mass : ", (self.UIpanel.position[0]+ 20, self.UIpanel.position[1]+50), (225, 255, 255))
        self.gravity_index = TextUI("Gravity : ", (self.UIpanel.position[0]+ 20, self.UIpanel.position[1]+80), (225, 255, 255))
        self.time_delta_index = TextUI("Time Delta : ", (self.UIpanel.position[0]+ 20, self.UIpanel.position[1]+110), (225, 255, 255))
        self.initial_velocity_index = TextUI("Initial Velocity : ", (self.UIpanel.position[0]+ 20, self.UIpanel.position[1]+140), (225, 255, 255))
        self.restitution_coef_index = TextUI("Restitution Coefficient : ", (self.UIpanel.position[0]+ 20, self.UIpanel.position[1]+170), (225, 255, 255))
        self.radius_index = TextUI("Body Radius : ", (self.UIpanel.position[0]+ 20, self.UIpanel.position[1]+200), (225, 255, 255))
        
        self.RunButton = Button(self.UIpanel.position[0] + 20, self.UIpanel.position[1] + 230, 75, 50, "RUN")
        
        self.initialHeightPanel = Panel((self.UIpanel.position[0] + 300, self.initial_height_index.position[1]), 50, 25, (155,155,255))
        self.massPanel = Panel((self.UIpanel.position[0] + 300, self.mass_index.position[1]), 50, 25, (155,155,255))
        self.gravityPanel = Panel((self.UIpanel.position[0] + 300, self.gravity_index.position[1]), 50, 25, (155,155,255))
        self.timeDeltaPanel = Panel((self.UIpanel.position[0] + 300, self.time_delta_index.position[1]), 50, 25, (155,155,255))
        self.initialVelocityPanel = Panel((self.UIpanel.position[0] + 300, self.initial_velocity_index.position[1]), 50, 25, (155,155,255))
        self.restitutionPanel = Panel((self.UIpanel.position[0] + 300, self.restitution_coef_index.position[1]), 50, 25, (155,155,255))
        self.radiusPanel = Panel((self.UIpanel.position[0] + 300, self.radius_index.position[1]), 50, 25, (155,155,255))
        
        self.h0Temp = str(self.h0)
        self.mTemp = str(self.m)
        self.gTemp = str(self.g)
        self.dtTemp = str(self.dt)
        self.v0Temp = str(self.v)
        self.eTemp = str(self.e)
        self.radiusTemp = str(self.mTemp)
        
        # instances of displaying values whic can be modified by text input
        self.initialHeightUI = TextUI(self.h0Temp, (self.initialHeightPanel.position[0] + 10, self.initialHeightPanel.position[1]), (255,255,255))
        self.massUI = TextUI(self.mTemp, (self.massPanel.position[0] + 10, self.massPanel.position[1]), (255,255,255))
        self.gravityUI = TextUI(self.gTemp, (self.gravityPanel.position[0] + 10, self.gravityPanel.position[1]), (255,255,255))
        self.timeDeltaUI = TextUI(self.dtTemp, (self.timeDeltaPanel.position[0] + 10, self.timeDeltaPanel.position[1]), (255,255,255))
        self.initialVelocityUI = TextUI(self.v0Temp, (self.initialVelocityPanel.position[0] + 10, self.initialVelocityPanel.position[1]), (255,255,255))
        self.restitutionUI = TextUI(self.eTemp, (self.restitutionPanel.position[0] + 10, self.restitutionPanel.position[1]), (255,255,255))
        self.radiusUI = TextUI(self.radiusTemp, (self.radiusPanel.position[0] + 10, self.radiusPanel.position[1]), (255,255,255))

        
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False  
                if event.key == pygame.K_BACKSPACE:
                    self.running = False  
                    
    def draw_ui(self):
        # UI Panel
        self.UIpanel.render(self.screen)
        
        # render text_indexes
        self.initial_height_index.render(self.screen, '')
        self.mass_index.render(self.screen, '')
        self.gravity_index.render(self.screen, '')
        self.time_delta_index.render(self.screen, '')
        self.initial_velocity_index.render(self.screen, '')
        self.restitution_coef_index.render(self.screen, '')
        self.radius_index.render(self.screen, '')
                    
        self.RunButton.render(self.screen)
        
        # render values panel
        self.initialHeightPanel.render(self.screen)
        self.massPanel.render(self.screen)
        self.gravityPanel.render(self.screen)
        self.timeDeltaPanel.render(self.screen)
        self.initialVelocityPanel.render(self.screen)
        self.restitutionPanel.render(self.screen)
        self.radiusPanel.render(self.screen)
        
        # get hover status of values panel
        self.initialHeightPanel.get_hover_status()
        self.massPanel.get_hover_status()
        self.gravityPanel.get_hover_status()
        self.timeDeltaPanel.get_hover_status()
        self.initialVelocityPanel.get_hover_status()
        self.restitutionPanel.get_hover_status()
        self.radiusPanel.get_hover_status()
        
        # rendering parameter values on the corresponding panel
        self.initialHeightUI.render(self.screen)
        self.massUI.render(self.screen)
        self.gravityUI.render(self.screen)
        self.timeDeltaUI.render(self.screen)
        self.initialVelocityUI.render(self.screen)
        self.restitutionUI.render(self.screen)
        self.radiusUI.render(self.screen)
    
    
    def update_ui(self):
        pass
    
        
    def run(self):
        """Main loop"""
        Time = 0
        while self.running:
            self.clock.tick()
            self.screen.fill(self.black)
            self.dt = 1/self.clock.get_fps()
            
            # Handle events
            self.handle_events()
            
            # calculate the force due to gravity
            F = self.m * self.g
            # calculate acceleration
            a = F / self.m
            # Update velocity
            self.v -= a * self.dt   # substracted because of y-axis flip in window system
            # Update position 
            self.y += self.v * self.dt
            self.mass_pos = (self.width // 2 - self.mass_size // 2, self.height - self.y - self.mass_size // 2 - self.ground_height)  
            # Check for collision with ground
            if self.y <= 0:
                # Update position and velocity based on coefficient of restitution
                self.v = -self.e * self.v
                self.y = -self.e * -self.y
                
            # Render simulation
            
            # draw the ground
            pygame.draw.rect(self.screen, self.ground_color, (self.ground_pos[0], self.ground_pos[1], self.width, self.ground_height))
            # draw the mass
            pygame.draw.circle(self.screen, self.mass_color, self.mass_pos, self.mass_size//2)
            
            self.draw_ui()
            self.update_ui()
            
            
            if self.RunButton.render(self.screen):
                self.h0 = float(self.h0Temp)
                self.m = float(self.mTemp)
                self.g = float(self.gTemp)
                self.dt = float(self.dtTemp)
                self.v = float(self.v0Temp)
                self.y = float(self.h0)
                self.e = float(self.eTemp)
                
            TextUI("Height : " + (str(np.round(self.y, 3))), (15, 15), (255,255,255)).render(self.screen)
            TextUI("Velocity : " + str(np.round(self.v, 3)), (15, 35), (255,255,255)).render(self.screen)
            TextUI("Time : " + str(np.round(Time, 3)), (15, 55), (255,255,255)).render(self.screen)
            TextUI("FPS : " + str(np.round(self.clock.get_fps(), 3)), (15, 75), (255,255,255)).render(self.screen)
            Time += self.dt
            
            print(self.dt)
            pygame.display.update()
            