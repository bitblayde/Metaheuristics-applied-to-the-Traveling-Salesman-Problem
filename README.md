# Algorithms applied to the Traveling Salesman Problem

The focus of this project is the implementation of different algorithms for the TSP in Python in it's symmetric version (although incorporating support for non-symmetric version when possible), with the goal of gaining an empirical understanding of the differences in performance between different families of algorithms and techniques. The results will help us deciding which algorithm to implement in a better performing language (e.g. C/C++ or Rust).

Different problem samples with varying sizes are available in 'samples' folder, involving different subsets of spanish cities, although any problem specified by a set of geographical points (which may or not contain an altitude coordinate) can be loaded via csv files. For more details check instructions available in 'TSP_rep'.

Methods for solution visualization can be found on 'visualization.py'.

## Implemented algorithms (so far)

### Greedy

* Nearest neighbor

## To be implemented

### Greedy

* Nearest insertion

* Farthest insertion

### Local Search

* k-Opt

### Genetic Algorithms

* Traditional generational approach (based on [Holland, 1975], but adding any modifications shown in more recent literature to increase performance).

* Steady-state model (based on [Whitley & Kauth, 1988, Whitley, 1989], incorporating once again newer improvements at authors' discretion).

* Memetic algorithm ([Moscato, 1989]).

### Approximation Algorithms

* Christofides algorithm ([Christofides,1976])

### Dynamic programming

* Held–Karp ([Bellman, 1962], [Held & Karp,1962])



