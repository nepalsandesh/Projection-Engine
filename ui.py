import pygame
from constants import *


class Button:
    """A Button UI class
    parameters: x-pos, y-pos, width, height, text
    """
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.w = w
        self.h = h 
        self.text = text
        self.font_size = 20
        
        self.is_clicked = False
        self.action = False
        
        self.color = (200, 200, 200)
        self.hover_color = (150, 150, 150)
        self.initial_color = self.color
        self.text_color = BLACK
        
        self.initializeFont()
        
    def initializeFont(self):
        self.font = pygame.font.SysFont('consolas', self.font_size)
        
    def setColor(self, new_color):
        self.color = new_color
        self.initial_color = new_color
        
    def update(self):
        action = False
        m_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(m_pos):
            self.color = self.hover_color
            if pygame.mouse.get_pressed()[0] and self.is_clicked == False:
                self.color = (255, 255, 0)
                action = True
                self.is_clicked = True
        else:
            self.color = self.initial_color
        if pygame.mouse.get_pressed()[0] == 0:
            self.is_clicked = False
        
        return action
    
    
    def RenderText(screen, message, font, text_color=WHITE, x=WIDTH//2, y=HEIGHT//2):
        img = font.render(message, True, text_color)
        rect = img.get_rect()
        rect.center = (x, y)
        screen.blit(img, rect)
    
    def draw(self, screen):
        action = self.update()
        pygame.draw.rect(screen, self.color, self.rect)
        
    
    