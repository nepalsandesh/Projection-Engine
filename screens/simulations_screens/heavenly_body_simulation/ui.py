import pygame
pygame.init()

def RenderText(screen, message, font, text_color, x, y):
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
        
        self.last_button_pressed_time = 0
        self.debounce_interval = 500
        
    def InitializeFont(self):
        self.font = pygame.font.Font('freesansbold.ttf', 15)
        
    
    def Update(self):
        action = False
        m_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(m_pos):
            self.color = self.hover_color
            if pygame.mouse.get_pressed()[0]:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_button_pressed_time > self.debounce_interval:
                    self.last_button_pressed_time = current_time
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
        
        
class TextUI:
    """A class for rendering text UI"""
    def __init__(self, text, position, fontColor, anchor="center"):
        self.text = text
        self.position = position
        self.fontColor = fontColor
        self.anchor = anchor
        self.fontSize = 20
        self.font = 'freesansbold.ttf'
        
    def render(self, screen, additional_text=""):
        """method for rendering the text"""
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(self.text+additional_text, True, self.fontColor)
        # textRect = text.get_rect()
        # setattr(textRect, self.anchor, self.position)
        screen.blit(text, self.position)
        
        

class RadioButton:
    def __init__(self, x, y, w, h, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.fontsize  = 20
        self.font = pygame.font.Font('freesansbold.ttf', 15)
        self.clicked = False
        self.active = False
        self.last_button_pressed_time = 0
        self.debounce_interval = 200
        
        self.color = (200, 200, 200)
        self.hover_color = (150, 150, 150)
        self.initial_color = self.color
        self.active_color = (100, 100, 255)
        self.text_color = (0,0,0)
        
    
    def update(self):
        m_pos = pygame.mouse.get_pos()
        if self.rect.colliderect(m_pos):
            self.color = self.hover_color
            if pygame.mouse.get_pressed()[0]:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_button_pressed_time > self.debounce_interval:
                    self.last_button_pressed_time = current_time
                    self.clicked = not self.clicked
                
        
        
    def render(self, screen):
        "Renders and returns true until next click. Debounce interval is set."
        if self.active:
            color = self.active_color
        else:
            color = self.initial_color
        pygame.draw.rect(screen, color, self.rect)
        RenderText(screen, self.text, self.font, self.text_color, self.rect.x + self.w//2, self.rect.y + self.h//2)
        m_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(m_pos):
            self.color = self.hover_color
            if pygame.mouse.get_pressed()[0]:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_button_pressed_time > self.debounce_interval:
                    self.last_button_pressed_time = current_time
                    self.active = not self.active
        return self.active
        
    def is_double_clicked(self, screen):
        "Renders and returns true while clicked. Debounce interval is not set"
        if self.active:
            color = self.active_color
        else:
            color = self.initial_color
        action = False
        pygame.draw.rect(screen, color, self.rect)
        RenderText(screen, self.text, self.font, self.text_color, self.rect.x + self.w//2, self.rect.y + self.h//2)
        m_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(m_pos):
            self.color = self.hover_color
            if pygame.mouse.get_pressed()[0]:
                action = True 
                self.active = True  
            else:
                self.color = self.initial_color
                self.active = False
        return action