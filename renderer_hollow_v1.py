# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 00:12:13 2017

@author: Alexander Boyko
"""
import numpy as np
import math
from math import exp
import threading

class Actor:
    def __init__(self):
        self.position = np.array([0, 0, 0]) #массивы numpy - оотличный способ работы с векторами.
        self.fieldComfortObstacle
        self.fieldComfortCrowd
        self.fieldSpeed 
        self.direct = np.array([0, 0, 0])
        self.isAlive = False
    
    def distanceTool(self):
    
        
    def alignment(self):
        


class Crowd:
    def __init__(self):
        self.actors = []
        self.obstacles = []
        self.seeders = []
        self.goal = np.array([0, 0, 0])
    
    def seed(self):

class AbstractSeeder:
    def seed(self):
        
        
class SquareSeeder(AbstractSeeder):
    def seed(self):
       #realisation
       
class LinearSeeder(AbstractSeeder):
    def seed(self):
       #realisation
       
class PolygonalSeeder(AbstractSeeder):
    def seed(self):
       #realisation

class FileReader():
    def deserialize(self):
        #realisation
        
class FileWriter():
    def serialize(self):
        #realisation

class Function(x, s_min, s_max, x_min, x_max, c):
    def check(self):
        if x >= x_max:
            return y_min
        if x <= x_min:
            return y_max
        
    def linear(self):
        self.check()
        if (x_max > x_min > 0):
            return y_min + (x - x_min)*(y_min - y_max)/(x_max - x_min)
        else:
            raise badparam
            
    def power(self):
        self.check()
        if (x_max > x_min > 0) and (c > 0):
            a = y_max - b/(c + x_min)
            b = (y_min - y_max)*(c + x_min)*(c + x_max)/(x_min - x_max)
            return a + b/(c + x)
        else:
            raise badparam
            
    def sigmoidal(self):
        self.check()
        from math export exp
        if (x_max > x_min > 0) and (c > 0):
            a = y_max - b/(1 + exp(-2*(x_min + c)))
            b = exp(-2*c)*(1 + exp(2*(c + x_min)))*(1 + exp(2*(c + x_max)))*(y_max - y_min)/(exp(2*x_max) - exp(2*x_min))
            return a - b/(1 + exp(-2*(x + c)))
        else:
            raise badparam
            
class AbstractSolver():
    def solve(self):
            
class DensitySolver(AbstractSolver)(actor):
    def solve(self):
        num = 0
        radius = 5#выбрать константу
        for other in __crowd:
            if np.linalg.norm(actor.position - other.position) < radius:
                num += 1
        return num/(radius*radius)
        
class FieldSolver(AbstractSolver)(actor, param):
    def __init__(self):
        self.__swarmOptimizer
        self.x = actor.position
        self.x_gmin = param[0] #unpacking params
        self.x_gmax = param[1]
        self.x_wmin = param[2]
        self.x_wmax = param[3]
        self.x_pmin = param[4]
        self.x_pmax = param[5]
        self.s_gmin = param[6]
        self.s_gmax = param[7]
        self.s_wmin = param[8]
        self.s_wmax = param[9]
        self.s_pmin = param[10]
        self.s_pmax = param[11]
        self.c_g = param[12]
        self.c_w = param[13]
        self.c_p = param[14]
        self.c_f = param[15]
        self.p_min = param[16]
        self.p_max = param[17]
        self.f_max = param[18]
        self.f_cr = param[19]
    
    def solve(self)
        #realisation
    def fieldGoal(self):
        return __function(np.linalg.norm(x - __crowd.goal), s_gmin, s_gmax, x_gmin, x_gmax, c_g).sigmoidal()
    #добавить области видимости после реализации цели и препятствий
    def fieldComfortObstacle(self):
        summ = 0
        for k in xrange(10):#? - число точек на границе препятствия. Ожидается реализация
            summ += __function(np.linalg.norm(x - __crowd.obstacles[k]), s_wmin, s_wmax, x_wmin, x_wmax, c_w).linear()
        return summ
    
    def fieldComfortCrowd(self):
        summ = 0
        for k in len(Crowd.actors):# - число людей в толпе
            summ += __function(np.linalg.norm(x - __crowd.actors[k].position), s_pmin, s_pmax, x_pmin, x_pmax, c_p).power()
        return summ
    
    def fieldSpeed(self):
        if p < p_min:
            return f_max#максимальная скорость
        elif p > p_max:
            return f_cr#скорость движения в плотной толпе
        else:
            return __function(__densitySolver.solve(x + actor.direct*f_cr), p_min, f_max, p_max, f_cr, c_f).power()

class SwarmOptimizer():#должен возвращать вектор - массив numpy
    def __init__(self):
        self.__bestGoal

    def populate(self):
        #realisation
    def agentStep(self):
        #realisation

class CrowdController():
    def __init__(self):
        self.__param = []
        self.__crowd
        self.__densitySolver
        self.__squareSeeder
        self.__linearSeeder
        self.__polygonalSeeder
        self.__fileReader
        self.__fileWriter
        self.__fieldSolver
        
    def doStep(self):
        for actor in self.__crowd.actors:
            if np.linalg.norm(actor.position - __crowd.goal) > 0.01: #достижение цели - выбрать константу
                actor.fieldComfortObstacle = __fieldSolver(actor, self.__param).fieldComfortObstacle()
                actor.fieldComfortCrowd = __fieldSolver(actor, self.__param).fieldComfortCrowd()
                actor.fieldSpeed = __fieldSolver(actor, self.__param).fieldSpeed()
                actor.direct = __fieldSolver(actor, self.__param).__swarmOptimizer()
                actor.position += actor.direct*actor.fieldSpeed