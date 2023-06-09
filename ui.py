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
                self.color = (175,25, 175)
                action = True   
        else:
            self.color = self.initial_color
        return action
    
    def Draw(self, screen):
        action = self.Update()
        pygame.draw.rect(screen, self.color, self.rect)
        RenderText(screen, self.text, self.font, self.text_color, self.rect.x + self.w//2, self.rect.y + self.h//2)
        return action
    
    def SetColor(self, new_color):
        self.color = new_color
        self.initial_color = new_color
        
        

class Panel:
    """Every Interaction Interface would be on top of panel layer"""
    
    def __init__(self, position=(1920-365, 20), w = 345, h = 500, color=(8,3,12), alpha=128):
        self.position = position
        self.w = w
        self.h = h
        self.color = color
        self.alpha = alpha
        self.rect = pygame.Rect(self.position[0], self.position[1], self.w, self.h)
        
    def render(self, screen):
        s = pygame.Surface((self.w, self.h))
        s.set_alpha(self.alpha)
        s.fill(self.color)
        screen.blit(s, self.position)
        
    def get_hover_status(self):
        m_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(m_pos):
            self.color = (155,155,155)
            return True
        else:
            self.color = (55,55,155)
            return False        