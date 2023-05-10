import pygame


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
        
        
class TextUI:
    """A class for rendering text UI"""
    def __init__(self, text, position, fontColor, anchor="center"):
        self.text = text
        self.position = position
        self.fontColor = fontColor
        self.anchor = anchor
        self.fontSize = 20
        self.font = 'freesansbold.ttf'
        
    def render(self, screen, value=""):
        """method for rendering the text"""
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(self.text + value, True, self.fontColor)
        textRect = text.get_rect()
        textRect.left, textRect.top = self.position[0], self.position[1]
        setattr(textRect, self.anchor, self.position)
        screen.blit(text, textRect)
        
        


class Button:
    """Button Class having multiple methods"""
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.w = w
        self.h = h
        self.text = text
        self.font_size = 20      
        self.color = (25,25, 25)
        self.hover_color = (0, 50, 50)
        self.initial_color = self.color
        self.text_color = (155,155,0)
        self.anchor = "center"
        self.clicked = False

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
    
    def render(self, screen):
        """render button and returns boolean flag, ie either pressed or not"""
        action = self.Update()
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font('freesansbold.ttf', self.font_size)
        text = font.render(self.text, True, self.text_color)
        textRect = text.get_rect()
        (textRect.x, textRect.y) = self.rect.x+8, self.rect.y+5
        screen.blit(text, textRect)
        return action
