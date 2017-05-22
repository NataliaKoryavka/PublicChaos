# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 01:41:46 2017

@author: Наталья
"""

import sys
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QComboBox,QMainWindow,QDockWidget,QAction,QFileDialog,QApplication, QWidget,QPushButton
from PyQt5.QtGui import QIcon,QFont, QPainter
from PyQt5.QtCore import QCoreApplication, Qt


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self): 
        self.panel = Panel(self) 
        self.panel_area = QDockWidget('new',self)
        self.panel_area.setWidget(self.panel)
        self.addDockWidget(Qt.BottomDockWidgetArea,self.panel_area)
        
        
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
      
        self.setGeometry(300, 200, 500, 500)
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
        
class Panel(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.list = QComboBox(self)
        self.list.addItem('Person')
        self.list.addItem('Walls')
        
        self.btn_start = QPushButton('Start',self)
        
        vertical = QVBoxLayout()
        vertical.addWidget(self.list)
        vertical.addStretch(1)
        vertical.addWidget(self.btn_start)
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
    print ('')