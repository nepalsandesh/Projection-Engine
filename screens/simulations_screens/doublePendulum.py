import math
import numpy as np
import pygame
from .parameters import mass1Index, mass2Index, length1Index, length2Index, \
    gravityIndex
from .ui import Panel, Button, TextUI

        

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
        self.BACKGROUND = (0, 0, 0)
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
              
        self.ui_panel = Panel(position=(1920-365+50, 20), w=300, h=300)
        self.mass1Panel = Panel((self.ui_panel.position[0] + 175, self.ui_panel.position[1] + 40), 90, 30, (255,255,255), 150)
        self.mass2Panel = Panel((self.ui_panel.position[0] + 175, self.ui_panel.position[1] + 80), 90, 30, (255,255,255), 150)
        self.length1Panel = Panel((self.ui_panel.position[0] + 175, self.ui_panel.position[1] + 120), 90, 30, (255,255,255), 150)
        self.length2Panel = Panel((self.ui_panel.position[0] + 175, self.ui_panel.position[1] + 160), 90, 30, (255,255,255), 150)
        self.GravityPanel = Panel((self.ui_panel.position[0] + 175, self.ui_panel.position[1] + 200), 90, 30, (255,255,255), 150)
               
        
        self.RunButton = Button(self.ui_panel.position[0] + 120, self.ui_panel.position[1] + 240, 80, 50, "RUN")
        
        self.mass1Temp = str(self.mass1)
        self.mass2Temp = str(self.mass2)
        self.length1Temp = str(self.length1)
        self.length2Temp = str(self.length2)
        self.GravityTemp = str(self.Gravity)
        
        self.mass1UI = TextUI(self.mass1Temp, (self.mass1Panel.position[0]+10, self.mass1Panel.position[1]+5), (255,255,255))
        self.mass2UI = TextUI(self.mass2Temp, (self.mass2Panel.position[0]+10, self.mass2Panel.position[1]+5), (255,255,255))
        self.length1UI = TextUI(self.length1Temp, (self.length1Panel.position[0]+10, self.length1Panel.position[1]+5), (255,255,255))
        self.length2UI = TextUI(self.length2Temp, (self.length2Panel.position[0]+10, self.length2Panel.position[1]+5), (255,255,255))
        self.GravityUI = TextUI(self.GravityTemp, (self.GravityPanel.position[0]+10, self.GravityPanel.position[1]+5), (255,255,255))
        
        
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
        mass1Index.render(self.screen, "")  #str(self.mass1Temp)
        mass2Index.render(self.screen, "")  #str(self.mass2Temp)
        length1Index.render(self.screen, "")  #str(self.length1Temp)
        length2Index.render(self.screen, "")  #str(self.length2Temp)
        gravityIndex.render(self.screen, "") #str(self.GravityTemp)
        
        
        
        # theta1.render(self.screen, "")
        # theta1_value.render(self.screen, str(np.round(self.angle1 * 180/math.pi)))
        # theta2.render(self.screen, "")
        # theta2_value.render(self.screen, str(np.round((self.angle2 * 180/math.pi)%360)))
        
        # values panel
        self.mass1Panel.render(self.screen)
        self.mass2Panel.render(self.screen)
        self.length1Panel.render(self.screen)
        self.length2Panel.render(self.screen)
        self.GravityPanel.render(self.screen)
        
        # Run Button
        # self.RunButton.render(self.screen)
        
        # check values hover
        self.mass1Panel.get_hover_status()
        self.mass2Panel.get_hover_status()
        self.length1Panel.get_hover_status()
        self.length2Panel.get_hover_status()
        self.GravityPanel.get_hover_status()
        
        self.mass1UI.render(self.screen, "")
        self.mass2UI.render(self.screen, "")
        self.length1UI.render(self.screen, "")
        self.length2UI.render(self.screen, "")
        self.GravityUI.render(self.screen, "")
        
        self.mass1UI.text = str(self.mass1Temp)
        self.mass2UI.text = str(self.mass2Temp)
        self.length1UI.text = str(self.length1Temp)
        self.length2UI.text = str(self.length2Temp)
        self.GravityUI.text = str(self.GravityTemp)
        
           
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
                        
                    if self.mass1Panel.get_hover_status():
                        if event.key == pygame.K_BACKSPACE:
                            self.mass1Temp = self.mass1Temp[0:-1]
                        else:
                            self.mass1Temp += event.unicode
                            
                    if self.mass2Panel.get_hover_status():
                        if event.key == pygame.K_BACKSPACE:
                            self.mass2Temp = self.mass2Temp[0:-1]
                        else:
                            self.mass2Temp += event.unicode
                            
                    if self.length1Panel.get_hover_status():
                        if event.key == pygame.K_BACKSPACE:
                            self.length1Temp = self.length1Temp[0:-1]
                        else:
                            self.length1Temp += event.unicode
                            
                    if self.length2Panel.get_hover_status():
                        if event.key == pygame.K_BACKSPACE:
                            self.length2Temp = self.length2Temp[0:-1]
                        else:
                            self.length2Temp += event.unicode
                            
                    if self.GravityPanel.get_hover_status():
                        if event.key == pygame.K_BACKSPACE:
                            self.GravityTemp = self.GravityTemp[0:-1]
                        else:
                            self.GravityTemp += event.unicode
        
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
            
            if self.RunButton.render(self.screen):
                self.mass1 = float(self.mass1Temp)
                self.mass2 = float(self.mass2Temp)
                self.length1 = float(self.length1Temp)
                self.length2 = float(self.length2Temp)
                self.Gravity = float(self.GravityTemp) 
                
                self.angle1 = math.pi/2
                self.angle2 = math.pi/2
                self.scatter2 = []
                self.angle_velocity1 = 0
                self.angle_velocity2 = 0
                self.angle_acceleration1 = 0
                self.angle_acceleration2 = 0
                
            pygame.display.update()
        self.run = True

    
    


