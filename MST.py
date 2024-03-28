import heapq
#row is representing the vertex
#column is representing the edge

def Prims(G):
    num_vertices = len(G) #the number of vertices that we have in the matrix
    visited = [False] * num_vertices #to keep track if we visited or not. List of False with the number of verticces in G
    #when we do visit, it will update to True
    edges = [] #list for the number of edges


    priority_queue = [(0, 0, 0)]  #our tuple that will represent the first edge, 0 weight and connect to vertex 0
    #weight, source, destination

    while priority_queue: #as long as we have a queue
        weight, u, v = heapq.heappop(priority_queue) #we will pop the smallest weight in our queue

        if not visited[v]: #check if we visited this destination
            visited[v] = True #if we visited it then we update to True
            if u != 0 or v != 0:  # Make sure that we are not checking the initial tuple of (0, 0, 0)
                edges.append((u, v, weight)) #and then we add it to the edges list

#we get the index and value
            for neighbor in range(len(G[v])): #number of neighbors in v (current vertex) and creates range for the indices ofthe neighbors
                neighbor_weight =G[v][neighbor] #obtain the weight of the edge of current vertex and neighbor
                if neighbor_weight > 0 and not visited[neighbor]: #ifpositive and not visited, add to queue
                    heapq.heappush(priority_queue, (neighbor_weight, v, neighbor))

    return edges #return the final list of edges which represent our MST


# Example usage
input_graph = [
    [0, 8, 5, 0, 0, 0, 0],
    [8, 0, 10, 2, 18, 0, 0],
    [5, 10, 0, 3, 0, 16, 0],
    [0, 2, 3, 0, 12, 30, 14],
    [0, 18, 0, 12, 0, 0, 4],
    [0, 0, 16, 30, 0, 0, 26],
    [0, 0, 0, 14, 4, 26, 0]
]

result = Prims(input_graph)
print(result)
