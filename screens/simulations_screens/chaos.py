import pygame
from constants import *

class Chaos:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.fps = 60
        self.running = True

        self.rate = 0.0
        self.increment_rate = 4/WIDTH
        self.generation_size = 0.5

        self.n_steps = 1000
        self.radius = 1

        self.hue = 160
        self.hue_increment = 0

    
    def ClearScreen(self):
        self.screen.fill(BLACK)
    
    def HandleEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def Run(self):
        self.ClearScreen()

        while self.running:
            self.clock.tick(self.fps)
            self.HandleEvent()

            self.generation_size = 0.05
            self.increment_rate = 4/WIDTH
            self.hue_increment = 200/WIDTH

            for i in range(self.n_steps):
                self.generation_size = self.rate * self.generation_size * (1 - self.generation_size)
                x = (self.rate / MAX_RATE) * (WIDTH * 2.3)
                y = (self.generation_size * HEIGHT) 

                # pygame.draw.circle(self.screen, WHITE, (x, HEIGHT - y), 1)
                # c = WHITE
                c = pygame.Color(0, 0, 0)
                c.hsva = (self.hue%360, 100, 100, 100)
                surface = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA, 32)
                pygame.draw.circle(surface, (c[0], c[1], c[2], 5), (self.radius, self.radius), self.radius)
                self.screen.blit(surface, ( x - self.radius, (HEIGHT - y) - self.radius))


            self.rate += self.increment_rate
            self.hue += self.hue_increment
            if self.rate < MAX_RATE:
                pygame.display.update()
        
        # Reset
        self.generation_size = 0.05
        self.rate = 0.0
        self.hue = 0
        self.running = True
