# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 21:08:37 2016

@author: Yicheng
"""

#import re
f = open("./project_2_data/act_process.txt","r")
g = open("./project_2_data/top10.txt","r")
h = open("./project_2_data/top10_mine.txt","r")

actDict = {}
actId = 0
for line in f.readlines():
    tokens = line.split("\t\t")
    actDict[tokens[0]] = actId
    actId = actId + 1
print ("actDict has been written successfully! Actors/actresses quantity: %d"%(len(actDict)))
#find the act name of the given top10 pagerank ids from R file
for line in g.readlines():
    tokens = line.split("\n")
    for key in actDict:
        if str(actDict[key]) == tokens[0]:
            print(key)
#find the act ids of my top10 favorite movie stars         
for line in h.readlines():
    tokens = line.split("\n")
    for key in actDict:
        if key == tokens[0]:
            print(actDict[key])

#then copy the ids to one file named top10_mine_id.txt which will be used in R to find pagerank of each id.

f.close()
g.close()
h.close()
