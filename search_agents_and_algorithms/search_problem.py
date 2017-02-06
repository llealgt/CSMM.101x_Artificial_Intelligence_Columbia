# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 23:05:23 2017

@author: luisf
"""

def is_goal(state):
    
    for index,value in enumerate(state):
        if index != value:
            return False
    
    return True