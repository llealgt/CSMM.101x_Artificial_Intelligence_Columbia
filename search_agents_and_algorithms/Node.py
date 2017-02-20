# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 22:14:33 2017

@author: luisf
"""
from collections import deque

class Node:
        
    def __init__(self,parent=None,path_cost = 0.0,visited=False,state=[],zero_position  = 0):
        self.parent = parent
        self.path_cost = path_cost
        self.visited = visited
        self.state = state
        self.zero_position = zero_position #fast acces to the index of the "0"
        self.neighbors = deque()