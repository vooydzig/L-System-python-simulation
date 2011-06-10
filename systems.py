#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from pyglet.gl import *
import math

from vector import Vector2

class LSystem(object):
    def __init__(self, start = 'F-F-F-F', lenght = 10, angle = 90, steps = 4, name = 'Sample'):
        self.lenght = lenght
        self.angle = angle
        self.steps = steps
        self.name = name
        
        self.start = start
        self.variables = {
                'F':self._draw_forward,
                'f':self._move_forward,
            }
            
        self.constants = {
                '+':self._turn_right,
                '-':self._turn_left,
                '[':self._push_state,
                ']':self._pop_state
        }
        
        self.rules = {}
        
        self.states = []
        
        self.START_POINT = Vector2(0, 0 )
        self.START_DIRECTION = Vector2(1, 0)
        self.START_COLOR = [255, 255, 255]
        
    def draw(self):
        self.color = self.START_COLOR
        self.last_drawing_point = self.START_POINT 
        self.drawing_direction = self.START_DIRECTION
        glBegin(GL_LINES)
        for c in self.system:
            if c in self.variables.iterkeys():
                self.variables[c]()
            elif c in self.constants.iterkeys():
                self.constants[c]()
            else:
                self._skip()
        glEnd()
        
    def _draw_forward(self):
        glColor3ub(self.color[0],self.color[1],self.color[2])
        
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

    def _push_state(self):
        self.states.append({'point': self.last_drawing_point, 
            'direction': self.drawing_direction, 'color':self.color})
        self.color = [self.color[0] - 25, self.color[1], self.color[2]]
        
    def _pop_state(self):
        state = self.states.pop()
        self.last_drawing_point = state['point']
        self.drawing_direction = state['direction']
        self.color = state['color']

    def _skip(self):
        pass
    
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