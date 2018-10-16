# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:43:52 2018

@author: AntoineFortECP
"""

class WhiteBoard:
    def __init__(self, shape, color) :
        self._shape = shape
        self._color = color
    
    #getter and property for the shape attribute
    def _get_shape(self) :
        return self._shape
    shape = property(_get_shape)

    #getter and property for the color attribute
    def _get_color(self) :
        return self._color
    color = property(_get_color)
        
    
class Circle(WhiteBoard):
    def __init__(self, XYcenter, radius, color) :
        WhiteBoard.__init__(self, "circle", color)
        self._XYcenter = XYcenter #must be a (x,y) tuple coordinates
        self._radius = radius #lentgh of the radius of the circle
        
    #getter and property for the center attribute
    def _get_center(self) :
        return self._XYcenter
    center = property(_get_center)

    #getter and property for the radius attribute
    def _get_radius(self) :
        return self._radius
    radius = property(_get_radius)
    
    
class Square(WhiteBoard):
    def __init__(self, XYupperleftcorner, side, color) :
        WhiteBoard.__init__(self, "square", color)
        self._XYupperleftcorner = XYupperleftcorner #must be a (x,y) tuple coordinates
        self._side = side #length of the side of the square
        
    #getter and property for the upperleftcorner attribute
    def _get_corner(self) :
        return self._XYupperleftcorner
    corner = property(_get_corner)

    #getter and property for the side attribute
    def _get_side(self) :
        return self._side
    side = property(_get_side)
    
    
class Triangle(WhiteBoard): #all triangles will will equilateral
    def __init__(self, XYuppersummit, side, color) :
        WhiteBoard.__init__(self, "triangle", color)
        self._XYuppersummit = XYuppersummit #must be a (x,y) tuple coordinates
        self._side = side #length of the side of the triangle
    
    #getter and property for the uppersummit attribute
    def _get_summit(self) :
        return self._XYuppersummit
    summit = property(_get_summit)

    #getter and property for the side attribute
    def _get_side(self) :
        return self._side
    side = property(_get_side)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    