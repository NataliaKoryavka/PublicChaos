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
        #self.abs = abs
        #self.ord = ord
        self.pos = pos #np.array([0,0])

    def x(self):
        return self.pos[0]

    def y(self):
        return self.pos[1]

    def myQPoint(self):
        return QPoint(self.pos[0], self.pos[1])

    @staticmethod
    def dist(point1, point2):
        #return ((point2.x() - point1.x()) ** 2 + (point2.y() - point1.y()) ** 2) ** 0.5
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
    def __init__(self,first,name):
        self.name = name
        self.fn = first #Point
        self.pos1 = first.pos  #np.array([0,0])
        self.completed = False
        
    def endOfWall(self,end):
        if self.completed == False:
            self.en = end #Point
            self.pos2 = end.pos #np.array([0,0])
        #   self.completed = True
        #self.pos = [fn,en]
        
    def extract(self):
        if self.completed:
            #pos = []
            #for n in self.pos:
            #    pos.append((n.x(),n.y()))
            return self.pos1, self.pos2 #возвращаем два вектора
        