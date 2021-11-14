import pygame as pg
import numpy as np
import math

class Player:
    def __init__(self):
        self.pos = np.array([0, 0], dtype=float)
        self.angle = math.pi/4
        self.height = 270
        self.pitch = 40
        self.angleVel = 0.01
        self.vel = 3

    def update(self):
        sinA = math.sin(self.angle)
        cosA = math.cos(self.angle)

        pressedKey = pg.key.get_pressed()
        if pressedKey[pg.K_UP]:
            self.pitch += self.vel
        if pressedKey[pg.K_DOWN]:
            self.pitch -= self.vel
        if pressedKey[pg.K_LEFT]:
            self.angle -= self.angleVel
        if pressedKey[pg.K_RIGHT]:
            self.angle += self.angleVel

        if pressedKey[pg.K_w]:
            self.pos[0] += self.vel*cosA
            self.pos[1] += self.vel * sinA
        if pressedKey[pg.K_s]:
            self.pos[0] -= self.vel * cosA
            self.pos[1] -= self.vel * sinA
        if pressedKey[pg.K_a]:
            self.pos[0] += self.vel * cosA
            self.pos[1] -= self.vel * sinA
        if pressedKey[pg.K_d]:
            self.pos[0] -= self.vel * cosA
            self.pos[1] += self.vel * sinA

