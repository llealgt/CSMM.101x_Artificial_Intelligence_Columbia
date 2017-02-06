# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 23:05:23 2017

@author: luisf
"""

from Node import Node
from collections import deque

class SearchProblem:
    
    def __init__(self,initialState = []):
        self.rootNode = Node(state = initialState )

    def breadth_first_search(self):
        print("bfs")
        self.frontier = deque()
        self.frontier.append(self.rootNode)
        
        #TODO:code to expand node and get its neighbors is still mising
        while len(self.frontier) > 0:
            node = self.frontier.popleft()
            
            node.visited = True
            
            if self.is_goal(state = node.state):
                self.get_problem_solution(node)
                

    def depth_first_search(self):
        print("dfs")

    def a_star(self):
        print("A star")      
        
    def iterative_deepening_a_star(self):
        print("ida")
        
    def is_goal(self,state=[]):
        
        for index,value in enumerate(state):
            if index != value:
                return False
        
        return True
        
    def get_problem_solution(self,node = None):
         
        while node != None:
            print(node.state)            
            node = node.parent
            
        
    def search_template(self,algorithm ="bfs"):
        print("Create a generic search")