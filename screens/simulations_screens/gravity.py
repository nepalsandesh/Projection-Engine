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
        self.pause = False

        self.h0 = 500 # Initial heights in pixel
        self.m = 5 # Mass in kilograms
        self.g = 9.8 # Acceleration due to gravity in m/s^2
        self.dt = 0.1  # Time steps in seconds
        self.v = 0  # Initial velocity in pixel/second
        self.y = self.h0  # Initial position in pixels
        self.e = 0.5  # Coefficients of restitution      
        
        # Set up the simulation objects
        # self.mass_size = self.m * 2  # Diameter of mass in pixels
        self.mass_pos = (self.width // 2 , self.height - self.y )
        self.ground_height = 80 # Height of the ground in pixels
        self.ground_pos = (0, self.height - self.ground_height)
        self.mass_color = (100,100,255)
        self.ground_color = (10, 75, 10)
        self.radius = 10
        
        # UI 
        self.UIpanel = Panel(position=(self.width-420,20), w=400, h=280, color=(35,35,55))
        
        self.initial_height_index = TextUI("Initial Height : ", (self.UIpanel.position[0]+ 20, self.UIpanel.position[1]+20), (225, 255, 255))
        self.mass_index = TextUI("Mass : ", (self.UIpanel.position[0]+ 20, self.UIpanel.position[1]+50), (225, 255, 255))
        self.gravity_index = TextUI("Gravity : ", (self.UIpanel.position[0]+ 20, self.UIpanel.position[1]+80), (225, 255, 255))
        self.initial_velocity_index = TextUI("Initial Velocity : ", (self.UIpanel.position[0]+ 20, self.UIpanel.position[1]+110), (225, 255, 255))
        self.restitution_coef_index = TextUI("Restitution Coefficient : ", (self.UIpanel.position[0]+ 20, self.UIpanel.position[1]+140), (225, 255, 255))
        self.radius_index = TextUI("Body Radius : ", (self.UIpanel.position[0]+ 20, self.UIpanel.position[1]+170), (225, 255, 255))
        
        self.RunButton = Button(self.UIpanel.position[0] + 162, self.UIpanel.position[1] + 210, 75, 50, "RUN")
        self.RunButton.hover_color = (50, 50, 95)
        
        self.initialHeightPanel = Panel((self.UIpanel.position[0] + 300, self.initial_height_index.position[1]), 75, 25, (155,155,255))
        self.massPanel = Panel((self.UIpanel.position[0] + 300, self.mass_index.position[1]), 75, 25, (155,155,255))
        self.gravityPanel = Panel((self.UIpanel.position[0] + 300, self.gravity_index.position[1]), 75, 25, (155,155,255))
        self.initialVelocityPanel = Panel((self.UIpanel.position[0] + 300, self.initial_velocity_index.position[1]), 75, 25, (155,155,255))
        self.restitutionPanel = Panel((self.UIpanel.position[0] + 300, self.restitution_coef_index.position[1]), 75, 25, (155,155,255))
        self.radiusPanel = Panel((self.UIpanel.position[0] + 300, self.radius_index.position[1]), 75, 25, (155,155,255))
        
        self.h0Temp = str(self.h0)
        self.mTemp = str(self.m)
        self.gTemp = str(self.g)
        self.dtTemp = str(self.dt)
        self.v0Temp = str(self.v)
        self.eTemp = str(self.e)
        self.radiusTemp = str(self.radius)
        
        # instances of displaying values whic can be modified by text input
        self.initialHeightUI = TextUI(self.h0Temp, (self.initialHeightPanel.position[0] + 10, self.initialHeightPanel.position[1]+5), (255,255,255))
        self.massUI = TextUI(self.mTemp, (self.massPanel.position[0] + 10, self.massPanel.position[1]+5), (255,255,255))
        self.gravityUI = TextUI(self.gTemp, (self.gravityPanel.position[0] + 10, self.gravityPanel.position[1]+5), (255,255,255))
        self.initialVelocityUI = TextUI(self.v0Temp, (self.initialVelocityPanel.position[0] + 10, self.initialVelocityPanel.position[1]+5), (255,255,255))
        self.restitutionUI = TextUI(self.eTemp, (self.restitutionPanel.position[0] + 10, self.restitutionPanel.position[1]+5), (255,255,255))
        self.radiusUI = TextUI(self.radiusTemp, (self.radiusPanel.position[0] + 10, self.radiusPanel.position[1]+5), (255,255,255))

        
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False 
                
                if event.key == pygame.K_SPACE:
                    self.pause = True if self.pause==False else False 
                    
                if self.initialHeightPanel.get_hover_status():
                    if event.key == pygame.K_BACKSPACE:
                        self.h0Temp = self.h0Temp[0:-1]
                    else:
                        self.h0Temp += event.unicode

                if self.massPanel.get_hover_status():
                    if event.key == pygame.K_BACKSPACE:
                        self.mTemp = self.mTemp[0:-1]
                    else:
                        self.mTemp += event.unicode
                        
                if self.gravityPanel.get_hover_status():
                    if event.key == pygame.K_BACKSPACE:
                        self.gTemp = self.gTemp[0:-1]
                    else:
                        self.gTemp += event.unicode
                        
                if self.initialVelocityPanel.get_hover_status():
                    if event.key == pygame.K_BACKSPACE:
                        self.v0Temp = self.v0Temp[0:-1]
                    else:
                        self.v0Temp += event.unicode
                        
                if self.restitutionPanel.get_hover_status():
                    if event.key == pygame.K_BACKSPACE:
                        self.eTemp = self.eTemp[0:-1]
                    else:
                        self.eTemp += event.unicode
                        
                if self.radiusPanel.get_hover_status():
                    if event.key == pygame.K_BACKSPACE:
                        self.radiusTemp = self.radiusTemp[0:-1]
                    else:
                        self.radiusTemp += event.unicode
                    
    def draw_ui(self):
        # UI Panel
        self.UIpanel.render(self.screen)
        
        # render text_indexes
        self.initial_height_index.render(self.screen, '')
        self.mass_index.render(self.screen, '')
        self.gravity_index.render(self.screen, '')
        self.initial_velocity_index.render(self.screen, '')
        self.restitution_coef_index.render(self.screen, '')
        self.radius_index.render(self.screen, '')
                    
        self.RunButton.render(self.screen)
        
        # render values panels
        self.initialHeightPanel.render(self.screen)
        self.massPanel.render(self.screen)
        self.gravityPanel.render(self.screen)
        self.initialVelocityPanel.render(self.screen)
        self.restitutionPanel.render(self.screen)
        self.radiusPanel.render(self.screen)
           
    
    def update_ui(self):
        # get hover status of values panel
        self.initialHeightPanel.get_hover_status()
        self.massPanel.get_hover_status()
        self.gravityPanel.get_hover_status()
        self.initialVelocityPanel.get_hover_status()
        self.restitutionPanel.get_hover_status()
        self.radiusPanel.get_hover_status()
        
        # rendering parameter values on the corresponding panel
        self.initialHeightUI.render(self.screen)
        self.massUI.render(self.screen)
        self.gravityUI.render(self.screen)
        self.initialVelocityUI.render(self.screen)
        self.restitutionUI.render(self.screen)
        self.radiusUI.render(self.screen)
        
        # Update Temp text on keypress
        self.initialHeightUI.text = str(self.h0Temp)
        self.massUI.text = str(self.mTemp)
        self.gravityUI.text = str(self.gTemp)
        self.initialVelocityUI.text = str(self.v0Temp)
        self.restitutionUI.text = str(self.eTemp)
        self.radiusUI.text = str(self.radiusTemp)
    
        
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
            
            if self.pause == False:
                # Update velocity
                self.v -= a * self.dt   # substracted because of y-axis flip in window system
                # Update position 
                self.y += self.v * self.dt
                self.mass_pos = (self.width // 2, self.height - self.y - self.ground_height - self.radius)  
                # Check for collision with ground
                if self.y <= 0:
                    # Update position and velocity based on coefficient of restitution
                    self.v = -self.e * self.v
                    self.y = -self.e * -self.y
                Time += self.dt
                
            # Render simulation
            
            # draw the ground
            pygame.draw.rect(self.screen, self.ground_color, (self.ground_pos[0], self.ground_pos[1], self.width, self.ground_height))
            # draw the mass
            pygame.draw.circle(self.screen, self.mass_color, self.mass_pos, self.radius)
            
            self.draw_ui()
            self.update_ui()
            
            # Update values on run
            if self.RunButton.render(self.screen):
                self.h0 = float(self.h0Temp)
                self.m = float(self.mTemp)
                self.g = float(self.gTemp)
                self.v = float(self.v0Temp)
                self.v = -self.v
                self.y = float(self.h0)
                self.e = float(self.eTemp)
                self.radius = float(self.radiusTemp)
                Time = 0
                

            TextUI("Height : " + (str(np.round(self.y, 2))), (25, 45), (160,160,200)).render(self.screen)
            TextUI("Velocity : " + str(np.round(-self.v, 1)), (25, 70), (160,160,200)).render(self.screen)
            TextUI("Time : " + str(np.round(Time, 2)), (25, 95), (160,160,200)).render(self.screen)
            TextUI("FPS : " + str(np.round(self.clock.get_fps(), 2)), (25, 120), (160,160,200)).render(self.screen)
            TextUI("Press 'space' to pause", (25, 145), (200,120,200)).render(self.screen)
            
        
            pygame.display.update()
            