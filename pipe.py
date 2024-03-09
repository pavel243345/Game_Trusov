import pygame as pg

class Pipe:
    def __init__(self, screen):
        self.screen = screen
        self.x = 100
        self.y = 250

    def draw(self):
        pg.draw.rect(self.screen)

    def move(self):
        self.x -= 10


    def update(self):
        pass



