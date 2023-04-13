import pygame 
import numpy as np
from numba import jit


@jit()
def Get_neighbours(x, y, rows, columns, grid_array):
    total = 0
    for n in range(-1, 2):
        for m in range(-1, 2):
            x_edge = (x+n+rows) % rows
            y_edge = (y+m+columns) % columns
            total += grid_array[x_edge][y_edge]
    total -= grid_array[x][y]
    return total


class ConwaysGameOfLife:
    """Conways Game of Life"""
    def __init__(self, screen, resolution, clock, FPS):
        self.screen = screen
        self.resolution = resolution
        self.width = resolution[0]
        self.height = resolution[1]
        self.clock = clock
        self.FPS = FPS
        
        self.scale = 10
        self.offset = 1
        self.columns = int(self.height//self.scale)
        self.rows = int(self.width//self.scale)
        self.size = (self.rows, self.columns)
        self.grid_array = np.random.randint(2, size=self.size)
        
        self.black = (0,0,0)
        self.white = (255, 255, 255)
        self.dark_blue = (10, 10, 60)
        self.on_color = (155,155,155)
        self.off_color = (0,0,0)
        
        self.pause = False
        self.running = True
        
    def Conway(self):
        for x in range(self.rows):
            for y in range(self.columns):
                x_pos = x * self.scale
                y_pos = y * self.scale
                if self.grid_array[x][y] == 1:
                    rect = pygame.Rect(x_pos, y_pos, self.scale-self.offset, self.scale-self.offset)
                    pygame.draw.rect(self.screen, self.dark_blue, rect)
                else:
                    rect = pygame.Rect(x_pos, y_pos, self.scale-self.offset, self.scale-self.offset)
                    pygame.draw.rect(self.screen, self.white, rect)
        
        next = np.ndarray(shape=(self.rows, self.columns))
        if self.pause == False:
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.grid_array[x][y]
                    neighbours = self.get_neighbours(x, y)
                    if state == 0 and neighbours == 3:
                        next[x][y] = 1
                    elif state == 1 and (neighbours < 2 or neighbours >3):
                        next[x][y] = 0
                    else:
                        next[x][y] = state
            self.grid_array = next
            
    

    def get_neighbours(self, x, y):
        return Get_neighbours(x, y, self.rows, self.columns, self.grid_array)
        
    
    def handle_mouse(self, x, y):
        _x = x//self.scale
        _y = y//self.scale
        if self.grid_array[_x][_y] != None:
            self.grid_array[_x][_y] = 1
    
    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            pygame.display.set_caption("FPS-{}".format(np.round(self.clock.get_fps())))
            self.screen.fill(self.black)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        
            self.Conway()
            
            if pygame.mouse.get_pressed()[0]:
                x_pos, y_pos = pygame.mouse.get_pos()
                self.handle_mouse(x_pos, y_pos)
            
                
            # frame_count += 1
            # filename = "captures/%04d.png" % ( frame_count ) # name with four decimals
            # pygame.image.save( screen, filename )
            
            pygame.display.flip()
        