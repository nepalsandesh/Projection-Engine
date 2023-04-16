import pygame
from constants import *

def RenderText(screen, message, font, text_color=WHITE, x=WIDTH//2, y=HEIGHT//2):
    img = font.render(message, True, text_color)
    rect = img.get_rect()
    rect.center = (x, y)
    screen.blit(img, rect)

class Button:
    """Button Class having multiple methods"""
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.w = w
        self.h = h
        self.text = text
        self.font_size = 20

        # self.isClicked = False
        # self.action = False
        
        self.color = (200, 200, 200)
        self.hover_color = (150, 150, 150)
        self.initial_color = self.color
        self.text_color = (0,0,0)
        self.InitializeFont()
        
    def InitializeFont(self):
        self.font = pygame.font.SysFont("consolas", self.font_size)
        
    
    def Update(self):
        action = False
        m_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(m_pos):
            self.color = self.hover_color
            if pygame.mouse.get_pressed()[0]:
                print("AAAAAAAAAAA")
                self.color = (175,25, 175)
                action = True   
        else:
            self.color = self.initial_color
        return action
        # action = False
        # m_pos = pygame.mouse.get_pos()
        # # check mouseover and clicked conditions
        # if self.rect.collidepoint(m_pos):
        #     self.color = self.hover_color
        #     if pygame.mouse.get_pressed()[0] == True:
        #         self.color = (255, 255, 0)
        #         action = True
        #         self.isClicked = True
        # else:
        #     self.color = self.initial_color
        # if pygame.mouse.get_pressed()[0] == 0:
        #     self.clicked = False
        
    
    def Draw(self, screen):
        action = self.Update()
        pygame.draw.rect(screen, self.color, self.rect)
        RenderText(screen, self.text, self.font, self.text_color, self.rect.x + self.w//2, self.rect.y + self.h//2)
        return action
    
    def SetColor(self, new_color):
        self.color = new_color
        self.initial_color = new_color