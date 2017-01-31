# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 22:14:33 2017

@author: luisf
"""

class Node:

    def __init__(self):
        self.parent = Node()
        self.path_cost = 0.0
        self.visited = False
        self.stage = []