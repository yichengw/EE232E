import re
f = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/processedAct.txt","r")
g = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/movie_genre.txt","r")
q=open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/MoiveID.txt","w")
print("open all the files successfully ...")

actDict={}
movieDict={}

movieId=0
for line in g.readlines():
	tokens = line.split("\t\t")
	movieDict[tokens[0]]=movieId
	movieId+=1
print("movie dictionary has been initialized successfully with length %d!"%(len(movieDict)))
for key in movieDict:
	s = '%s\t%s\n'%(key,str(movieDict[key]))
	q.write(s)
print 'newMovieDict has loaded successfully with length %d'%(len(movieDict))
f.close()
g.close()
q.close()