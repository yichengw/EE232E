# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 14:03:46 2016

@author: Gaoxiang
"""
import re
import numpy as np
p_r = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/prlist.txt","r")
f = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/processedAct.txt","r")
g = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/movie_genre.txt","r")
di = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/director_movies.txt","r")
top = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/top100.txt","r")
feature_pr = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/feature_pagerank.txt","w")
r = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/movie_rating.txt","r")
target_rating = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/target_rating.txt","w")
test_feature= open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/test_feature.txt","w")
print("open all the files successfully ...")

actorDict={}
movieDict={}


#building movie dictionary, key=movie name
mId=0
for line in g.readlines():
	tokens = line.split("\t\t")
	movieDict[tokens[0]]=[mId]
	mId+=1
  
print ("movie:%d"%(mId))

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
    actorDict[actName] = tokens[0]
    actId = actId + 1
print ("actor:%d"%(actId))

#building top 100 dictionary, key=movie name
topDict={}
#countTop={}
count=0
for lines in top.readlines():
    tokens=lines.split("\t")
    topDict[tokens[0]]=tokens[1]    
#    countTop[count]=tokens[0]
    count=count+1

#building director dictionary, key=movie ID
directorDict={}
topdirList=[]
movieList=[]
for lines in di.readlines():
    tokens=lines.split("\t\t")
    for i in range(1,len(tokens)):
        if (tokens[i] in movieDict):
            directorDict[movieDict[tokens[i]][0]]=tokens[0]
        if (tokens[i] in topDict):
            topdirList.append(tokens[0])
            movieList.append(tokens[i])
#build top 100 list
for i in range(0,100):
    if countTop[i] not in movieList:
        print(countTop[i])
print ("director:%d"%(len(topdirList)))

#building rating dictionary, key=movie ID
ratingDict={}
for line in r.readlines():
    tokens = line.split("\t\t")
    movie = tokens[0]
    if (movie in movieDict) and(len(movieDict[movie])>5):
        ratingDict[movieDict[movie][0]]=tokens[1]

#building pagerank dictionary, key=actor ID
pagerank_dict={}
count=0
for line in p_r.readlines():
    count=count+1
    tokens = line.split("\t\t")
    pagerank_dict[int(tokens[0])]=float(tokens[1])
    if count%5000==0:
        print("construct pagerank_dict: %d"%(count))

testID=[894353,779750,763762]
testFeature=np.zeros([3,9])
ct=0;

#extract the feature
for movie in movieDict:
    ID=movieDict[movie][0]
    if (ID in testID):
        print("ID:%d"%ID)
        testFeature[ct][0]=ID
        testpr=[]
        print(len(movieDict[movie]))
        for i in range(1,len(movieDict[movie])):
            actor=movieDict[movie][i]
            actorID=actorDict[actor]
            testpr.append(pagerank_dict[actorID])
        testpr=sorted(testpr,reverse=True)
        print(testpr)
        flag=0
        if(ID in directorDict and directorDict[ID] in topdirList):
            flag=1
        testFeature[ct][8]=flag
        testFeature[ct][6]=sum(testpr)
        testFeature[ct][7]=sum(testpr[:10])/10
        for j in range(1,6):
            testFeature[ct][j]=testpr[j-1]
        ct=ct+1
    pagerank=[]
    if(len(movieDict[movie])>5 and ID in ratingDict):
        for i in range(1,len(movieDict[movie])):
            actor=movieDict[movie][i]
            actorID=actorDict[actor]
            pagerank.append(pagerank_dict[actorID])
        pagerank=sorted(pagerank,reverse=True)
        average=sum(pagerank[:10])/10
        sumPage=sum(pagerank)
        flag=0
        if(ID in directorDict and directorDict[ID] in topdirList):
            flag=1
        s = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(str(ID),str(pagerank[0]),str(pagerank[1]),str(pagerank[2]),str(pagerank[3]),str(pagerank[4]),str(sumPage),str(average),str(flag))
        feature_pr.write(s)
        d = '%s\t%s'%(str(ID),ratingDict[ID])
        target_rating.write(d)
np.save('test_feature',testFeature)

p_r.close()
f.close()
g.close()
feature_pr.close()
target_rating.close()
top.close()
di.close()
test_feature.close()