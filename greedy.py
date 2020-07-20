# -*- coding: utf-8 -*-



"""
 Generates a nearest neighbor solution for a given instance. Starting city in computed solution is always '0'.
"""
def nearest_neighbor( instance ):
    size = instance.matrix.shape[0]
    
    if size < 2:
        raise ValueError( "nearest_neighbor() : invalid problem size" )
        
    visited = [False]*size
    visited[0] = True
    solution = [0]
    
    for i in range(size-1):
        min_distance = float('+inf')
        
        #Find closest neighbor
        for j in range(1,size):
            if not visited[j] and instance.matrix[solution[-1],j] < min_distance:
                best_neighbor = j
                min_distance = instance.matrix[solution[-1],j]
                
        solution.append( best_neighbor )
        visited[best_neighbor] = True
        
    return solution
        