library("igraph")
#import the network
filePath = "C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/movie_graph.txt"
g = read.graph(file = filePath ,format = "ncol",directed = F)
print("The graph reading has been finished")

# add genre information
#import the genre information by line
filePath2 = "C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/movie_genre.txt"
genreFile = file(filePath2,open = "r")
genreByLine = readLines(genreFile)
addGenre = rep("null",vcount(g))
id = 0

for (i in 1:length(genreByLine)){
  if(id %in% V(g)$name){
    genreInfo = strsplit(genreByLine[i],"\t\t")
    movie_idx = which(V(g)$name == id)
    addGenre[movie_idx] = genreInfo[[1]][2]
  }
  id = id + 1
}
close(filePath2)

#Community finding
movie_community = fastgreedy.community(g)

V(g)$genre = addGenre
# tag the communtiy
community_tag_genre = numeric(0)
for (i in 1:length(movie_community)){
  community_genre = V(g)[which(movie_community$membership ==i)]$genre
  max_length = 0
  max_genre_type = "null"
  genre_type_set = unique(community_genre)
  proportion=0
  community_length=0;
  for(genre_type in genre_type_set)
  {
    if(length(which(community_genre == genre_type))>max_length && genre_type!="null")
    {
      max_length = length(community_genre[which(community_genre == genre_type)])
      max_genre_type = genre_type
      community_length=length(community_genre)
      per=length(which(community_genre == genre_type))/community_length
    }
  }
  cat(i,"\t",proportion,"\t",community_length,"\t",max_genre_type,"\n")
  community_tag_genre = c(community_tag_genre,max_genre_type)
}