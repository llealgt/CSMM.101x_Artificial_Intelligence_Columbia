# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 22:14:33 2017

@author: luisf
"""

class Node:
        
    def __init__(self,parent=None,path_cost = 0.0,visited=False,state=[]):
        self.parent = parent
        self.path_cost = path_cost
        self.visited = visited
        self.state = state