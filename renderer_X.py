# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 00:12:13 2017

@author: Alexander Boyko
"""
import numpy as np
import math
from math import exp


class Actor:
    def __init__(self):
        self.position = np.array([0, 0, 0]) #массивы numpy - оотличный способ работы с векторами.
        self.vectors = []
        self.fields = []
        self.isAlive = True
    
    def distanceTool(self):
    
        
    def alignment(self):
        


class Crowd:
    def __init__(self):
        self.actors = []
        self.obstacles = []
        self.seeders = []
    
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

class CrowdController():
    def doStep(self):
            while stop_condition != 1:
                for i in Crowd.actors[]:
                    Actor.i.position += Actor.i.vectors*time #перемещение каждого агента вдоль вектора
            FieldSolver.solve()
            
class FileReader():
    def deserialize(self):
        #realisation
        
class FileWriter():
    def serialize(self):
        #realisation

class AbstractSolver():
    def solve(self):

class DummySolver(AbstractSolver):
    
class BoidsSolver(AbstractSolver):
    def solve(self):
        #realisation
    def vectorGoal(self):
        #realisation
    def vectorSeparation(self):
        #realisation
    def vectorAlignment(self):
        #realisation
    def vectorCohesion(self):
        #realisation
    def vectorObstacles(self):
        #realisation
    def inertionCorrect(self):
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
            
            
class FieldSolver(AbstractSolver)(actor, param):
    x = actor.position
    x_gmin = param[0]
    x_gmax = param[1]
    x_wmin = param[2]
    x_wmax = param[3]
    x_pmin = param[4]
    x_pmax = param[5]
    s_gmin = param[6]
    s_gmax = param[7]
    s_wmin = param[8]
    s_wmax = param[9]
    s_pmin = param[10]
    s_pmax = param[11]
    c_g = param[12]
    c_w = param[13]
    c_p = param[14]
    c_f = param[15]
    p_min = param[16]
    p_max = param[17]
    f_max = param[18]
    f_cr = param[19]
    
    
    def solve(self)
        #realisation
    def fieldGoal(self):
        return Function.sigmoidal(np.linalg.norm(x - BoidsSolver.vectorGoal), s_gmin, s_gmax, x_gmin, x_gmax, c_g)
    #добавить области видимости после реализации цели и препятствий
    def fieldComfortObstacle(self):
        summ = 0
        for k in xrange(10):#? - число точек на границе препятствия. Ожидается реализация
            summ += Function.linear(np.linalg.norm(x - BoidsSolver.vectorObstacles[k]), s_wmin, s_wmax, x_wmin, x_wmax, c_w)
        return summ
    
    def fieldComfortCrowd(self):
        summ = 0
        for k in len(Crowd.actors):# - число людей в толпе
            summ += Function.power(np.linalg.norm(x - Crowd.actors[k].position), s_pmin, s_pmax, x_pmin, x_pmax, c_p)
        return summ
    def fieldSpeed(self):
        if p < p_min:
            return f_max#максимальная скорость
        elif p > p_max:
            return f_cr#скорость движения в плотной толпе
        else:
            return Function.power(BoidsSolver.vectorCohesion(x + Step*actor.vectors[len(actor.vectors)]), p_min, f_max, p_max, f_cr, c_f)

class SwarmOptimizer():
    def __init__(self):
        self.__bestGoal

    def populate(self):
        #realisation
    def agentStep(self):
        #realisation
