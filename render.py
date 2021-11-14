import pygame as pg
from numba import njit
import numpy as np
import math

HeightMapImg = pg.image.load('assets/T_HeightMap.jpg')
HeightMap = pg.surfarray.array3d(HeightMapImg)

ColorMapImg = pg.image.load('assets/T_ColorMap.jpg')
ColorMap = pg.surfarray.array3d(ColorMapImg)

MapHeight = len(HeightMap[0])
MapWidth = len(HeightMap)


@njit(fastmath=True)
def RayCasting(screenArray, playerPos, playerAngle, playerHeight, playerPitch,
               screenWidth, screenHeight, deltaAndge, rayDistancem, hFov, scaleHeight):
    screenArray[:] = np.array([0, 0, 0])
    yBuffer = np.full(screenWidth, scaleHeight)

    rayAngle = playerAngle - hFov
    for numRay in range(screenWidth):
        firstContact = False
        sinA = math.sin(rayAngle)
        cosA = math.cos(rayAngle)

        for depth in range(1, rayDistancem):
            x = int(playerPos[0] + depth * cosA)
            if 0 < x < MapWidth:
                y = int(playerPos[1] + depth * sinA)
                if 0 < y < MapHeight:

                    depth *= math.cos(playerAngle - rayAngle)
                    heightOnScreen = int((playerHeight - HeightMap[x, y][0]) / depth * scaleHeight + playerPitch)

                    if not firstContact:
                        yBuffer[numRay] = min(heightOnScreen, screenHeight)
                        firstContact = True

                    if heightOnScreen < 0:
                        heightOnScreen = 0

                    if heightOnScreen < yBuffer[numRay]:
                        for yScreen in range(heightOnScreen, yBuffer[numRay]):
                            screenArray[numRay, yScreen] = ColorMap[x, y]
                        yBuffer[numRay] = heightOnScreen
        rayAngle += deltaAndge
    return screenArray


class Render:
    def __init__(self, app):
        self.app = app
        self.player = app.player
        self.fov = math.pi / 3
        self.hFov = self.fov / 2
        self.numRays = app.width
        self.deltaAngle = self.fov / self.numRays
        self.rayDistance = 2000
        self.scaleHeight = 620
        self.screenArray = np.full((app.width, app.height, 3), (0, 0, 0))

    def update(self):
        self.screenArray = RayCasting(self.screenArray, self.player.pos, self.player.angle,
                                      self.player.height, self.player.pitch, self.app.width, self.app.height,
                                      self.deltaAngle, self.rayDistance, self.hFov, self.scaleHeight)

    def draw(self):
        self.app.screen.blit(pg.surfarray.make_surface(self.screenArray), (0, 0))
