# -*- coding: utf-8 -*-
from itertools import combinations

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
        

"""
 Selects the best solution among the ones resulting from all possible reconnections of a circuit where edges in 'edges' list have been removed, with k>=2.
 An edge 'n' in list 'edges' denotes the removal of the edge connecting the n-th and (n+1)-th vertex of 'initial_sol'.
"""
def kOpt( instance, initial_sol, edges ):
    edges.sort()
    distances = [ instance.evaluate_solution( initial_sol[edges[i]:edges[(i+1)%len(edges)]] ) for i in range(len(edges)) ]
    print(distances)
    total = sum(distances) + sum( [ instance.matrix[initial_sol[e],initial_sol[(e+1)%instance.problem_size()]] for e in edges ] )
    print( total )
    print( instance.evaluate_solution( initial_sol ) )
    
def rand_kOpt( instance, initial_sol, k ):
    i = 0
    for comb in combinations( initial_sol, k ):
        i+=1
    print( i )
        
    