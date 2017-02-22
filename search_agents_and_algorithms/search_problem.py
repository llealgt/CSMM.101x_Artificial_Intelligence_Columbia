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
        self.frontier_hash = dict() #auxiliary hash table to know which nodes are already in the frontier

    def breadth_first_search(self):
        print("bfs")
        self.frontier = deque()
        self.frontier.append(self.rootNode)
        self.frontier_hash[self.rootNode.hash] = True
        
        #TODO:code to expand node and get its neighbors is still mising
        while len(self.frontier) > 0:
            node = self.frontier.popleft()
        
            if self.is_goal(state = node.state):
                print "solution found" 
                self.get_problem_solution(node)
                return
            
                
            self.generate_node_neighbors(node)           
            
            node.visited = True
                
            for neighbor in node.neighbors:
                
                if not neighbor.visited and not self.frontier_hash.get(neighbor.hash): 
                    self.frontier.append(neighbor)
                    self.frontier_hash[neighbor.hash] = True
        
        print "No solution found"
                

    def depth_first_search(self):
        print("dfs")
        self.frontier = deque()
        self.frontier.append(self.rootNode)
        self.frontier_hash[self.rootNode.hash] = True

        while len(self.frontier) > 0 :
            node = self.frontier.pop()
            
            if self.is_goal(state = node.state):
                print "Solution found"
                self.get_problem_solution(node)
                return
                
            self.generate_node_neighbors(node)
            
            node.visited = True
            
            while len(node.neighbors) > 0:
                
                neighbor = node.neighbors.pop()
                
                if not neighbor.visited and not self.frontier_hash.get(neighbor.hash):
                    self.frontier.append(neighbor)
                    self.frontier_hash[neighbor.hash] = True

        print "No solution found"

    def a_star(self):
        print("A star")      
        
    def iterative_deepening_a_star(self):
        print("ida")
        
    #given a state representing the current board, evaluate if its a goal state
    def is_goal(self,state=[]):
        
        previous_value = state[0]

        for index in range(1,len(state)):
            current_value = state[index]
            if current_value != 0:
                
                if previous_value > current_value:
                    return False
                
                previous_value = current_value
        
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
            
        child = Node(parent = parent, state = state)
        
        return child
        
    #return the row in the corresponding 2dimensions of the element in 1 dimension
    def get_element_row(self,element=0):
         
        return element/self.size
        
    #return the column in the corresponding 2 dimensions of the element in 1 dimension
    def get_element_col(self,element = 0):
        
        return element%self.size
        
    #generate a list of a node neighbors for a node
    def generate_node_neighbors(self,parent):

        #make sure no duplicate neighbors are generated yet
        if len(parent.neighbors) > 0 :
            return
        
        auxiliar_node = self.child_node(parent,"up")        
        if auxiliar_node  is not None:
            parent.neighbors.append(auxiliar_node)
            
        auxiliar_node = self.child_node(parent,"down")
        if auxiliar_node is not None:
            parent.neighbors.append(auxiliar_node)
            
        auxiliar_node = self.child_node(parent,"left")
        if auxiliar_node is not None:
            parent.neighbors.append(auxiliar_node)
            
        auxiliar_node = self.child_node(parent,"right")    
        if auxiliar_node is not None:
            parent.neighbors.append(auxiliar_node)
        
            
