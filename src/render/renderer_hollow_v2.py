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
        self.position = np.array([0, 0]) #массивы numpy - отличный способ работы с векторами.
        self.fieldGoal = []
        self.fieldComfortObstacle = []
        self.fieldComfortCrowd = []
        self.fieldSpeed
        self.direct = np.array([0, 0])
        self.isAlive = False
    
    def distanceTool(self):
        #realisation
        
    def alignment(self):
        #realisation


class Crowd:
    def __init__(self):
        self.actors = []
        self.obstacles = []
        self.seeders = []
        self.goal = np.array([0, 0])
    
    def seed(self):

class AbstractSeeder:
    def seed(self):
        
        
class SquareSeeder(AbstractSeeder):
    super().__init__()
    def seed(self):
       #realisation
       
class LinearSeeder(AbstractSeeder):
    super().__init__()
    def seed(self):
       #realisation
       
class PolygonalSeeder(AbstractSeeder):
    super().__init__()
    def seed(self):
       #realisation

class FileReader:
    def deserialize(self):
        #realisation
        
class FileWriter:
    def serialize(self):
        #realisation

class AbstractSolver:
    def solve(self):
            
class DensitySolver(AbstractSolver):
    super().__init__()
    def solve(self, actor, crowd):
        num = 0
        radius = 5#выбрать константу
        for other in crowd:
            if np.linalg.norm(actor.position - other.position) < radius:
                num += 1
        return num/(radius*radius)
        
class FieldSolver():
    def __init__(self, pos, crowd, param, densitySolver, step):
        def __init__()
        self.crowd = crowd
        self.densitySolver = densitySolver
        self.pos = pos #np array with cords x, y
        self.step = step
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
        self.f_min = param[19]
            
    def linear(self, x, s_min, s_max, x_min, x_max, c):
        if x >= x_max:
            return s_min
        if x <= x_min:
            return s_max
        if (x_max > x_min > 0) and (s_max > s_min > 0):
            return s_min + (x - x_min)*(s_min - s_max)/(x_max - x_min)
        else:
            raise badparam
            
    def power(self, x, s_min, s_max, x_min, x_max, c):
        if x >= x_max:
            return s_min
        if x <= x_min:
            return s_max
        if (x_max > x_min > 0) and (s_max > s_min > 0) and (c > 0):
            b = (s_min - s_max)*(c + x_min)*(c + x_max)/(x_min - x_max)
            a = s_max - b/(c + x_min)
            return a + b/(c + x)
        else:
            raise badparam
            
    def sigmoidal(self, x, s_min, s_max, x_min, x_max, c):
        if x >= x_max:
            return s_min
        if x <= x_min:
            return s_max
        from math export exp
        if (x_max > x_min > 0) and (s_max > s_min > 0) and (c > 0):
            b = exp(-2*c)*(1 + exp(2*(c + x_min)))*(1 + exp(2*(c + x_max)))*(s_max - s_min)/(exp(2*x_max) - exp(2*x_min))
            a = s_max - b/(1 + exp(-2*(x_min + c)))
            return a - b/(1 + exp(-2*(x + c)))
        else:
            raise badparam
    
    def fieldGoal(self):
        x_goal = self.sigmoidal(self, np.linalg.norm(self.pos - self.crowd.goal), self.s_gmin, self.s_gmax, self.x_gmin, self.x_gmax, self.c_g)
        x_goal_x_step = self.sigmoidal(self, np.linalg.norm(self.pos + np.array([self.step, 0]) - self.crowd.goal), self.s_gmin, self.s_gmax, self.x_gmin, self.x_gmax, self.c_g)
        x_goal_y_step = self.sigmoidal(self, np.linalg.norm(self.pos + np.array([0, self.step]) - self.crowd.goal), self.s_gmin, self.s_gmax, self.x_gmin, self.x_gmax, self.c_g)
    return [x_goal, x_goal_x_step, x_goal_y_step]
    #добавить области видимости после реализации цели и препятстий
    def fieldComfortObstacle(self):
        summ = 0
        for k in xrange(10):#? - число точек на границе препятствия. Ожидается реализация
            summ += self.linear(self, np.linalg.norm(self.pos - self.crowd.obstacles[k]), self.s_wmin, self.s_wmax, self.x_wmin, self.x_wmax, self.c_w)
            summ_x_step += self.linear(self, np.linalg.norm(self.pos + np.array([self.step, 0]) - self.crowd.obstacles[k]), self.s_wmin, self.s_wmax, self.x_wmin, self.x_wmax, self.c_w)
            summ_y_step += self.linear(self, np.linalg.norm(self.pos + np.array([0, self.step]) - self.crowd.obstacles[k]), self.s_wmin, self.s_wmax, self.x_wmin, self.x_wmax, self.c_w)
        return [summ, summ_x_step, summ_y_step]
    
    def fieldComfortCrowd(self):
        summ = 0
        for k in len(self.crowd.actors):# - число людей в толпе
            summ += self.power(self, np.linalg.norm(self.pos - self.crowd.actors[k].position), self.s_pmin, self.s_pmax, self.x_pmin, self.x_pmax, self.c_p)
            summ_x_step += self.power(self, np.linalg.norm(self.pos + np.array([self.step, 0]) - self.crowd.actors[k].position), self.s_pmin, self.s_pmax, self.x_pmin, self.x_pmax, self.c_p)
            summ_y_step += self.power(self, np.linalg.norm(self.pos + np.array([0, self.step]) - self.crowd.actors[k].position), self.s_pmin, self.s_pmax, self.x_pmin, self.x_pmax, self.c_p)
        return [summ, summ_x_step, summ_y_step]
    
    def fieldSpeed(self):
        return self.power(self.densitySolver.solve(self.pos + actor.direct*self.f_cr), self.f_min, self.f_max, self.p_min, self.p_max, self.c_f)

class SwarmOptimizer:#должен возвращать вектор - массив numpy
    def __init__(self):
        self.__bestGoal

    def populate(self):
        #realisation
    def agentStep(self):
        #realisation

class CrowdController:
    def __init__(self):
        self.__param = []#20 perems
        self.__crowd
        self.__densitySolver = DensitySolver()
        #self.__swarmOptimizer = SwarmOptimizer()
        self.__squareSeeder
        self.__linearSeeder
        self.__polygonalSeeder
        self.__fileReader
        self.__fileWriter
        self.__fieldSolver
        self.__step = 0.01
        
    def doStep(self):
        for actor in self.__crowd.actors:
            if np.linalg.norm(actor.position - self.__crowd.goal) > 0.01: #достижение цели - выбрать константу
                actorSolver = FieldSolver(actor.position, self.__crowd, self.__param, self.__densitySolver, self.__step)
                actor.fieldGoal = actorSolver.fieldGoal()
                actor.fieldComfortObstacle = actorSolver.fieldComfortObstacle()
                actor.fieldComfortCrowd = actorSolver.fieldComfortCrowd()
                actor.fieldSpeed = actorSolver.fieldSpeed()
                #actor.direct = self.__swarmOptimizer#ожидается реализация swarm optimizer
                field = actor.fieldGoal[0] + actor.fieldComfortObstacle[0] + actor.fieldComfortCrowd[0]
                field_x_step = actor.fieldGoal[1] + actor.fieldComfortObstacle[1] + actor.fieldComfortCrowd[1]
                field_y_step = actor.fieldGoal[2] + actor.fieldComfortObstacle[2] + actor.fieldComfortCrowd[2]
                actor.direct = [-(field_x_step - field)/self.__step, -(field_y_step - field)/self.__step] #антиградиент по определению
                actor.position += actor.direct*actor.fieldSpeed