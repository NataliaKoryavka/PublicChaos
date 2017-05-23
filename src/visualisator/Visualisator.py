# -*- coding: utf-8 -*-
"""
Created on Tue May 23 02:47:19 2017

@author: Наталья
"""
from GraficFunction import Point, SetPoint
from PyQt5.QWidget import *
from PyQt5.QCore import *
from PyQt5.QGui import *

class CommunicatePainter(QObject):
          flag = pyqtSygnal(int)
    
    
class Decision:
    def __init__(self,painter):
        self.painter = painter
        self.isMove = False
        self.setPerson()
        self.setSchema()
        
    def switchObject(self):
        return 0
    def switchOnPerson(self):
        return 0
    def switchOnWalls(self):
        return 0
    
class Painter(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.initUI()
        self.decision = Decision()
        self.signal = CommunicatePainter()
        self.signal.flag.connect(self.decision.switchObject)
        self.setMouseTracking(True)
    def initUI(self):
        
        col = QColor(255,255,255)
        self.setStyleSheet("QWidget { background-color: %s }"
                                    % col.name())
        
        self.setGeometry(200,200,500,500)
        self.walls = []
        self.people = []
        self.pointlist = []
        
    def mousePressEvent(self, event):
        self.customMousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.customMouseMoveEvent(self, event)

    def drawWall(self, qp):
        pen = QPen(Qt.black, 3, Qt.DashLine)
        qp.setPen(pen)
        points = []
        for point in self.pointList:
           points.append(point.myQPoint())
        polygon = QPolygon(points)
        qp.drawPolyline(polygon)