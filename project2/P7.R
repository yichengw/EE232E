library("igraph")
MovieID = c(894353,779750,763762)
#import the rating list
ratingFilePath = "C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/IDRating.txt"
ratingFile = file(ratingFilePath, open = "r")
ratingByLine = readLines(ratingFile)
addRating = rep(0,vcount(g))

counter=0
for (i in 1:length(ratingByLine))
  {
    rating_in_one_line = strsplit(ratingByLine[i],"\t")
    movie_idx = which(V(g)$name == rating_in_one_line[[1]][1])
    if(length(movie_idx)!=0)
    {
      counter = counter+1
      addRating[movie_idx] = as.numeric(rating_in_one_line[[1]][2])
    }
  }
close(ratingFile)
V(g)$rating = addRating

for (mid in MovieID)
{
  #Locate movie in the graph
  movie_idx = which(V(g)$name == mid)
  
  #Find the neighbor of the movie
  neighbor_node_set = neighbors(g,movie_idx)
  
  #Find the five nearest movie according to the weight
  neighbor_weight_set=numeric(0)
  for (neighbor_node in neighbor_node_set){
    #print(nei_node)
    neighbor_weight = E(g,P=c(movie_idx,neighbor_node))$weight
    neighbor_weight_set = c(neighbor_weight_set,neighbor_weight)
  }
  weight_set_inorder = sort(neighbor_weight_set,decreasing =T,index.return =T)
  near_neighbor_idx = neighbor_node_set[weight_set_inorder$ix[1:5]]
  near_neighbor_id = V(g)[near_neighbor_idx]
  
  ## rating calculate by nearest neighbors
  cat("Neighbor Rating:",V(g)$rating[near_neighbor_id],"\n")
  neighbor_rating_set = as.numeric(V(g)$rating[near_neighbor_id])
  cat(neighbor_rating_set,"\n")
  print(mean(neighbor_rating_set[which(neighbor_rating_set!=0)]))
}
