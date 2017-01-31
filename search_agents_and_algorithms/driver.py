import sys
import math
from Node import Node

if __name__ == '__main__':
    
    #input search algorithm and initial state array
    method = sys.argv[1]
    board = map(int,sys.argv[2].split(','))
    
    #Validate initial board(is square if square root is integer)
    #End execution if initial board is not valid
    board_size = len(board)

    if not math.sqrt(board_size).is_integer():
        print("Invalid board,try again")
        sys.exit(0)
    
    #create the root node with the given board(initial state)
    root_node =  Node(state=board)
    
    #perform the selected method
    if method == 'bfs':
        print('bfs')
    elif method == 'dfs':
        print('dfs')
    elif method == 'ast':
        print('ast')
    elif method == 'ida':
        print('ida')
    else:
        print('Not valid method selected')
    