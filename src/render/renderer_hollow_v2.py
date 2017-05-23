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
#Метакласс синглетон
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
#Класс человека - является отдельным тредом. Подчиняется контроллеру, рассчитывает поля и делает шаг.
class Actor(threading.Thread):
    def __init__(self, pos, param, step, do_step, solve):
        super(Actor, self).__init__()
        #Позиция в "комнате"
        self.position =  pos# np.array([0, 0])
        #Поле цели
        self.fieldGoal = []
        #Поле дискомфорта от препятствия
        self.fieldComfortObstacle = []
        #Поле дискомфорта от толпы
        self.fieldComfortCrowd = []
        #Поле скорости
        self.fieldSpeed = 0
        #Направление движения
        self.direct = np.array([0, 0])
        #Толпа, содержащая этого человека
        self.crowd #это поле заполнит seeder после создания толпы.
        #Параметры - см. FieldSolver
        self.param = param
        #Шаг расчета градиента по X и Y
        self.step = step
        #Threading.Event(), указывающий сделать шаг
        self.do_step = do_step
        #Threading.Event(), указывающий сделать расчет градиента
        self.solve = solve
        #Явялется ли человек "ходоком" - т.е. движется ли он, является ли препятствием для других людей
        self.walker = False
        self.setDaemon(True)
        self.start()
    #Перегружаем run()
    def run(self):
        while self.walker == True:
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
            else:
                self.walker = False
                break
            self.do_step.wait()
            if np.linalg.norm(self.position - self.crowd.goal) > 0.01: #достижение цели - выбрать константу
                self.position += self.direct*self.fieldSpeed
            else:
                self.walker = False
                break
#Класс стены
class Wall(): #np.array([0,0]) дважды
    def __init__(self, pos1, pos2):
        #Положение первой точки стены в виде np.array([0, 0])
        self.pos1 = pos1
        #Положение второй точки стены в виде np.array([0, 0])
        self.pos2 = pos2
#класс толпы
class Crowd(metaclass=Singleton): #Singleton
    def __init__(self, actors, walls, goal):
        #list инстансов людей в толпе
        self.actors = actors
        #list инстансов препятствий
        self.walls = walls
        #Положение цели в виде np.array([0, 0])
        self.goal = goal
            
#Расчет плотности толпы относительно положения pos. Учитываются только люди с walker == True
class DensitySolver():
    #def __init__(self):
    @staticmethod
    def solveDensity(pos, crowd):
        num = 0
        radius = 5 #выбрать константу
        for actor in crowd.actors:
            if actor.walker == True:
                if np.linalg.norm(pos - actor.position) < radius:
                    num += 1
        return num
#Класс гладких убывающих функций для задания полей
class FieldFunction():
    #def __init__(self):
    @staticmethod
    def linear(x, s_min, s_max, x_min, x_max, c):
        if x >= x_max:
            return s_min
        if x <= x_min:
            return s_max
        if (x_max > x_min >= 0) and (s_max > s_min >= 0):
            return s_max + ((x - x_min)*(s_min - s_max))/(x_max - x_min)
        else:
            ???#виджет "вы неверно ввели параметры". Вернуться к началу
    @staticmethod        
    def power(x, s_min, s_max, x_min, x_max, c):
        if x >= x_max:
            return s_min
        if x <= x_min:
            return s_max
        if (x_max > x_min >= 0) and (s_max > s_min >= 0) and (c > 0):
            b = (s_min - s_max)*(c + x_min)*(c + x_max)/(x_min - x_max)
            a = s_max - b/(c + x_min)
            return a + b/(c + x)
        else:
            ???#виджет "вы неверно ввели параметры". Вернуться к началу.

#Рассчитывает значения полей цели, поля дискомфорта от препятствий(стен) и поля дискомфорта от людей. 
class FieldSolver(FieldFunction, DensitySolver):
    def __init__(self, pos, crowd, param, step):
        #super().__init__()
        self.crowd = crowd
        self.pos = pos
        self.step = step
        #Распаковка параметров ограничителей для каждого отдельного поля.
        self.x_gmin = param[0] 
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
        
    #Поле цели. Должно быть линейным по смыслу.
    def fieldGoal(self):
        x_goal = self.linear(self, np.linalg.norm(self.pos - self.crowd.goal), self.s_gmin, self.s_gmax, self.x_gmin, self.x_gmax, self.c_g)
        x_goal_x_step = self.linear(self, np.linalg.norm(self.pos + np.array([self.step, 0]) - self.crowd.goal), self.s_gmin, self.s_gmax, self.x_gmin, self.x_gmax, self.c_g)
        x_goal_y_step = self.linear(self, np.linalg.norm(self.pos + np.array([0, self.step]) - self.crowd.goal), self.s_gmin, self.s_gmax, self.x_gmin, self.x_gmax, self.c_g)
    return [x_goal, x_goal_x_step, x_goal_y_step]
    #Поле дискомфорта от препятствий зависит от углового размера стены относительно человека.
    def fieldComfortObstacle(self):
        summ = 0
        summ_x_step = 0
        summ_y_step = 0
        for wall in self.crowd.walls:
            vec1 = wall.pos1 - self.pos
            vec2 = wall.pos2 - self.pos
            summ += self.linear(self, np.arccos(np.dot(vec1, vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2))), self.s_wmin, self.s_wmax, self.x_wmin, self.x_wmax, self.c_w)
            vec1_x_step = vec1 - np.array([self.step, 0])
            vec2_x_step = vec2 - np.array([self.step, 0])
            summ_x_step += self.linear(self, np.arccos(np.dot(vec1_x_step, vec2_x_step)/(np.linalg.norm(vec1_x_step)*np.linalg.norm(vec2_x_step))), self.s_wmin, self.s_wmax, self.x_wmin, self.x_wmax, self.c_w)
            vec1_y_step = vec1 - np.array([0, self.step])
            vec2_y_step = vec2 - np.array([0, self.step])
            summ_y_step += self.linear(self, np.arccos(np.dot(vec1_y_step, vec2_y_step)/(np.linalg.norm(vec1_y_step)*np.linalg.norm(vec2_y_step))), self.s_wmin, self.s_wmax, self.x_wmin, self.x_wmax, self.c_w)
        return [summ, summ_x_step, summ_y_step]
    #Поле дискомфорта связанного с толпой зависит от расстояния от человека до каждого другого человека.
    def fieldComfortCrowd(self):
        summ = 0
        summ_x_step = 0
        summ_y_step = 0
        for actor in self.crowd.actors:
                if actor.walker == True:
                    summ += self.power(self, np.linalg.norm(self.pos - actor.position), self.s_pmin, self.s_pmax, self.x_pmin, self.x_pmax, self.c_p)
                    summ_x_step += self.power(self, np.linalg.norm(self.pos + np.array([self.step, 0]) - actor.position), self.s_pmin, self.s_pmax, self.x_pmin, self.x_pmax, self.c_p)
                    summ_y_step += self.power(self, np.linalg.norm(self.pos + np.array([0, self.step]) - actor.position), self.s_pmin, self.s_pmax, self.x_pmin, self.x_pmax, self.c_p)
        return [summ, summ_x_step, summ_y_step]
    #Поле скорости зависит от плотности толпы вокруг человека
    def fieldSpeed(self):
        return self.power(self.solveDensity(self.pos, self.crowd), self.f_min, self.f_max, self.p_min, self.p_max, self.c_f)

#Контроллер толпы. Управляет квантизацией времени шага.
class CrowdController(metaclass=Singleton): #singleton
    def __init__(self, do_step, solve):
        #Threading.Event(), указывающий сделать шаг
        self.do_step = do_step
        #Threading.Event(), указывающий сделать расчет градиента
        self.solve = solve
        #self.startMove()
    #Функция, контроллирующая движение    
    def startMove(self):
        while True:
            try:
                self.solve.set()
                time.sleep(1)
                self.solve.clear()
                self.do_step.set()
                time.sleep(1)
                self.do_step.clear()
            except KeyboardInterrupt: 
                self.solve.clear()
                self.do_Step.clear()
                break
                
#Конструктор. Запускает каскадное создание инстансов, создает инстансы людей. Получает параметры из UI.
class Constructor(metaclass=Singleton): #singleton
<<<<<<< HEAD
    def __init__(self, step, param): #ЭТО ВВОДИТСЯ ПОЛЬЗОВАТЕЛЕМ В ИНТЕРФЕЙСЕ
=======
    def __init__(self, crowd_size, step, param): #ЭТО ВВОДИТСЯ ПОЛЬЗОВАТЕЛЕМ В ИНТЕРФЕЙСЕ
        #Число людей в толпе
        self.crowd_size = crowd_size
        #Параметры - см. FieldSolver
>>>>>>> origin/master
        self.param = param
        #шаг расчета градиента
        self.step = step
<<<<<<< HEAD
        self.crowd = crowd
=======
        #инстанс синглетона толпы
        self.crowd
        #Threading.Event(), указывающий сделать шаг
>>>>>>> origin/master
        self.do_step = threading.Event()
        #Threading.Event(), указывающий сделать расчет градиента
        self.solve = threading.Event()
<<<<<<< HEAD
        self.crowdController = crowdController(self.do_step, self.solve)
    def start(self):
        for actor in self.crowd.actors:
            actor.crowd = self.crowd
            actor.walker = True
=======
        #инстанс синглетона контроллера
        self.crowdController
        self.construct()
    #Конструктор
    def construct(self):
        actors = []
        for i in range(self.crowd_size):
            pos = ???
            new_actor = Actor(pos, self.param, self.step, self.do_step, self.solve)
            actors.append(new_actor)
        self.crowd = Crowd(??? self.actors)
        for i in range(self.crowd_size):
            Actor.crowd = self.crowd
            Actor.walker = True
        self.crowdController = CrowdController(self.do_step, self.solve)
>>>>>>> origin/master
        

if __name__ == '__main__':
