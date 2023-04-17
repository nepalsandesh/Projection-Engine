import pygame
import numpy as np
from sympy import symbols, sin, cos, lambdify
from sympy.parsing.sympy_parser import parse_expr

x = symbols('x')

x_array = np.linspace(-50,50,500)

expr = parse_expr(str(input("Enter the expression first: ")))

f = lambdify(x, expr)


y_array = f(x_array)

points = np.array([x_array, f(x_array)]).T
print(points.shape)

print(points[:3])

points[:, 0] = (points[:, 0] * 25) +1920//2
points[:, 1] = (points[:, 1] * 25) +1080//2

print(points[:3])


width = 1920
height = 1080
resolution = (width, height)

pygame.init()
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Calculus Engine")
clock = pygame.time.Clock()
FPS = 60

white = (255, 255, 255)
black = (0, 0, 0)
dark_blue = (15, 15, 55)

while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
                
    pygame.draw.line(screen, white, (0,height//2), (1920, height//2))
    pygame.draw.line(screen, white, (width//2,0), (width//2, height))
    
    pygame.draw.lines(screen, (125,125,255), False, points)
    
    pygame.display.flip()
    
