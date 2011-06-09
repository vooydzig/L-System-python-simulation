#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import math

class Vector2(object):
    """Vector2 class. Implements typical vector2 math."""
    def __init__(self, x = 0, y = 0):
        """Constructor.
        
        @param x: Vector's X value
        @param y: Vector's Y value
        """
        self.x = float(x)
        self.y = float(y)
    def __repr__(self):
        return 'Vector2(%s, %s)' % (self.x, self.y)

    def zero(self):
        """Sets vector's X and Y to 0.0f. And returns it."""
        self.x = 0.0
        self.y = 0.0
        return self

    def clone(self):
        """Clones Vector2"""
        return Vector2(self.x, self.y)
    
    def is_zero(self):
        """Checks if both X and Y are 0.0"""
        if self.x == 0 and self.y ==0:
            return True
        return False

    def normalize(self):
        """Normalizes vector and returns it"""
        norm = float (1.0 / math.sqrt(self.x*self.x + self.y*self.y))
        self.x *= norm
        self.y *= norm        
        return self

    def invert(self):
        """Sets both X and Y to, respectively, -X and -Y"""
        self.x = -(self.x)
        self.y = -(self.y)
        return self

    def resize(self, sizeFactor):
        """Resizes vector by given factor, and returns it. It calls normalize() and scale(sizeFactor)"""
        self.normalize()
        self.scale(sizeFactor)
        return self

    def __sub__(self, t):        
        """Works as - operator
        
        @param t: vector to be subtracted
        @type t: engine.Vector2"""
        return Vector2(self.x - t.x, self.y - t.y)        
    
    def __add__(self, t):
        """Works as + operator
        
        @param t: vector to be added
        @type t: engine.Vector2"""
        return Vector2(self.x + t.x, self.y + t.y)        
        
    def __eq__(self, t):  
        """Works as == operator
        
        @param t: vector to be compared
        @type t: engine.Vector2"""
        if t == None:
            return False
        return self.x == t.x and self.y == t.y
    
    def roundToInt(self):     
        """Rounds both X and Y to integers"""
        self.x = int(self.x)
        self.y = int(self.y)
        return self
    
    def lengthSquared(self):
        """Returns the squared length of this vector."""
        return float((self.x*self.x) + (self.y*self.y))
    
    def length(self):
        """Returns the length of this vector."""
        return float(math.sqrt(self.x*self.x + self.y*self.y))
        
        
    def dot(self, v2):
        """Computes the dot product of this vector and given one
        
        @param v2: vector for dot product
        @type v2: engine.Vector2"""
        return (self.x * v2.x + self.y * v2.y)

    def interpolate(self, v2):
        """Linearly interpolates between this vector and v2 and returns the result point = (1-alpha)*v1 + alpha*v2.
        
        @param v2: vector for interpolation
        @type v2: engine.Vector2"""
        self.x = float((1 - math.alpha) * self.x + math.alpha * v2.x)
        self.y = float((1 - math.alpha) * self.y + math.alpha * v2.y)
        return Vector2(self.x, self.y)

    def angle(self, v2):
        """Returns the angle in radians between this vector and the vector parameter; 
        the return value is constrained to the range [0,PI].
        
        @param v2: vector to compute angle
        @type v2: engine.Vector2"""
        vDot = self.dot(v2) / (self.length() * v2.length())
        if vDot < -1.0 : vDot = -1.0
        if vDot > 1.0 : vDot = 1.0
        return float(math.acos(vDot))
    
    def limit(self, size):
        """Limits this vector to a given size.
        
        @param size: maximum size for vector
        @type size: float"""
        if (self.length() > size):
            self.normalize()
            self.scale(size)
            
            
    def distanceSquared(self, t1):
        """When used to store a point, 
        returns the square of the distance between two points.
        
        @param t1: point to compute squared distance
        @type t1: engine.Vector2"""
        dx = self.x - t1.x
        dy = self.y - t1.y
        return (dx * dx + dy * dy)
        
    def scale(self, s):
        """Scales vector by given value
        
        @param s: scale
        @type s: float"""
        self.x *= s
        self.y *= s
        return self
        
    def distance(self, pt):
        """When used to store a point, 
        returns the distance between two points.
        
        @param pt: point to compute squared distance
        @type pt: engine.Vector2"""
        dx = self.x - pt.x
        dy = self.y - pt.y
        return float(math.sqrt(dx * dx + dy * dy))
