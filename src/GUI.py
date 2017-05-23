# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 01:41:46 2017

@author: Наталья
"""

import sys
from PyQt5.QtWidgets import QGridLayout,QVBoxLayout,QHBoxLayout,QComboBox,QMainWindow,QDockWidget,QAction,QFileDialog,QApplication, QWidget,QPushButton
from PyQt5.QtGui import QColor,QIcon,QFont, QPainter
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSignal, QObject
from visualisator.Visualisator import Painter

class Communicate(QObject):

    updateP = pyqtSignal(int)

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self): 
        self.widget = Interface(self)
        self.setCentralWidget(self.widget)
        
        
        exitAction = QAction( QIcon('../resources/exit2.png'),'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        saveAction = QAction(QIcon('../resources/save.png'), 'Save', self)
        saveAction.setShortcut('F2')
        saveAction.setStatusTip('save current file')
        saveAction.triggered.connect(self.save)

        loadAction = QAction(QIcon('../resources/load.png'), 'Load file', self)
        loadAction.setShortcut('F6')
        loadAction.setStatusTip('Download existing file')
        loadAction.triggered.connect(self.load)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(loadAction)
      
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('ChaosTheory')    
        self.show()
        
    def save(self):

        fname = QFileDialog.getOpenFileName(self, 'save file', '/home')
        if fname[0]:
            
            return 0
        else:
            return -1
        
    def load(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname[0]:
            return 0

class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        #self.painter = Painter(self)
        self.setMinimumSize(300,300)
              
    
class Interface(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.col = QColor(100,100,100)
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), self.col)
        self.setPalette(self.p)  
        
        grid = QGridLayout()
        
        self.canvas = Canvas()
        self.painter = Painter(self.canvas)
        
        getPerson = QAction('Person',self)
        getPerson.triggered.connect(self.painter.decision.switchOnPerson)
        
        getWall = QAction('Walls',self)
        getWall.triggered.connect(self.painter.decision.switchOnWall)
        
        getEndPoint = QAction('EndPoint',self)
        getEndPoint.triggered.connect(self.painter.decision.switchOnEndPoint)
        
        
        
        self.listoftrig = []
        self.listoftrig.append(getPerson)
        self.listoftrig.append(getWall)
        self.listoftrig.append(getEndPoint)
        
        self.list = QComboBox(self)       
        self.list.addItem('Person')
        self.list.addItem('Walls')
        self.list.addItem('EndPoint')
        
        self.list.activated[str].connect(self.chooseObject)
        
        self.btn_start = QPushButton('Start',self)
        self.btn_start.clicked.connect(self.painter.buttonClicked)
        
        grid.addWidget(self.list,2,0)
        grid.addWidget(self.btn_start,6,0)
        grid.addWidget(self.canvas,0,1,12,5)
        self.setLayout(grid)
        
    def chooseObject(self,str):
        for action in self.listoftrig:
            if action.text() == str:
                action.trigger();
                break
    
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    app.exec_()
    print ('')