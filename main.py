import pygame as pg
from player import Player
from render import Render

class App:
    def __init__(self):
        self.res = self.width, self.height = (800, 600)
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()
        self.player = Player()
        self.render = Render(self)

    def update(self):
        self.player.update()
        self.render.update()

    def draw(self):
        self.render.draw()
        pg.display.flip()

    def run(self):
        while True:
            self.update()
            self.draw()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(60)
            pg.display.set_caption(f'FPS: {self.clock.get_fps()}')

if __name__ == '__main__':
    app = App()
    app.run()