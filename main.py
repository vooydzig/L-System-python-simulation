#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rabbyt
import pyglet
import os
from systems import *


class Window(pyglet.window.Window):
    def __init__(self, system):
        rabbyt.set_default_attribs()
        pyglet.window.Window.__init__(self)
            
        self.system = system
        
    def on_draw(self):
        rabbyt.clear()
        self.system.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.S:
            mgr = pyglet.image.get_buffer_manager()
            name = "%s_%d.png"%(self.system.name, self.system.steps)
            name = os.path.join('gfx', name)
            mgr.get_color_buffer().save(name)
            
        if symbol == pyglet.window.key.PLUS:
            self.system.steps += 1
            self.system.lenght /= 2
            self.system.simulate()
        
        if symbol == pyglet.window.key.MINUS:
            self.system.steps -= 1
            self.system.lenght *= 2
            self.system.simulate()


system = LSystem(start = 'X', steps = 6, lenght = 2, angle = 25, name = 'Leaf')
system.rules = {
        'X':'F-[[X]+X]+F[+FX]-X',
        'F':'FF'
}
system.simulate()


system6 = LSystem(start = 'A', steps = 8, lenght = 2, angle = 60, name = 'Sierpinski triangle')
system6.rules = {
        'A':'B-A-B',
        'B':'A+B+A'
}
system6.variables = {
        'A':system6._draw_forward,
        'B':system6._draw_forward,
}
system6.simulate()

window = Window(system6)
pyglet.app.run()
