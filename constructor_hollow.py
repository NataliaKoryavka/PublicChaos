# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 11:50:00 2017

@author: Alexander Boyko
"""

class ConstructorWindow():
    def __init__(self):
        self.__viewer

class ViewerWidget():
    def paintEvent(self):
        #realisation
    def mousePressEvent(self):
        #realisation
    def mouseMoveEvent(self):
        #realisation
    def mouseReleaseEvent(self):
        #realisation
    def wheelEvent(self):
        #realisation
    def convertCoord(self):
        #realisation
    
class AbstractTool():
    def define(self):
        
class DefineSeederTool(AbstractTool):
    def define(self):
        #realisation

class DefineObstaclesTool(AbstractTool):
    def define(self):
        #realisation
        
class DefineGoalTool(AbstractTool):
    def define(self):
        #realisation