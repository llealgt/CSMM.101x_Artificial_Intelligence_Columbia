# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 23:05:23 2017

@author: luisf
"""

from Node import Node
from collections import deque
import math

class SearchProblem:
    
    def __init__(self,initialState = []):
        self.rootNode = Node(state = initialState )
        self.size = int(math.sqrt(len(initialState)))

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
                
            for neighbor in node.neighbors:
                
                if not neighbor.visited: 
                    print "neighbor"
                

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
        
    #Return a node representing the result of an action in a parent node    
    def child_node(self,parent,action):
        
        #get the current location of the "0" to verify if is a valid action
        zero_row = self.get_element_row(parent.zero_position)
        zero_col = self.get_element_col(parent.zero_position)
        #get a copy(because it is handled by reference, not value) of the state that the parent node represents
        state = list(parent.state)

        #we need to swap the empty tide(zero value) with another tide depending on the action
        #we will validate swaps(if not valid return None) and calculate swap indexes depending 
        #on current indexes and action
        if action == "up" and zero_row > 0:
            row_index = -1
            col_index = 0
        elif action == "down" and zero_row< self.size-1:
            row_index = 1
            col_index = 0
        elif action == "right" and zero_col < self.size -1:
            row_index = 0
            col_index = 1
        elif action == "left" and zero_col > 0:
            row_index = 0
            col_index = -1
        else:
            #if its a non permited operation, return None
            return None
            
        #swap empty(0) tide with corresponding adjacent tide    
        temp_value = state[(zero_row+row_index)*self.size + zero_col + col_index]
        state[(zero_row+row_index)*self.size + zero_col + col_index] = 0
        state[zero_row*self.size + zero_col] = temp_value
            
        child = Node(parent = parent, state = state ,zero_position=(zero_row+row_index)*self.size + zero_col + col_index)
        
        return child
        
    #return the row in the corresponding 2dimensions of the element in 1 dimension
    def get_element_row(self,element=0):
         
        return element/self.size
        
    #return the column in the corresponding 2 dimensions of the element in 1 dimension
    def get_element_col(self,element = 0):
        
        return element%self.size
