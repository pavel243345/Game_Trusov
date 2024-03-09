import pygame as pg
from player import Player
from pipe import Pipe


Y = 600
X = 600


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Y, X))#пишем в скобочки размеры.
        self.back_surf = pg.image.load('sources/background.jpg')
        self.clock = pg.time.Clock()
        self.player = Player(self.screen)
        self.pipe = Pipe(self.screen)
    

    def game(self):
        while True:
            self.draw()
            self.move()
            self.update()
            self.clock.tick(30)

    def draw(self):
        self.screen.blit(self.back_surf, (0, 0))
        self.player.draw()
        self.pipe.draw()



    def move(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        keys = pg.key.get_pressed()
        self.player.move(keys)

    def update(self):
        pg.display.update()


game = Game()
game.game()

