# -*- coding: utf-8 -*-
"""
Created on Wed Jun 08 00:33:50 2016

@author: Yicheng
"""

import re
f = open("./project_2_data/act_process.txt","r")
g = open("./project_2_data/movie_genre.txt","r")
h = open("./project_2_data/target_rating.txt","r")
print("open files successfully..")

actDict={}  #key: actname; value:actId and movies he/she attended
movieDict={}    #key: movie; value: movieId actor/actress in this movie

#build movie dictionary and act dictionary
movieId=0
for line in g.readlines():
	tokens = line.split("\t\t")
	movieDict[tokens[0]]=[movieId]
	movieId = movieId + 1
print("movie dictionary has been initialized successfully! Movie quantity: %d!"%(len(movieDict)))

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

#build a dictionary of movie rating we got in problem 8
movieRatingDict = {}
for line in h.readlines():
    tokens = line.split("\t")  
    movieRatingDict[tokens[0]] = tokens[1]
print("movie rating dictionary has been initialized successfully! Movie quantity: %d!"%(len(movieRatingDict)))

actScoreDict = {}
count = 0
for key in actDict:
    score = 0
    num = 0
    #for all the movies this actor acted
    for i in range(1,len(actDict[key])):
        movie = actDict[key][i]
        movieId = movieDict[movie][0]
        if str(movieId) in movieRatingDict:   
            #get the score of this movie                
            score = score + float(movieRatingDict[str(movieId)])
            num = num + 1
    if num == 0:
        av_score = 0
    else:
        av_score = score/num
    

    actScoreDict[key] = av_score
    if count%5000 == 0:
        print("construct actScoreDict: %d"%(count))
        #print(av_score)
    count=count + 1
    
print("Act score has been written successfully!")  

#predict the rating of the 3 new movies
#movieId: 894353 779750 763762
for movie in movieDict:
    if movieDict[movie][0] == 894353:
        score = 0        
        lnum = 0
        mnum = 0
        starnum = 0
        for i in range(1,len(movieDict[movie])):
            actname = movieDict[movie][i]
            actscore = actScoreDict[actname]
            if actscore != 0:
                if actscore > 7:
                    score = score + 10*actscore                    
                    starnum = starnum + 1
                elif actscore <= 7 and actscore > 5.5:
                    score = score + 3*actscore 
                    mnum = mnum + 1
                else:
                    score = score + actscore 
                    lnum = lnum + 1
        av_score = score/(lnum + 3*mnum + 10*starnum)
        print("The predicted rating of movie: Batman v Superman: Dawn of Justice (2016) is %f"%(av_score))
    elif movieDict[movie][0] == 779750:
        score = 0        
        lnum = 0
        mnum = 0
        starnum = 0
        for i in range(1,len(movieDict[movie])):
            actname = movieDict[movie][i]
            actscore = actScoreDict[actname]
            if actscore != 0:
                if actscore > 7:
                    score = score + 10*actscore                    
                    starnum = starnum + 1
                elif actscore <= 7 and actscore > 5.5:
                    score = score + 3*actscore 
                    mnum = mnum + 1
                else:
                    score = score + actscore 
                    lnum = lnum + 1
        av_score = score/(lnum + 3*mnum + 10*starnum)
        print("The predicted rating of movie: Mission: Impossible - Rogue Nation (2015) is %f"%(av_score))
    elif movieDict[movie][0] == 763762:
        score = 0        
        lnum = 0
        mnum = 0
        starnum = 0
        for i in range(1,len(movieDict[movie])):
            actname = movieDict[movie][i]
            actscore = actScoreDict[actname]
            if actscore != 0:
                if actscore >7:
                    score = score + 10*actscore                    
                    starnum = starnum + 1
                elif actscore <= 7 and actscore > 5.5:
                    score = score + 3*actscore 
                    mnum = mnum + 1
                else:
                    score = score + actscore 
                    lnum = lnum + 1
        av_score = score/(lnum + 3*mnum + 10*starnum)

        print("The predicted rating of movie: Minions (2015) is %f"%(av_score))

f.close()
g.close()
h.close()