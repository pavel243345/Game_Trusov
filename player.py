import pygame as pg

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.bird_image = pg.image.load('sources/birds.png')
        self.x = 250
        self.y = 250
        self.a = 1
        self.speed = 0
        


    def draw(self): 
        self.scale = pg.transform.scale(self.bird_image,(self.bird_image.get_width() //3,
                         self.bird_image.get_height() //3))
        self.scale_rect = self.scale.get_rect(center=(self.x, self.y ))
        self.screen.blit(self.scale, self.scale_rect)    


    def move(self, keys): 
        self.speed += self.a
        self.y += self.speed
        if keys[pg.K_SPACE]:
            self.speed = -20


    def update(self): 
        pass 