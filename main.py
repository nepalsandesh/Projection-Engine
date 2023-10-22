import pygame 
from constants import *
from ui import Button, Panel
from screens.simulations import Simulation
from screens.math_engine import MathEngine
from screens.obj_renderer.render import SoftwareRender
from screens.obj_renderer.object_loader import run as load
import numpy as np


class StarAddon:
    def __init__(self):
        self.star_list = [
            [-1, 0, 0],           # Left point
            [-0.5, -0.866, 0],     # Upper-left point (bottom triangle)
            [0.5, -0.866, 0],      # Upper-right point (top triangle)
            [1, 0, 0],            # Right point
            [0.5, 0.866, 0],       # Lower-right point (top triangle)
            [-0.5, 0.866,0]       # Lower-left point (bottom triangle)
        ]

        self.star_list = np.array(self.star_list)
        self.star_list = np.array([self.star_list[:, 0], self.star_list[:, 1], self.star_list[:, 2]]).T
        self.tail_matrix = []

        self.scale = 0

        self.theta = np.pi/2
        self.speed = 0.004
        self.light_blue = (125, 125, 255)

    def rot_z(self):
        return np.array([
            [-np.cos(self.theta), -np.sin(self.theta), 0],
            [np.sin(self.theta), -np.cos(self.theta),  0],
            [0, 0, 1]
        ])
    
    def append(self, coordinates, screen):
        # print(self.star_list)
        self.tail_matrix.append(coordinates)
        # print(self.tail_matrix)
        if len(self.tail_matrix) > 50:
            for i in range(6):
                # print("tail array: ", self.tail_matrix[i::6])
                pygame.draw.lines(screen, (155,155,155), False, self.tail_matrix[i::6])

        # if len(self.tail_matrix) > 12:
        #     exit()

    def update(self):
        self.theta += self.speed
        if self.scale <= 1300:
            self.scale += 0.8
        else:   
            self.tail_matrix = []
            self.scale *= -1

    

    def draw(self, screen):
        # draw lines 
        seq1 = np.dot(self.star_list[0::2, :], self.rot_z())
        seq1 = np.array([seq1[:, 0]*self.scale+1920//1.5, seq1[:, 1]*self.scale+1080//2]).T
        # print("seq1 = ", seq1)
        pygame.draw.lines(screen, self.light_blue, True, seq1, 10)

        seq2 = np.dot(self.star_list[1::2, :], self.rot_z())
        seq2 = np.array([seq2[:, 0] * self.scale + 1920//1.5, seq2[:, 1]*self.scale+1080//2]).T
        # print("seq1 = ", seq2)
        pygame.draw.lines(screen, self.light_blue, True, seq2, 10)

        # draw points
        for point in self.star_list:
            point = np.dot(point, self.rot_z())
            # print(point)  
            coordinate = (point[0]*self.scale+1920//1.5, point[1]*self.scale+1080//2)
            print("coordinate: ", coordinate)
            pygame.draw.circle(screen, self.light_blue, coordinate, 10)
            self.append(coordinate,screen)
       

    
    


class Render:
    """Main Rendering class"""
    def __init__(self):
        pygame.init()
        self.WIDTH = 1920
        self.HEIGHT = 1080
        self.RESOLUTION = (self.WIDTH, self.HEIGHT)
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.running = True
        
        # panel 
        self.panel = Panel((325,100), 400, 500, (25, 25, 50), alpha=200)
        
        # BUTTONS
        self.ChaosEquationButton = Button(WIDTH//4 - 100, self.HEIGHT//10, 300, 60, "Chaos Equation")
        self.SimulationButton = Button(WIDTH//4 - 100, self.HEIGHT//10 + 100, 300, 60, "Simulations")
        self.MathEngineButton = Button(WIDTH//4 - 100, self.HEIGHT//10 + 200, 300, 60, "Math Engine")
        self.ObjRenderButton = Button(WIDTH//4 - 100, self.HEIGHT//10 + 300 , 300, 60, "Object Render")
        self.AlgVizButton = Button(WIDTH//4 - 100, self.HEIGHT//10 + 400 , 300, 60, "Algorithms Visualization")
        self.GamesButton = Button(WIDTH//4 - 100, self.HEIGHT//10 + 500 , 300, 60, "Games")
        
        
        # After Button Click
        self.Simulation = Simulation(self.screen, self.RESOLUTION, self.clock, self.FPS)
        self.MathEngine = MathEngine(self.screen, self.RESOLUTION, self.clock, self.FPS)
        # self.ObjEngine = SoftwareRender(self.screen, self.RESOLUTION, self.clock, self.FPS)

        self.AddOn = StarAddon()
        
        
        
    
    def clear_screen(self):
        self.screen.fill((0,0,0))
        
    def displayMenu(self):
        """Displays each buttons and runs the corresponding function if clicked"""

        self.panel.render(self.screen)
        
        if self.MathEngineButton.Draw(self.screen):
            self.MathEngine.run_menu()
        elif self.SimulationButton.Draw(self.screen):
            self.Simulation.run_menu()
        elif self.ObjRenderButton.Draw(self.screen):
            load(self.screen, self.RESOLUTION, self.clock, self.FPS)
            # self.ObjEngine.run()
        # elif self.AlgVizButton.Draw(self.screen):
        #     self.AlgViz.Run()
        # elif self.GamesButton.Draw(self.screen):
        #     self.Games.Run()

    def displayAddOn(self):
        self.AddOn.draw(self.screen)
        self.AddOn.update()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_BACKSPACE:
                    self.running = False  
        
    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.clear_screen()
            self.check_events()
            self.displayAddOn()
            self.displayMenu()
            print(self.clock.get_fps())
            pygame.display.update()
            # exit()
            
   
        
if __name__ == "__main__":
    app = Render()
    app.run()