library("igraph")
#import the graph
filePath = "E:/UCLA/Courses/2016 SPRING/EE232E/EE232EPRO2/movie_graph.txt"
g = read.graph(file = filePath ,format = "ncol",directed = F)
print("The graph reading has been finished")

#Add the movie using its movie ID
#Movie Id is found using generated MoiveID.txt
MovieID = c(894353,779750,763762)

for (mid in MovieID){
  #Locate movie in the graph
  movie_idx = which(V(g)$name == mid)
  
  #Find the neighbor of the movie
  neighbor_node_set = neighbors(g,movie_idx)
  
  #Find the five nearest movie according to the weight
  neighbor_weight_set=numeric(0)
  for (neighbor_node in neighbor_node_set){
    #print(nei_node)
    neighbor_weight_weight = E(g,P=c(movie_idx,neighbor_node))$weight
    neighbor_weight_set = c(neighbor_weight_set,neighbor_weight_weight)
  }
  weight_set_inorder = sort(neighbor_weight_set,decreasing =T,index.return =T)
  near_neighbor_idx = neighbor_node_set[weight_set_inorder$ix[1:5]]
  near_neighbor_id = V(g)[near_neighbor_idx]
  
  cat("Added Movie: ",mid,"\n")
  cat("Neighbor MovieID: ",V(g)[near_neighbor_id]$name,"\n")
  cat("Neighbor Community: ",g_movie_com$membership[near_neighbor_id],"\n")
}

