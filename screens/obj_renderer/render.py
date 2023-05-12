import pygame as pg
from .object_3d import Object3d, Axes
from .camera import Camera
from .projection import Projection


class SoftwareRender:
    """The main rendering class"""
    def __init__(self, screen, resolution, clock, FPS, filename):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = resolution
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH//2, self.HEIGHT//2
        self.FPS = FPS
        self.screen = screen
        self.clock = clock
        self.running = True
        self.filename = filename
        self.create_objects()
        
        
    def create_objects(self):
        self.camera = Camera(self, [-5, 5, -50])
        self.projection = Projection(self)
        self.object = self.get_object_from_file('resources/' + self.filename)

        
    def get_object_from_file(self, filename):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object3d(self,vertex, faces)
                
    def draw(self):
        self.screen.fill((0,0,0))
        self.object.draw()
        
           
    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE or event.key == pg.K_BACKSPACE:
                        self.running = False
            
            self.draw()
            self.camera.control()
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

        self.running = True

