# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 22:14:33 2017

@author: luisf
"""
from collections import deque

class Node:
        
    def __init__(self,parent=None,path_cost = 0.0,visited=False,state=[]):
        self.parent = parent
        self.path_cost = path_cost
        self.visited = visited
        self.state = state
        self.zero_position =  state.index(0) #gets the position of the  empty(0 value) tide
        self.neighbors = deque()
        #get a string hash wich is the concatenation of the state values
        #for example [0,2,1,3] hash will be "0213"
        self.hash = "".join(map(str,state)) 