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
        print('switchOnPerson')
        
    def switchOnWall(self):
        self.i = 1
        self.setDecisionPlan()
        self.setPaintPlan(self.plan)
        print('switchonwall')
    
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
        self.pointlist = []
        self.show()
        self.button = None
    """   
    def drawLastWall(self):
        qp = QPainter()
        wall = self.walls.pop()
        qp.begin(self)
        pen = QPen(Qt.black, 3, Qt.SolidLine)
        qp.setPen(pen)
        if wall.ready:
            qp.drawLine(20,20,100,100)
            #qp.drawLine(wall.extract())
        qp.end()
    """    
        
    def paintEvent(self,event):    
        kol = len(self.people)
        print(kol,' ',person.myQPoint())
        
        if self.button == 1:
            qp1 = QPainter()
            qp1.begin(self)
            person = self.people[kol-1]
            brush = QBrush(Qt.SolidPattern)
            qp1.setBrush(brush)
            qp1.drawEllipse(100,100, 7, 7)
            qp1.setFont(QFont('Decorative', 10))
            qp1.drawText(person.x() + 7, person.y() + 7, 30, 20, 0, person.name)
            qp1.end()
            
            qp2 = QPainter()
            wall = self.walls.pop()
            qp2.begin(self)
            pen = QPen(Qt.black, 3, Qt.SolidLine)
            qp2.setPen(pen)
            if wall.ready:
                qp2.drawLine(20,20,100,100)
            #qp.drawLine(wall.extract())
            qp2.end()
            
    def mousePressEvent(self, event):
        self.decMousePressEvent(self,event)
    
    def makePerson(self,event):
        text = u"person"
        print('person')
        if event.button() == Qt.LeftButton:
            person = Node(event.x(),event.y(),text)
            self.people.append(person)
            #self.drawPerson(event)
            print('endperson')
            self.button = event.button()
            self.signal.flag.emit()
            #вставить ссылку на класс actor
    def makeWall(self,event):
         self.button = event.button()
         self.update()
    """    
    def makeWall(self,event):
        print('walls')
        if event.button() == Qt.LeftButton:
            point = Point(event.x(), event.y())
            self.pointlist.append(point)
            length = len(pointlist)
            if length%2 == 0:
                    point2 = self.pointlist.pop()
                    point1 = self.pointlist.pop()
                    wall = Wall(point1,u"Wall")
                    wall.endOfWall(point2)
                    self.walls.append(wall)
                    #self.drawLastWall(event)  
            self.signal.flag.emit()
    """
     
    Press = (makePerson, makeWall)