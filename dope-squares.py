#!/usr/bin/env python3

from random import randint
import pyxel


pyxel.init(160, 120, caption='Dope Fucking Squares')

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.y = 0
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_S, period=1, hold=1):     
            self.y = (self.y + 1) % pyxel.width
        if pyxel.btnp(pyxel.KEY_A, period=1, hold=1): 
            self.x = (self.x - 1) % pyxel.width 
        if pyxel.btnp(pyxel.KEY_W, period=1, hold=1): 
            self.y = (self.y - 1) % pyxel.width
        if pyxel.btnp(pyxel.KEY_D, period=1, hold=1): 
            self.x = (self.x + 1) % pyxel.width
        

    def draw(self):
        pyxel.cls(0)
        pyxel.circb(self.x, self.y, 10,  14)
        pyxel.circb(self.x, self.y, 9, randint(1,16))
        pyxel.circb(self.x, self.y, 8, randint(1,16))
        pyxel.circb(self.x, self.y, 7, randint(1,16))
        pyxel.circb(self.x, self.y, 6, randint(1,16))
        pyxel.circb(self.x, self.y, 5, randint(1,16))
        pyxel.circb(self.x, self.y, 4, randint(1,16))
        pyxel.circb(self.x, self.y, 3, randint(1,16))
        pyxel.circb(self.x, self.y, 2, randint(1,16))
        pyxel.circ(self.x, self.y, 1, randint(1,16))

        pyxel.text(35, 6, "Welcome to dope squares!", 9)


App()
