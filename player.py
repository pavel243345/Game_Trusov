import pygame as pg

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.bird_image = pg.image.load('sources/birds.png')
        self.x = 250
        self.y = 250
        


    def draw(self): 
        self.scale = pg.transform.scale(self.bird_image,(self.bird_image.get_width() //3,
                         self.bird_image.get_height() //3))
        self.scale_rect = self.scale.get_rect(center=(self.x, self.y ))
        self.screen.blit(self.scale, self.scale_rect)    


    def move(self, keys): 
        if keys[pg.K_SPACE]: 
            self.y -= 10


    def update(self): 
        pass 