import heapq

def solve_puzzle(board, source, destination):
    """ Solve puzzle obtains parameters of board, source, destination which corresponds to
     a row which is either empty or passable, a tuple that represents the indices of its position and the destination to where
     we want to get to. What is returned is the tuple(starting postion) and the last tuple (our destination)
     If there is no valid path, then we return a none object.
     """
    rows= len(board) #rows in the board
    cols = len(board[0]) #columns in the board
    visited = set() #making an empty set to keep track of the cells
    priority_queue = [(0, source, [])] #initial value, starting position a-b, empty list to reach the cell

    while priority_queue: #as long as we have a queue aka not empty
        popped_tuple = heapq.heappop(priority_queue) #we pop the smallest element from the priority queue (ourmin heap)
        current_distance = popped_tuple[0] #we get the value of smallest element and label it current_distance
        current_row, current_col = popped_tuple[1] #we look at the second element which is our row and column tuple
        path = popped_tuple[2] # and then the third element is the path we took (R,L,U,D)

        if (current_row, current_col) == destination: #if we reached our destination
            return path + [(current_row, current_col)] #then we return the path and destination

        if ( 0 <= current_row < rows and 0 <= current_col < cols and board[current_row][current_col] == "-" and (current_row, current_col) not in visited):
            #if it is within the bounds of the row and column and is empty and not blocked and we havent visited
            visited.add((current_row, current_col)) #we add it to our visited set to explore

            # Explore adjacent cells
            for direc_row, direc_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #directions for moving up,down, right, left
                new_row, new_col = current_row + direc_row, current_col + direc_col #
                new_distance = current_distance + 1 #updating the distance to the new distance and changing it to +1 for adjacent cell

                if ( 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] == "-" and (new_row, new_col) not in visited):
                    #making sure we are in row and column range and make sure that it's an empty cell and also it hasnt been visited
                    heapq.heappush(priority_queue, (new_distance, (new_row, new_col), path + [(current_row, current_col)]))
                    #add to our priority queue
    return None

puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]
source = (0, 2)
destination = (2, 2)
result = solve_puzzle(puzzle, source, destination)
print(result)
