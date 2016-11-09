library("igraph")
filePath = "C:/Users/Gaoxiang/Desktop/232E/PROJ1/facebook_combined.txt"
g = read.graph(file = filePath,directed=FALSE)

#Find all the core node
core_index = numeric(0)
core_degree = numeric(0)
for(i in 1: length(degree(g))){
  if(length(neighbors(g,i))>200){
    core_index = c(core_index, i)
    core_degree = c(core_degree, length(neighbors(g,i)))
  }
}
V(g)$name = V(g)

#Begin calculating embeddedness and dispersion
embeddedness_tot=numeric(0)
dispersion_tot=numeric(0)
for(i in 1:length(core_index))
{
  #i=1,3,4
  
  #For embeddedness
  embeddedness=numeric(0)
  core_neighbors =neighbors(g,core_index[i])
  core_network = induced.subgraph(g,c(core_index[i],core_neighbors))
  for(j in 1:length(core_neighbors))
  {
    embeddedness =c(embeddedness,length(intersect(neighbors(g,core_index[i]),neighbors(g,core_neighbors[j]))))
  }
  
  #For dispersion
  dispersion = numeric(0)
  for(k in 1: length(core_neighbors))
  {
    mutual_friends = intersect(neighbors(g,core_index[i]),neighbors(g,core_neighbors[k]))
    dispersion_subgraph = delete.vertices(core_network,c(which(V(core_network)$name==core_index[i]),which(V(core_network)$name==core_neighbors[k])))
    shortestpath=numeric(0)
    for(m in 1:length(mutual_friends))
    {
      for(n in (m+1): length(mutual_friends))
      {
        shortestpath = c(shortestpath,shortest.paths(dispersion_subgraph,which(V(dispersion_subgraph)$name==mutual_friends[m]),which(V(dispersion_subgraph)$name==mutual_friends[n])))
      }
    }
    dispersion = c(dispersion, sum(shortestpath))
  }
  
  #Sum embeddedness and dispersion
  embeddedness_tot=c(embeddedness_tot,embeddedness)
  dispersion_tot=c(dispersion_tot,dispersion)
  
  #Find the index for max-dispersion max-embeddedness and max disper/embedded
  max_dispersion = which.max(dispersion)
  max_embeddedness = which.max(embeddedness)
  max_dispersion_embeddedness = which.max(dispersion*(1/embeddedness))
  
  #For plotting
  core_community = walktrap.community(core_network)
  color_vec = core_community$membership+1
  size_vec = rep(4,length(color_vec))
  color_vec[max_embeddedness[1]] = 0
  size_vec[max_embeddedness[1]] = 6
  color_vec[which(V(core_network)$name==core_index[i])] = 0
  size_vec[which(V(core_network)$name==core_index[i])] = 8
  E(core_network)$color = "grey"
  E(core_network,P = c(max_embeddedness[1],which(V(core_network)$name==core_index[i])))$color = "yellow"
  E(core_network,P = c(max_embeddedness[1],which(V(core_network)$name==core_index[i])))$width = 8
#  plot(core_network,vertex.color=color_vec,vertex.label=NA,vertex.size=size_vec)

}
hist(embeddedness_tot,breaks=50,main = "Embeddedness Distribution",xlab = "Embeddedness", col="red")
hist(dispersion_tot[which(dispersion_tot!=Inf)],breaks = 100,main = "Dispersion Distribution",xlab = "Dispersion")