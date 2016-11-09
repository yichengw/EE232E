m_rating = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/movie_rating.txt","r")
m_ID = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/MoiveID.txt","r")
ID_R = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/IDRating.txt","w")

ratingDict={}
for lines in m_rating.readlines():    
    tokens=lines.split("\t\t")    
    ratingDict[tokens[0].replace('\n','')]=tokens[1].replace('\n','')
print (ratingDict[tokens[0]])
print (tokens[0])
idDict={}
for lines in m_ID.readlines():
    tokens=lines.split("\t")
    idDict[tokens[0].replace('\n','')]=tokens[1].replace('\n','')

print (idDict[tokens[0]])

for movie in idDict:
    if movie in ratingDict:
        s='%s\t%s\n'%(str(idDict[movie]),str(ratingDict[movie]))
        ID_R.write(s)
m_rating.close()
m_ID.close()
ID_R.close()