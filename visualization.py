#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

"""
 Shows the solution circuit
"""
def geo_visualization( instance, solution ):
    fig = plt.figure( figsize=(12,12) )
    
    #min_coord = ( min(instance.cities_coordinates[:][0]), min(instance.cities_coordinates[:][0]))
    
    dist = 2*instance.matrix.max()
    
    back_map = Basemap( projection='lcc', resolution=None, width=8E6, height=8E6, lat_0=30, lon_0=-6 )
    back_map.etopo( scale=0.5, alpha=0.5 )
    
    x, y = back_map(-6, 36)
    plt.plot(x, y, 'ok', markersize=5)
    plt.text(x, y, ' Seattle', fontsize=12);