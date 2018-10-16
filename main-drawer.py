# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:05:03 2018

@author: AntoineFortECP
"""

from whiteboard_class import Circle, Square, Triangle
import numpy as np
import matplotlib.pyplot as plt


objects = [] #this list will contain the list of shapes to draw

#we ask the user to enter the shape he wants to draw (shape, size, color)
shape = input("""> shape among 'circle', 'square' and 'triangle' or
              'ERASE' to erase last drawn shape or 'STOP' to end drawing >""")

while shape.upper() != "STOP" :
    if shape == "circle" :
        Xcenter = float(input("> x coordinate of the center of the circle >"))
        Ycenter = float(input("> y coordinate of the center of the circle >"))
        radius = float(input("> radius of the circle >"))
        color = input("> color among 'blue', 'red' and 'green' >")
        objects.append(Circle((Xcenter, Ycenter), radius, color))
        #new circle has been added to the list 'objects'
    elif shape == "square" :
        Xupperleftcorner = float(input("> x coordinate of the upper left corner >"))
        Yupperleftcorner = float(input("> y coordinate of the upper left corner >"))
        side = float(input("> length of the side of the square >"))
        color = input("> color among 'blue', 'red' and 'green' >")
        objects.append(Square((Xupperleftcorner, Yupperleftcorner), side, color))
        #new square has been added to the list 'objects'
    elif shape == "triangle" :
        Xtopsummit = float(input("> x coordinate of the top sumit >"))
        Ytopsummit = float(input("> y coordinate of the top sumit >"))
        edge = float(input("> length of the edge of the equilateral triangle >"))
        color = input("> color among 'blue', 'red' and 'green' >")
        objects.append(Triangle((Xtopsummit, Ytopsummit), edge, color))
        #new shape has been added to the list 'objects'
    elif shape.upper() == "ERASE" :
        objects.pop() #we erase the last shape drawn
    else :
        print("shape " + shape + " does not exist !!!")
        
        

    index = 0 #we go through all objects to draw them all
    while  index < len(objects) :
        objet = objects[index]
        
        if objet.shape == "circle" :
            circle = objet #objet is now a circle
            x = circle.center[0]
            y = circle.center[1]
            r = circle.radius
            color = circle.color
    
            def polarX(teta) :
                return x + r*np.cos(teta) #polar equation of a circle
            def polarY(teta) :
                return y + r*np.sin(teta) #polar equation of a circle
            
            t = np.arange(0, 2*np.pi, 0.01)
            X = polarX(t)
            Y = polarY(t)
            
            if color == "blue" :
                plt.plot(X, Y, c='b')
            elif color == "red" :
                plt.plot(X, Y, c='r')
            elif color == "green" :
                plt.plot(X, Y, c='g')
            else :
                """error to be raised"""
                index+=0 #we do nothing now
            
        elif objet.shape == "square" :
            square = objet #objet is now a square
            x = square.corner[0]
            y = square.corner[1]
            c = square.side
            color = square.color
            
            sides_abs = []
            sides_ord = []
            
            #left side of the square
            sides_abs.append(np.array([x,x]))
            sides_ord.append(np.array([y-c, y]))
            #upper side of the square
            sides_abs.append(np.array([x, x+c]))
            sides_ord.append(np.array([y, y]))
            #right side of the square
            sides_abs.append(np.array([x+c, x+c]))
            sides_ord.append(np.array([y-c, y]))
            #lower side of the square
            sides_abs.append(np.array([x, x+c]))
            sides_ord.append(np.array([y-c, y-c]))
            
            for k in range(len(sides_abs)) :
                if color == "blue" :
                    plt.plot(sides_abs[k], sides_ord[k], c='b')
                elif color == "red" :
                    plt.plot(sides_abs[k], sides_ord[k], c='r')
                elif color == "green" :
                    plt.plot(sides_abs[k], sides_ord[k], c='g')
                else :
                    """error to be raised"""
                    index+=0 #we do nothing now
                    
        else :
            triangle = objet #objet is now a triangle
            x = triangle.summit[0]
            y = triangle.summit[1]
            c = triangle.side
            color = triangle.color
            
            lowerleftsummit = (x-(c/2), y-(c*np.sqrt(3)/2))
            lowerrightsummit = (x+(c/2), y-(c*np.sqrt(3)/2))
            
            edges_abs = []
            edges_ord = []        
            
            #first edge of the triangle
            edges_abs.append(np.array([lowerleftsummit[0], x]))
            edges_ord.append(np.array([lowerleftsummit[1], y]))
            #second edge of the triangle
            edges_abs.append(np.array([lowerrightsummit[0], x]))
            edges_ord.append(np.array([lowerrightsummit[1], y]))
            #third edge of the triangle
            edges_abs.append(np.array([lowerleftsummit[0], lowerrightsummit[0]]))
            edges_ord.append(np.array([lowerleftsummit[1], lowerrightsummit[1]]))
            
            for k in range(len(edges_abs)) :
                if color == "blue" :
                    plt.plot(edges_abs[k], edges_ord[k], c='b')
                elif color == "red" :
                    plt.plot(edges_abs[k], edges_ord[k], c='r')
                elif color == "green" :
                    plt.plot(edges_abs[k], edges_ord[k], c='g')
                else :
                    """error to be raised"""
                    index+=0 #we do nothing now
                    
            
        index+=1
    
    plt.show() #we show all expected shapes
    #now the user can start drawing a new shape or erase the previous one
    shape = input("""> shape among 'circle', 'square' and 'triangle' or
              'ERASE' to erase last drawn shape or 'STOP' to end drawing >""")
    












