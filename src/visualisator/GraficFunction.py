# -*- coding: utf-8 -*-
"""
Created on Tue May 23 02:11:37 2017

@author: Наталья
"""
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPolygon

class Point:
    def __init__(self, abs, ord):
        self.abs = abs
        self.ord = ord

    def x(self):
        return(self.abs)

    def y(self):
        return(self.ord)

    def myQPoint(self):
        return QPoint(self.abs, self.ord)

    @staticmethod
    def dist(point1, point2):
        return ((point2.x() - point1.x()) ** 2 + (point2.y() - point1.y()) ** 2) ** 0.5

class Node(Point):
    def __init__(self,abs,ord,name):
        super().__init__(abs,ord)
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
        return (self.x(), self.y())
    
    @staticmethod
    def newNode(x,y,name):
        v = Node(x,y,name)
        return v
    
class Wall:
    def __init__(self,first,name):
        self.name = name
        self.fn = first
        self.completed = False
        
    def endOfWall(self,end):
        if self.completed == False:
            self.en = end
            self.completed = True
        self.pos = [fn,en]
        
    def extract(self):
        if self.completed:
            pos = []
            for n in self.pos:
                pos.append((n.x(),n.y()))
            return pos
        
