import pygame as pg 


class Pup: 
    def __init__(self, screen ):
        self.screen = screen 
        self.x = 250
        self.y = 250

    def draw(self): 
        pg.draw.rect(self.screen, 'green',(self.x, self.y, 30, 100))
        

    def move(self): 
        self.x -= 10
        if self.x < 0:
            self.x = 500
            

    def update(self): 
      pass 
        
