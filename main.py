#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rabbyt
import pyglet

from systems import *


class Window(pyglet.window.Window):
    def __init__(self, system):
        rabbyt.set_default_attribs()
        pyglet.window.Window.__init__(self)
            
        self.system = system
        
    def on_draw(self):
        rabbyt.clear()
        self.system.draw()


system1 =  LSystem()
system1.rules = {
        'F':'FF-F-F-F-FF',
}
system1.simulate()

system2 =  LSystem(lenght = 5, steps=2)
system2.rules = {
        'F':'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF',
        'f':'ffffff'
}
system2.simulate()

system3 =  LSystem(lenght = 5, steps = 3)
system3.rules = {
        'F':'F-F+F+FF−F−F+F',
}
system3.simulate()

system4 =  LSystem(lenght = 5, steps=3)
system4.rules = {
        'F':'F+F-F-F+F',
}
system4.simulate()


window = Window(system4)
pyglet.app.run()