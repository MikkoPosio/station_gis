# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 10:49:29 2017

@author: mikkopos
"""
# Example showing the information for the first 8 stations
stations = ['Hanko Russarö', 'Heinola Asemantaus', 'Helsinki Kaisaniemi',
          'Helsinki Malmi airfield', 'Hyvinkää Hyvinkäänkylä', 'Joutsa Savenaho',
          'Juuka Niemelä', 'Jyväskylä airport']

# Latitude coordinates (North - South)
lats = [59.77, 61.2, 60.18, 60.25, 60.6, 61.88, 63.23, 62.4]

# Longitude coordinates (West - East)
lons = [22.95, 26.05, 24.94, 25.05, 24.8, 26.09, 29.23, 25.67]
#cutoff values that correspond to the centroid of Finnish mainland
# North - South

nscutoff = 64.5

#East- West
ewcutoff = 26.3
#--------------------------------------------------
# step 1. Create lists for geographical zones 
ne = []
nw = []
sw = []
se = []

# Step2 Make a loop that iterates N number of times
# N should be based on the numerb of stations that we have here

#---------------------------------------------------------------------
N = len(stations)

# create a for loop that runs N of times
for i in range(N):
    #step 2.1 find out the latitude, longitude and the name of the station at index i
    lat = lats[i]
    lon = lons[i]
    station = stations [i]
    
    # steps 2.2 - 2.3 - Make conditional statements to add the stations to correct zone -list
    # You should determine if
    # a) the lat coordinate is North or south of the center latitude (stored in NScutoff variable)
    # AND
    # b) if the lon coordinate is East or West of the center longitude (stored in EWcutoff variable)
    # Based on the criteria you should add the NAME of the stations (from stations -list) to correct list(done step 1)
    #Make conditional statements to allocate the stations to correct zones
    
    #Check if the stations is South from center
    if lat < nscutoff:
        #Check if the station is in west
        if lon < ewcutoff:
            # if it was South-West add the station name to corresponding list
            sw.append(station)
    