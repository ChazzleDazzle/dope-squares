#!/usr/bin/env python3

from random import randint
import time
import math

import pyxel

START = time.time()


class App:

    def __init__(self):
        pyxel.init(200, 200, caption="Dope Squares")
        self.x = 100
        self.y = 100
        pyxel.image(0).load(0, 0, "assets/Adventurer/adventurer-Sheet.png")

        # This has to be the last line of the init method.
        pyxel.run(self.update, self.draw)

    def update(self):
        period = 1
        hold = 1
        mult = 1
        if pyxel.btnp(pyxel.KEY_RIGHT_SHIFT, period=period, hold=hold):
            mult += 1
        speed = 2
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_S, period=period, hold=hold) or pyxel.btnp(
            pyxel.KEY_DOWN, period=period, hold=hold
        ):
            self.y = (self.y + speed * mult) % pyxel.width
        if pyxel.btnp(pyxel.KEY_A, period=period, hold=hold) or pyxel.btnp(
            pyxel.KEY_LEFT, period=period, hold=hold
        ):
            self.x = (self.x - speed * mult) % pyxel.width
        if pyxel.btnp(pyxel.KEY_W, period=period, hold=hold) or pyxel.btnp(
            pyxel.KEY_UP, period=period, hold=hold
        ):
            self.y = (self.y - speed * mult) % pyxel.width
        if pyxel.btnp(pyxel.KEY_D, period=period, hold=hold) or pyxel.btnp(
            pyxel.KEY_RIGHT, period=period, hold=hold
        ):
            self.x = (self.x + speed * mult) % pyxel.width


    def draw(self):
        offset = abs(round(math.sin(pyxel.frame_count * 0.1) * 3))
        pyxel.cls(13)
        # Head
        pyxel.circ(self.x, self.y, 10, 14)
        # Eyes
        pyxel.circ(self.x - 4, self.y - 5, 2, 7)
        pyxel.circ(self.x + 4, self.y - 5, 2, 7)
        pyxel.rect(self.x - 3, self.y - 4, self.x - 4, self.y - 5, 12)
        pyxel.rect(self.x + 3, self.y - 4, self.x + 4, self.y - 5, 12)

        idle_slices = [(0, 0), (50, 0), (100, 0), (150, 0),]

        # Land
        # rect(x1, y1, x2, y2, col)
        pyxel.rect(0, 136, 100, 200, 11)
        pyxel.rect(100, 136, 200, 200, 11)

        # Animation
        pyxel.blt(20, 100, 0, idle_slices[offset][0], idle_slices[offset][1], 50, 37, 0)
        


        if time.time() - START < 5:
            pyxel.text(35, 6, "Welcome to dope squares!", randint(1, 15))

        pyxel.text(10, 190, f"center: x:{self.x} y:{self.y}", 7)
        pyxel.text(10, 180, f"offset: {offset}", 7)


App()
