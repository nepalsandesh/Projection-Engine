import numpy as np
import pygame 
import math
import colorsys
from numba import jit


@jit(nopython=True)
def FirstAcceleration(t1, t2, m1, m2, L1, L2, G, v1, v2):
    numerator1 = -G * (2 * m1 + m2) * np.sin(t1)
    numerator2 = -m2 * G * np.sin(t1 - 2 * t2)
    numerator3 = -2 * np.sin(t1-t2)
    numerator4 =  m2 * ((v2 * v2) * L2 + (v1 * v1) * L1 * np.cos(t1-t2))
    numerator = numerator1 + numerator2 + (numerator3 * numerator4)
    denominator = L1 * (2 * m1 + m2 - m2 * np.cos(2 * t1 - 2 * t2))

    return float(numerator/denominator)

@jit(nopython=True)
def SecondAcceleration(t1, t2, m1, m2, L1, L2, G, v1, v2):
    numerator1 = 2 * np.sin(t1 - t2)
    numerator2 = (v1 * v1) * L1 * (m1 + m2) + G * (m1+ m2) * np.cos(t1)
    numerator3 = (v2 * v2) * L2 * m2 * np.cos(t1-t2)

    numerator = numerator1 * (numerator2 + numerator3)
    denominator = L2 * (2 * m1 + m2 - m2 * np.cos(2 * t1 - 2 * t2))

    return float(numerator/denominator)


class Body:
    def __init__(self, mass1, mass2, length1, length2,
                 angle1, angle2, angle_velocity1, angle_velocity2, 
                 angle_acceleration1, angle_acceleration2, 
                 color=(155,155,255), Gravity=1):
        self.mass1 = mass1
        self.mass2 = mass2
        self.length1 = length1
        self.length2 = length2
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle_velocity1 = angle_velocity1
        self.angle_velocity2 = angle_velocity2
        self.angle_acceleration1 = angle_acceleration1
        self.angle_acceleration2 = angle_acceleration2
        self.Gravity = Gravity
        
        self.offset = (1920//2, 1080//3)
        self.x_offset = self.offset[0]
        self.y_offset = self.offset[1]
        
        self.color = color
        
        
    def draw_and_update(self, screen):
        self.angle_acceleration1 = FirstAcceleration(self.angle1, self.angle2, self.mass1, self.mass2, self.length1, self.length2, self.Gravity, self.angle_velocity1, self.angle_velocity2)
        self.angle_acceleration2 = SecondAcceleration(self.angle1, self.angle2, self.mass1, self.mass2, self.length1, self.length2, self.Gravity, self.angle_velocity1, self.angle_velocity2)
        
        x1 = float(self.length1 * np.sin(self.angle1) + self.x_offset)
        y1 = float(self.length1 * np.cos(self.angle1) + self.y_offset)
        
        x2 = float(x1 + self.length2 * np.sin(self.angle2))
        y2 = float(y1 + self.length2 * np.cos(self.angle2))
        
        # print(x1, y1, x2, y2)
        
        # the angle varies with respect to velocity and velocity with respect to the acceleration 
        self.angle_velocity1 += self.angle_acceleration1
        self.angle_velocity2 += self.angle_acceleration2
        self.angle1 += self.angle_velocity1
        self.angle2 += self.angle_velocity2
        
        # scatter1.append((x1, y1))
        # scatter2.append((x2, y2))
        
        # scatter_point1 = Points(screen, SCATTERLINE1, scatter1)
        # scatter_point1.draw()
        # scatter_point2 = Points(screen, SCATTERLINE2, scatter2)
        # scatter_point2.draw()
            
        pygame.draw.line(screen, self.color, self.offset, (int(x1), int(y1)), 5)
        pygame.draw.line(screen, self.color, (x1, y1), (x2, y2),5)
        pygame.draw.circle(screen, self.color, (x1, y1), 10)
        pygame.draw.circle(screen, self.color, (x2, y2), 10)
        

        
        
        
# ------------------------------------------------------




bodies = [Body(
    mass1=40,
    mass2=40+i/1000,
    length1=250,
    length2=250,
    angle1=math.pi/1.9,
    angle2= math.pi/1.9,
    angle_velocity1=0,
    angle_velocity2=0,
    angle_acceleration2=0,
    angle_acceleration1=0,
    color=None,
    Gravity=0.5,
) for i in range(1000)]


max_mass = max(body.mass2 for body in bodies)
min_mass = min(body.mass2 for body in bodies)


# Define a function to map a value to a color
def map_value_to_rainbow_color(value, min_value, max_value):
    normalized_value = (value - min_value) / (max_value - min_value)
    hue = normalized_value * 240  # 240 is the range of hues for the rainbow spectrum
    saturation = 1.0  # You can adjust the saturation and lightness values
    lightness = 0.5  # to achieve the desired appearance
    
    rgb_color = colorsys.hls_to_rgb(hue / 360, lightness, saturation)
    red = int(rgb_color[0] * 155)
    green = int(rgb_color[1] * 155)
    blue = int(rgb_color[2] * 155)
    
    return red, green, blue

# Assign colors to bodies based on their properties
for body in bodies:
    red, green, blue = map_value_to_rainbow_color(body.mass2, min_mass, max_mass)
    body.color = (red, green, blue)


def render(screen,clock, FPS):
    run=True
    while run:
        
        clock.tick(FPS) 
        screen.fill((0, 0, 0))
        print(clock.get_fps())
        # [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_r:
                    restart = True
                    
        # drawing and updating stuffs
        for body in bodies:
            body.draw_and_update(screen=screen)                
        pygame.display.flip()

        
        
