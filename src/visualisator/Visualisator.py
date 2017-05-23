# -*- coding: utf-8 -*-
"""
Created on Tue May 23 02:47:19 2017

@author: Наталья
"""
import time
from visualisator.GraficFunction import Point, Node, Wall
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import numpy as np

class CommunicatePainter(QObject):
          flag = pyqtSignal(int)
    
    
class Decision:
    def __init__(self,painter):
        self.painter = painter
        self.i = 0
        self.setDecisionPlan()
        self.setPaintPlan(self.plan)
        self.isMove = False
        
    def setDecisionPlan(self):
        self.plan = Painter.Press[self.i]
        
    def setPaintPlan(self, plan):
        self.painter.decMousePressEvent = plan
        
    def switchObject(self):
        if self.i == 0:
            self.i = 1
        elif self.i == 1:
            self.i = 0
        self.setDecisionPlan()
        self.setPaintPlan(self.plan)

    def switchOnPerson(self):
        self.i = 0
        self.setDecisionPlan()
        self.setPaintPlan(self.plan)
        
    def switchOnWall(self):
        self.i = 1
        self.setDecisionPlan()
        self.setPaintPlan(self.plan)        
        
    def switchOnEndPoint(self):
        self.i = 2
        self.setDecisionPlan()
        self.setPaintPlan(self.plan)        
        
        
class Painter(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.initUI()
        self.decision = Decision(self)
        self.signal = CommunicatePainter()
        self.signal.flag.connect(self.decision.switchObject)
        self.setMouseTracking(True)
        
    def initUI(self):
        print('NERE')
        
        self.col = QColor(255, 255, 255)
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), self.col)
        self.setPalette(self.p)
        
        self.setGeometry(0,0,500,500)
        self.walls = []
        self.people = []
        self.np = 0
        self.pointlist = []
        self.npoints = 0
        self.ep = 0 #end point
        self.button = None
        self.show()
        
    def paintEvent(self,event):    
        if self.button == 1:
            
            qp1 = QPainter()
            qp1.begin(self)
            i = 1
            for person in self.people:
                brush = QBrush(Qt.SolidPattern)
                qp1.setBrush(brush)
                qp1.drawEllipse(person.x(),person.y(), 7, 7)
                qp1.setFont(QFont('Decorative', 10))
                qp1.drawText(person.x() + 7, person.y() + 7, 40, 20, 0, person.name+str(i))
                i = i+1
            qp1.end()
            
            qp2 = QPainter()
            qp2.begin(self)
            for wall in self.walls:  
                if wall.completed:
                    pos = wall.extract()
                    pen = QPen(Qt.black, 3, Qt.SolidLine)
                    qp2.setPen(pen)
                    qp2.drawLine(pos[0],pos[1],pos[2],pos[3])
                else:
                    brush = QBrush(Qt.SolidPattern)
                    qp2.setBrush(brush)
                    qp2.drawEllipse(wall.fn.x(),wall.fn.y(),3,3)
            qp2.end()
            
            qp3 = QPainter()
            qp3.begin(self)
            if self.ep != 0:
                brush = QBrush(Qt.BDiagPattern)
                qp3.setBrush(brush)
                qp3.drawEllipse(self.ep.x(),self.ep.y(),20,20)
            qp3.end()
            
            
    def mousePressEvent(self, event):
        self.decMousePressEvent(self,event)
        
    
    def makePerson(self,event):
        person = Node( np.array([event.x(),event.y()]),u"P")
        self.people.append(person)
        self.np = self.np + 1
        self.button = event.button()
        self.update()
        
        
    def makeWall(self,event):
        point = Point( np.array([event.x(),event.y()]) )
        self.pointlist.append(point)
        self.npoints = self.npoints + 1
        if self.npoints%2 == 1:
            point1 = self.pointlist.pop()
            new_wall = Wall(point1)
            self.walls.append(new_wall)
        else:
            point2 = self.pointlist.pop()
            wall = self.walls.pop()
            wall.endOfWall(point2)
            self.walls.append(wall)
        self.button = event.button()
        self.update()
        
    def makeEndPoint(self,event):
        self.ep = Point( np.array([event.x(),event.y()]) )
        self.button = event.button()
        self.update()
        
    Press = (makePerson, makeWall,makeEndPoint)
    
    def buttonClicked(self):
        sender = self.sender()
        print('button ', sender.text())
        
        