# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 14:07:30 2016

@author: Gaoxiang
"""

import re
f = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/processedAct.txt","r")
g = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/movie_genre.txt","r")
m_g = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/movie_graph.txt","w")

print("Open files successfully")

actorDict={}
#building movie dictionary, key=movie name
mId=0
for line in g.readlines():
	tokens = line.split("\t\t")
	movieDict[tokens[0]]=[mId]
	mId+=1
print ("movie:%d"%(mId))


movieDict={}
#building actor dictionary, key=actor name
actId=0
for line in f.readlines():
    tokens = line.split("\t\t")
    actName = tokens[0]
    tokens[0] = actId
    for i in range(1, len(tokens)):
        movie = tokens[i]
        year = re.search(r'\(\d\d\d\d\)|\(\?\?\?\?\)',movie)
        if year:
            end=movie.find(year.group())
            tokens[i]=movie[:end+6]
        if movieDict.has_key(tokens[i]):
            movieDict[tokens[i]].append(actName)
        else:
            movieDict[tokens[i]]=[len(movieDict)]
            movieDict[tokens[i]].append(actName)
    actorDict[actName] = tokens
    actId = actId + 1
print ("actor:%d"%(actId))

movieDict_new={}
for movie in movieDict:
	if(len(movieDict[movie]))>15 and len(movie)>0:
		movieDict_new[movie]=movieDict[movie]
print (%(len(movieDict_new)))

Numer={}
Denom={}
for key_movie in movieDict_new:
	for i in range(1,len(movieDict_new[key_movie])):
		actName =  movieDict_new[key_movie][i]
		for movie in actorDict[actName]:
			if movie==key_movie or isinstance(movie,int) or (not movieDict_new.has_key(movie)):
				continue#skip same movie or no movie or movie ID
			totActor = len(movieDict_new[key_movie])+len(movieDict_new[movie])-2
			if Numer.has_key((movieDict_new[key_movie][0],movieDict_new[movie][0])):
				Numer[(movieDict_new[key_movie][0],movieDict_new[movie][0])]+=1
			elif Numer.has_key((movieDict_new[movie][0], movieDict_new[key_movie][0])):
				Numer[(movieDict_new[movie][0], movieDict_new[key_movie][0])]+=1
			else:
				Numer[(movieDict_new[key_movie][0],movieDict_new[movie][0])]=1
				Denom[(movieDict_new[key_movie][0],movieDict_new[movie][0])]=totActor

print 'Numer:'%(len(Numer))


for key_edge in Numer:
	numerator = Numer[key_edge]/2
	denominator = Denom[key_edge]-numerator
	weight = 1.0*numerator/denominator
	s = '%d\t%d\t%f\n'%(key_edge[0],key_edge[1],weight)
	m_g.write(s)
print ("Graph has been constructed successfully!")

f.close()
g.close()        
m_g.close()
