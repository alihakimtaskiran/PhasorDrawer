import math
import turtle
import time

class Drawer(object):
    def __init__(self):
        self.__phasors=[]
    def add(self, phasor):
        self.__phasors.append(phasor)
        
    def addM(self, phasors):
        self.__phasors+=phasors
    def graph(self,scalar, view_time):
        t=turtle.Turtle()
        t.speed(scalar*len(self.__phasors))
        for phasor in self.__phasors:
            t.left(phasor[1]/math.pi*180)
            
            t.forward(scalar*phasor[0])
        time.sleep(view_time)
        turtle.bye()
        
