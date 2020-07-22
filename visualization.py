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
    
    components = list(zip(*instance.cities_coordinates))

    max_latitude = max(components[0])
    min_latitude = min(components[0])
    
    max_longitude = max(components[1])
    min_longitude = min(components[1])
    
    if (max_longitude - min_longitude)%360 > (min_longitude - max_longitude)%360:
        min_longitude, max_longitude = max_longitude, min_longitude
        
    print((max_latitude,max_longitude), (min_latitude,min_longitude))
    
    buffer_latitude_offset = abs(max_latitude - min_latitude)*0.15
    buffer_longitude_offset = abs(max_longitude - min_longitude)*0.15
    
    back_map = Basemap( projection='tmerc', resolution='h', llcrnrlat=min_latitude - buffer_latitude_offset, urcrnrlat = (max_latitude + buffer_latitude_offset), \
                           llcrnrlon=min_longitude - buffer_longitude_offset, urcrnrlon=max_longitude + buffer_longitude_offset, lat_0=(min_latitude+max_latitude)/2, lon_0=(min_longitude+max_longitude)/2 )
    
    back_map.drawmapboundary(fill_color='white')
    back_map.fillcontinents(color='#c6c6c6',lake_color='white')
    back_map.drawcoastlines()
    back_map.drawcountries(linewidth=2)
    back_map.drawstates(color='black')
    
    x, y = back_map.projtran(components[1], components[0])
    back_map.plot(x, y, '-', markersize=0, linewidth=0.7, c='#ee5959')
    back_map.plot(x, y, 'o', markersize=1.8, c='#ad0606')
    
    plt.show()