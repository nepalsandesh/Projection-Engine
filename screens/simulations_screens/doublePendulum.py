import math
import numpy as np
import pygame
from .parameters import mass1, mass2, theta1, theta2, theta1_value,  theta2_value, length1, length2
from .ui import Panel

        

class DoublePendulum:
    """Double Pendulum class"""
    def __init__(self, screen, RESOLUTION, clock, FPS):
        pygame.init()
        self.width = RESOLUTION[0]
        self.height = RESOLUTION[1]
        self.resolution = RESOLUTION
        self.screen = screen
        self.clock = clock
        self.FPS = FPS


        # initial Physics variables 
        self.mass1 = 40
        self.mass2 = 40
        self.length1 = 200
        self.length2 = 200

        self.angle1 = math.pi/2
        self.angle2 = math.pi/2
        self.angle_velocity1 = 0
        self.angle_velocity2 = 0
        self.angle_acceleration1 = 0
        self.angle_acceleration2 = 0
        self.Gravity = 0.5
        self.scatter1 = []
        self.scatter2 = []

        self.restart = False
        self.LIST_LIMIT = 100

        # color variables
        self.BACKGROUND = (20, 20, 20)
        self.SCATTERLINE1 = (55, 55, 55)
        self.SCATTERLINE2 = (55, 55, 0)
        self.MAINPOINT = (0, 255, 0)
        self.SMALLPOINT = (0, 255, 255)
        self.PENDULUMARM = (245, 140, 245)
        self.ARMSTROKE = 10

        self.starting_point = (self.width//2, self.height//3)

        self.x_offset = self.starting_point[0]
        self.y_offset = self.starting_point[1]
        self.run = True
              
        self.ui_panel = Panel()
        
        
    def FirstAcceleration(self,t1, t2, m1, m2, L1, L2, G, v1, v2):
        numerator1 = -G * (2 * m1 + m2) * math.sin(t1)
        numerator2 = -m2 * G * math.sin(t1 - 2 * t2)
        numerator3 = -2 * math.sin(t1-t2)
        numerator4 =  m2 * ((v2 * v2) * L2 + (v1 * v1) * L1 * math.cos(t1-t2))
        numerator = numerator1 + numerator2 + (numerator3 * numerator4)
        denominator = L1 * (2 * m1 + m2 - m2 * math.cos(2 * t1 - 2 * t2))

        return float(numerator/denominator)
    
    

    def SecondAcceleration(self,t1, t2, m1, m2, L1, L2, G, v1, v2):
        numerator1 = 2 * math.sin(t1 - t2)
        numerator2 = (v1 * v1) * L1 * (m1 + m2) + G * (m1+ m2) * math.cos(t1)
        numerator3 = (v2 * v2) * L2 * m2 * math.cos(t1-t2)

        numerator = numerator1 * (numerator2 + numerator3)
        denominator = L2 * (2 * m1 + m2 - m2 * math.cos(2 * t1 - 2 * t2))

        return float(numerator/denominator)
    
    
    
    def draw_curve(self, coordinates, color):
        if len(coordinates) > 2:
            pygame.draw.lines(self.screen, color, False, coordinates, 2)
            
    def draw_ui(self):
        self.ui_panel.render(self.screen)
        mass1.render(self.screen, str(self.mass1))
        mass2.render(self.screen, str(self.mass2))
        theta1.render(self.screen, "")
        theta1_value.render(self.screen, str(np.round(self.angle1 * 180/math.pi)))
        theta2.render(self.screen, "")
        theta2_value.render(self.screen, str(np.round(self.angle2 * 180/math.pi)))
        length1.render(self.screen, str(self.length1))
            
    def render(self):
        while self.run:
    
            self.clock.tick(self.FPS) 
            self.screen.fill(self.BACKGROUND)       
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:           
                        self.run = False
                    if event.key == pygame.K_r:
                        restart = True
                    if event.key == pygame.K_BACKSPACE:
                        self.run = False  
        
            if self.restart == True:
                self.angle1 = math.pi/2
                self.angle2 = math.pi/2
                self.angle_velocity1 = 0
                self.angle_velocity2 = 0
                self.angle_acceleration1 = 0
                self.angle_acceleration2 = 0
                self.Gravity = 9.8
                self.scatter1 = []
                self.scatter2 = []
                self.restart = False
            
            
            # calculate the acceleration
            self.angle_acceleration1 = self.FirstAcceleration(self.angle1, self.angle2, self.mass1, self.mass2, self.length1, self.length2, self.Gravity, self.angle_velocity1, self.angle_velocity2)
            self.angle_acceleration2 = self.SecondAcceleration(self.angle1, self.angle2, self.mass1, self.mass2, self.length1, self.length2, self.Gravity, self.angle_velocity1, self.angle_velocity2)
        
            x1 = (self.length1 * math.sin(self.angle1) + self.x_offset)
            y1 = float(self.length1 * math.cos(self.angle1) + self.y_offset)
        
            x2 = float(x1 + self.length2 * math.sin(self.angle2))
            y2 = float(y1 + self.length2 * math.cos(self.angle2))
        
            # the angle varies with respect to velocity and velocity with respect to the acceleration 
            self.angle_velocity1 += self.angle_acceleration1
            self.angle_velocity2 += self.angle_acceleration2
            self.angle1 += self.angle_velocity1
            self.angle2 += self.angle_velocity2
            
            self.scatter1.append((x1, y1))
            self.scatter2.append((x2, y2))
            
            self.draw_curve(self.scatter2, (55,55,100))


            

            pygame.draw.line(self.screen, self.PENDULUMARM, self.starting_point, (int(x1), int(y1)), 6)
            pygame.draw.line(self.screen, self.PENDULUMARM, (x1, y1), (x2, y2),6)
            pygame.draw.circle(self.screen, self.MAINPOINT, (x1, y1), 15)
            pygame.draw.circle(self.screen, self.MAINPOINT, (x2, y2), 15)
            
            self.draw_ui()
            
                
            pygame.display.update()
        self.run = True

    
    


