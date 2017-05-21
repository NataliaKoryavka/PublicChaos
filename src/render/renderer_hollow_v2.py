# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 00:12:13 2017

@author: Alexander Boyko
"""
import numpy as np
import math
from math import exp
import threading
import time

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Actor(threading.Thread):
    def __init__(self, pos, param, step, do_step, solve):
        super(Actor, self).__init__()
        self.position =  pos# np.array([0, 0]) это заполняет seeder
        self.fieldGoal = []
        self.fieldComfortObstacle = []
        self.fieldComfortCrowd = []
        self.fieldSpeed = 0
        self.direct = np.array([0, 0])
        self.crowd #это поле заполнит seeder после создания толпы.
        self.param = param #это заполняет seeder
        self.step = step #это заполняет seeder
        self.do_step = do_step #это ивент
        self.solve = solve
        self.setDaemon(True)
        self.start()
        
    def run(self):
        while True:
            self.solve.wait()
            if np.linalg.norm(self.position - self.crowd.goal) > 0.01: #достижение цели - выбрать константу
                actorSolver = FieldSolver(self.position, self.crowd, self.param, self.step)
                self.fieldGoal = actorSolver.fieldGoal()
                self.fieldComfortObstacle = actorSolver.fieldComfortObstacle()
                self.fieldComfortCrowd = actorSolver.fieldComfortCrowd()
                self.fieldSpeed = actorSolver.fieldSpeed()
                field = self.fieldGoal[0] + self.fieldComfortObstacle[0] + self.fieldComfortCrowd[0]
                field_x_step = self.fieldGoal[1] + self.fieldComfortObstacle[1] + self.fieldComfortCrowd[1]
                field_y_step = self.fieldGoal[2] + self.fieldComfortObstacle[2] + self.fieldComfortCrowd[2]
                self.direct = np.array([-(field_x_step - field)/self.step, -(field_y_step - field)/self.step]) #антиградиент по определению

            self.do_step.wait()
            if np.linalg.norm(self.position - self.crowd.goal) > 0.01: #достижение цели - выбрать константу
                self.position += self.direct*self.fieldSpeed

class Crowd(metaclass=Singleton): #Singleton
    def __init__(self, actors, obstacles, goal):
        self.actors = actors
        self.obstacles = obstacles #WTF IS OBSTACLES
        #self.seeders = []
        self.goal = goal #np.array([0, 0])
    
    #def seed(self):

#class AbstractSeeder():
#    def seed(self):
        
        
#class SquareSeeder(AbstractSeeder):
#    super().__init__()
#    def seed(self):
       #realisation
       
#class LinearSeeder(AbstractSeeder):
#    super().__init__()
#    def seed(self):
       #realisation
       
#class PolygonalSeeder(AbstractSeeder):
#    super().__init__()
 #   def seed(self):
       #realisation

#class FileReader:
 #   def deserialize(self):
        #realisation
        
#class FileWriter:
#    def serialize(self):
        #realisation

class DensitySolver():
    #def __init__(self):
        
    def solveDensity(self, pos, crowd):
        num = 0
        radius = 5 #выбрать константу
        for other in crowd:
            if np.linalg.norm(pos - other.position) < radius:
                num += 1
        return num

class FieldFunction():
    #def __init__(self):
    
    def linear(self, x, s_min, s_max, x_min, x_max, c): #отлажено
        if x >= x_max:
            return s_min
        if x <= x_min:
            return s_max
        if (x_max > x_min >= 0) and (s_max > s_min >= 0):
            return s_max + ((x - x_min)*(s_min - s_max))/(x_max - x_min)
        else:
            raise badparam
            
    def power(self, x, s_min, s_max, x_min, x_max, c): #отлажено
        if x >= x_max:
            return s_min
        if x <= x_min:
            return s_max
        if (x_max > x_min >= 0) and (s_max > s_min >= 0) and (c > 0):
            b = (s_min - s_max)*(c + x_min)*(c + x_max)/(x_min - x_max)
            a = s_max - b/(c + x_min)
            return a + b/(c + x)
        else:
            raise badparam

class FieldSolver(FieldFunction, DensitySolver):
    def __init__(self, pos, crowd, param, step):
        #super().__init__()
        self.crowd = crowd
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
        self.f_min = param[18]
        self.f_max = param[19]
        
    def fieldGoal(self):
        x_goal = self.linear(self, np.linalg.norm(self.pos - self.crowd.goal), self.s_gmin, self.s_gmax, self.x_gmin, self.x_gmax, self.c_g)
        x_goal_x_step = self.linear(self, np.linalg.norm(self.pos + np.array([self.step, 0]) - self.crowd.goal), self.s_gmin, self.s_gmax, self.x_gmin, self.x_gmax, self.c_g)
        x_goal_y_step = self.linear(self, np.linalg.norm(self.pos + np.array([0, self.step]) - self.crowd.goal), self.s_gmin, self.s_gmax, self.x_gmin, self.x_gmax, self.c_g)
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
        return self.power(self.solveDensity(self.pos, self.crowd), self.f_min, self.f_max, self.p_min, self.p_max, self.c_f)


class CrowdController(metaclass=Singleton): #singleton
    def __init__(self, do_step, solve):
        self.do_step = do_step
        self.solve = solve
        self.doStep()
        
    def doStep(self):
        while True:
            try:
                self.solve.set()
                time.sleep(5) #SLEEEEEEEPING TIME
                self.solve.clear()
                self.do_step.set()
                time.sleep(5)
                self.do_step.clear()
            except:
                print("end")

class Constructor(metaclass=Singleton): #singleton
    def __init__(self, crowd_size, step, param): #ЭТО ВВОДИТСЯ ПОЛЬЗОВАТЕЛЕМ В ИНТЕРФЕЙСЕ
        self.crowd_size = crowd_size
        self.param = param
        self.step = step
        self.crowd
        self.do_step = threading.Event()
        self.solve = threading.Event()
        self.crowdController
        self.seed()
    def seed():
        actors = []
        for i in range(self.crowd_size):
            res = ???
            new_actor = Actor(res, self.param, self.step, self.do_step, self.solve)
            actors.append(new_actor)
        self.crowd = Crowd(??? self.actors)
        for i in range(self.crowd_size):
            Actor.crowd = self.crowd
        self.crowdController = CrowdController(self.do_step, self.solve)