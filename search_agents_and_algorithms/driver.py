import sys
import math
from search_problem import SearchProblem

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
    searchProblem = SearchProblem(initialState = board)
    
    #perform the selected method
    if method == 'bfs':
        searchProblem.breadth_first_search()
    elif method == 'dfs':
        searchProblem.depth_first_search()
    elif method == 'ast':
        searchProblem.a_star()
    elif method == 'ida':
        searchProblem.iterative_deepening_a_star()
    else:
        print('Not valid method selected')
    