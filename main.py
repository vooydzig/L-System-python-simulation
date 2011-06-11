#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rabbyt
import pyglet
from pyglet.gl import *
import os
from systems import *


class Window(pyglet.window.Window):
    def __init__(self, system):
        rabbyt.set_default_attribs()
        pyglet.window.Window.__init__(self, 800, 600)
            
        self.system = system
        
    def on_draw(self):
        rabbyt.clear()
#        glBegin(GL_LINES)
#        glVertex3f(0,0,0)
#        glVertex3f(10,0,0)
#        glEnd()
        self.system.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.S:
            mgr = pyglet.image.get_buffer_manager()
            name = "%s_%d.png"%(self.system.name, self.system.steps)
            name = os.path.join('gfx', name)
            mgr.get_color_buffer().save(name)
            
        if symbol == pyglet.window.key.PLUS:
            self.system.steps += 1
            self.system.simulate()
        
        if symbol == pyglet.window.key.MINUS:
            if self.system.steps > 0:
                self.system.steps -= 1
                self.system.simulate()

        if symbol == pyglet.window.key.ASTERISK or \
            symbol == pyglet.window.key.NUM_MULTIPLY:
            self.system.lenght *= 2

        if symbol == pyglet.window.key.SLASH or \
            symbol == pyglet.window.key.NUM_DIVIDE:
            self.system.lenght /= 2


system = LSystem2(start = 'F', steps = 0, lenght = 50, angle = 20, name = 'Leaf_3')
system.rules = {
        'F':'F[+F]F[-F][F]'
}
system.simulate()

window = Window(system)
pyglet.app.run()
