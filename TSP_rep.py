# -*- coding: utf-8 -*-

import math
import numpy as np
import geopy.distance
import csv

"""
 Euclidian distance operator. A and B, represented by tuples of coordinates, must belong to the same euclidean space.
"""
def euclidean_distance( A, B ):
    if len(A)!=len(B):
        raise ValueError( "euclidean_distance() : Points A and B do not have equal number of coordinates" )
        
    return math.sqrt( np.sum( [ (A[i] - B[i])**2 for i in range(len(A)) ] ) )

"""
 Geodesic distance operator. A and B may both have two or three coordinates, depending on wether or not altitude is to be used
 in distance computation.
"""
def geo_distance( A, B ):
    if len(A)!=len(B) or len(A)<2 or len(A)>3:
        raise ValueError( "geo_distance() : Invalid/mismatching number of coordinates" )
        
    dist = geopy.distance.distance( A[:2], B[:2] ).m
    
    if len(A)==3: # If altitude is included
        dist = math.sqrt( (A[2] - B[2])**2 + dist**2 )
        
    return dist
        

"""
 Generates a distances matrix from a list of points and a distance operator,
 which must accept exactly two parameters (points) and return a scalar
"""
def generate_distance_matrix( points, distance_operator, is_symmetric=True ):
    dmatrix = np.zeros( (len(points), len(points)) )
    for i in range( len(points) ):
        if is_symmetric:
            for j in range( i+1, len(points) ):
                dmatrix[i,j] = distance_operator( points[i], points[j] )
                dmatrix[j,i] = dmatrix[i,j]
        else:
            for j in range( i+1, len(points) ):
                dmatrix[i,j] = distance_operator( points[i], points[j] )
                dmatrix[j,i] = distance_operator( points[j], points[i] )
                
    return dmatrix

"""
 Class modelling instances of the travelling salesman problem.
"""
class TSP_Instance:
    
    """
     Args:
         'file_path': file containing ...
    """
    def __init__( self, file_path, coord_columns, name_columns ):
        self.cities_coordinates = []
        self.cities_names = []
        
        with open( file_path ) as file:
            reader = csv.reader( file )
            next(reader)
            for row in reader:
                self.cities_coordinates.append(tuple( [ float(row[index]) for index in coord_columns ] ))
                self.cities_names.append(tuple( [ row[index] for index in name_columns ] ))
                    

        self.matrix = generate_distance_matrix( self.cities_coordinates, geo_distance )
        
                    
    """
     Computes the total distance of a solution.
    """
    def evaluate_solution( self, solution ):
        return np.sum([ self.matrix[i,(i+1)%len(solution)] for i in range(len(solution)) ])
    
    """
      Checks if passed solution constitutes a valid permutation of all unique integers between 0 and n-1, with n
      being problem size (number of cities)
    """
    def is_solution_valid( self, solution ):
        return len(solution) == self.matrix.shape[0] and min(solution) == 0 and max(solution) == self.matrix.shape[0]-1 and len(set(solution)) == len(solution)
    
