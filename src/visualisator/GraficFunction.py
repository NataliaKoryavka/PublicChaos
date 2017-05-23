# -*- coding: utf-8 -*-
"""
Created on Tue May 23 02:11:37 2017

@author: Наталья
"""
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPolygon
import numpy as np

class Point:
    def __init__(self, pos):
        self.pos = pos #np.array([0,0])

    def x(self):
        return self.pos[0]

    def y(self):
        return self.pos[1]

    def myQPoint(self):
        return [self.pos[0], self.pos[1]]

    @staticmethod
    def dist(point1, point2):
        return np.linalg.norm(point2.pos - point1.pos)

class Node(Point):
    def __init__(self, pos, name):
        super().__init__(pos)
        self.name = name
        self.isBeginning = False
        self.isEnd = False

    def setBeginning(self):
        self.isBeginning = True

    def setEnd(self):
        self.isEnd = True
        
    def setUnallocated(self):
        self.isBeginning = False
        self.isEnd = False
        
    def setName(self, str):
        self.name = str

    def getName(self):
        return self.name
    
    def extract(self):
        return self.pos
    
    @staticmethod
    def newNode(pos, name):
        v = Node(pos, name)
        return v
    
class Wall:
    def __init__(self,first):
        self.fn = first #Point
        self.en = Point( np.array([0,0]) )
        self.completed = False
        
    def endOfWall(self,end):
        if self.completed == False:
            self.en = end #Point
            self.completed = True
        print('makeWall', self.extract())
        
    def extract(self):
        if self.completed:
            coord = []
            coord.append(self.fn.x())
            coord.append(self.fn.y())
            coord.append(self.en.x())
            coord.append(self.en.y())
            return coord #возвращаем координаты двух векторов
        