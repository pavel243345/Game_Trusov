import pygame as pg 
from player import Player 
from pup import Pup

class Game:
    def __init__(self): 
        pg.init()
        self.screen = pg.display.set_mode((500,500))
        self.back_surf = pg.image.load('sources/back.jpg')
        self.clock = pg.time.Clock()
        self.player = Player(self.screen)
        self.pup = Pup(self.screen)

    def game(self): 
        while True: 
            
            self.move()
            self.draw()
            self.update()
            self.clock.tick(30)

    def draw(self):
        self.screen.fill('white')
        self.player.draw()
        self.pup.draw()

    def move(self): 
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                pg.quit()

        keys_pressed = pg.key.get_pressed()
        self.player.move(keys_pressed)
        self.pup.move()
        
    def update(self): 
        pg.display.update()

game = Game()
game.game()