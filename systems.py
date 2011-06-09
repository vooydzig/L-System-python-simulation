#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from pyglet.gl import *
import math

from vector import Vector2

class LSystem(object):
    def __init__(self, start = 'F-F-F-F', lenght = 10, angle = 90, steps = 4):
        self.lenght = lenght
        self.angle = angle
        self.steps = steps
        
        self.start = start
        self.variables = {
                'F':self._draw_forward,
                'f':self._move_forward
            }
            
        self.constants = {
                '-':self._turn_right,
                '+':self._turn_left
        }
        
        self.rules = {}
        
        self.START_POINT = Vector2(400, 300)
        self.START_DIRECTION = Vector2(0, 1)
        
    def draw(self):
        self.last_drawing_point = self.START_POINT 
        self.drawing_direction = self.START_DIRECTION
        glBegin(GL_LINES)
        for c in self.system:
            if c in self.variables.iterkeys():
                self.variables[c]()
            elif c in self.constants.iterkeys():
                self.constants[c]()
        glEnd()
        
    def _draw_forward(self):
        glVertex3f(self.last_drawing_point.x, self.last_drawing_point.y, 0)
        next_drawing_point = Vector2(self.last_drawing_point.x+self.drawing_direction.x*self.lenght, self.last_drawing_point.y+self.drawing_direction.y*self.lenght)
        glVertex3f(next_drawing_point.x, next_drawing_point.y, 0)
        self.last_drawing_point = next_drawing_point.clone()
        
    def _move_forward(self):
        next_drawing_point = Vector2(self.last_drawing_point.x+self.drawing_direction.x*self.lenght, self.last_drawing_point.y+self.drawing_direction.y*self.lenght)
        self.last_drawing_point = next_drawing_point.clone()
        
    def _turn_left(self):
        x,y = self.drawing_direction.x, self.drawing_direction.y
        angle = math.radians(-self.angle)
        x2 = math.cos(angle) * x - math.sin(angle) * y
        y2 = math.sin(angle) * x + math.cos(angle) * y
        self.drawing_direction = Vector2(x2, y2)
        self.drawing_direction.normalize()
        
    def _turn_right(self):
        x,y = self.drawing_direction.x, self.drawing_direction.y
        angle = math.radians(self.angle)
        x2 = math.cos(angle) * x - math.sin(angle) * y
        y2 = math.sin(angle) * x + math.cos(angle) * y
        self.drawing_direction = Vector2(x2, y2)
        self.drawing_direction.normalize()

    def simulate(self):
        system = self.start
        for i in range(self.steps):
            next = ''
            for c in system:
                if c in self.rules.iterkeys():
                    next += self.rules[c]
                elif c in self.constants:
                    next += c
            system = next
        self.system = system