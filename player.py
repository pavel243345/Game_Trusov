import pygame as pg

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x = 100
        self.y = 100

    def draw(self):
        pg.draw.circle(self.screen, 'black', (self.x, self.y), 25)

    def move(self, keys):
        if keys[pg.K_SPACE]:
            self.y -= 10
       



    def update(self):
        pass