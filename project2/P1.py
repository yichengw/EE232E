# -*- coding: utf-8 -*-
"""
Created on Mon May 23 16:34:17 2016

@author: Yicheng
"""
##### PROBLEM 1#####
import re
a1 = open('./project_2_data/actor_movies.txt','r')
a2 = open('./project_2_data/actress_movies.txt','r')
a3 = open('./project_2_data/act_combine.txt','w')

for line in a1.readlines():
    a3.write(str(line))
for line in a2.readlines():
    a3.write(str(line))
a1.close()
a2.close()
a3.close()    
print("actor and actress file has been combined successfully ...")   
 
a3 = open('./project_2_data/act_combine.txt','r')
a4 = open('./project_2_data/act_process.txt','w')

split = '\t\t'
mycount = 0

for line in a3.readlines():
	if(line.count(split)>=5):
		print "line %d has %d movies" % (mycount, line.count(split))
		a4.write(str(line))
	mycount+=1

a3.close()
a4.close()
print("remove all actors/actresses with less than 5 movies successfully ...")

f = open("./project_2_data/act_process.txt","r")
g = open("./project_2_data/movie_genre.txt","r")
a_g = open("./project_2_data/act_graph.txt","w")
#m_g = open("./project_2_data/movie_graph.txt","w")

print("open all the files successfully ...")


actDict={}  #key: actname #value:actId and movies he/she attended
movieDict={}    #key: movie; value: actor/actress in this movie


movieId=0
for line in g.readlines():
	tokens = line.split("\t\t")
	movieDict[tokens[0]]=[movieId]
	movieId = movieId + 1
print("movie dictionary has been initialized successfully! Movie quantity: %d!"%(len(movieDict)))

"""
actor_movies.txt
contains movies each actor has played in:

{actor1}\t\t{movie1}\t\t{movie2}\t\t{movie3}...
{actor2}\t\t{movie1}\t\t{movie2}\t\t{movie3}...
"""  
actId=0
for line in f.readlines():
    tokens = line.split("\t\t")
    actorName = tokens[0]
    tokens[0] = actId
    
    for i in range(1, len(tokens)):
        movie = tokens[i]
        year = re.search(r'\(\d\d\d\d\)|\(\?\?\?\?\)',movie)
        #if movie != "":
        if year:
            end=movie.find(year.group())
            tokens[i]=movie[:end+6]
        
        if movieDict.has_key(tokens[i]):
            movieDict[tokens[i]].append(actorName)
        else:
            movieDict[tokens[i]]=[len(movieDict)]
            movieDict[tokens[i]].append(actorName)
    actDict[actorName] = tokens
    if actId%5000==0:
        print("construct actDict: %d"%(actId))
    actId = actId + 1
print ("actDict has been written successfully! Actors/actresses quantity: %d"%(len(actDict)))
print ("movieDict have been written successfully! Movie quantity: %d"%(len(movieDict)))

##### PROBLEM 2 #####
edgeAct = {}
count = 0
for key in actDict:
    for i in range(1,len(actDict[key])):
        movie = actDict[key][i]
        for act in movieDict[movie]:
            #skip the actor/actress him/herself, and connect all the other
            #actors/actress in the edgeAct
            if act == key or isinstance(act,int):
                continue;
            if edgeAct.has_key((actDict[key][0],actDict[act][0])):
                edgeAct[(actDict[key][0],actDict[act][0])] = edgeAct[(actDict[key][0],actDict[act][0])] + 1.0/(len(actDict[key])-1)
            else:
                edgeAct[(actDict[key][0],actDict[act][0])] = 1.0/(len(actDict[key])-1)
    if count%1000 == 0:
        print("construct edgeAct: %d"%(count))
    count = count +1
print("edgeAct has been construct successfully with %d records!"%(len(edgeAct)))

#write to file
count = 0
for key in edgeAct:
    s = '%d\t%d\t%f\n'%(key[0],key[1],edgeAct[key])
    a_g.write(s)
    if count%10000==0:
        print ("write to file graphAct: %d"%(count))
    count=count + 1

print("Act graph has been written successfully!")       
f.close()
g.close()
a_g.close()
#m_g.close()