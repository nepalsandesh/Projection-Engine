from constants import *
import pygame


class Chaos:
    """Chaos Object class"""
    def __init__(self, screen, clock, FPS=60):
        self.screen = screen
        self.clock = clock
        self.FPS =  FPS
        self.running = True
        