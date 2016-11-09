library("igraph")
#modify this filePath to locate the facedgebetweenook_combined.txt
filePath = "C:/Users/Gaoxiang/Desktop/232E/PROJ1/facebook_combined.txt"
g = read.graph(file = filePath,directed=FALSE)

##########
#Problem 2
g_node_no1 = induced.subgraph(g, c(1, neighbors(g,1)))
vertex_vector = rep(4,vcount(g_node_no1))
vertex_vector[1]=6
vertex_color = rep("skyblue1",vcount(g_node_no1))
vertex_color[1] ="black"
plot.igraph(g_node_no1,vertex.size=vertex_vector,vertex.label =NA,vertex.color=vertex_color)
num_node = vcount(g_node_no1)
num_edge = ecount(g_node_no1)

##########
#Problem 3
core_index = numeric(0)
core_degree = numeric(0)
for(i in 1: vcount(g)){
  if(length(neighbors(g,i))>200){
    core_index = c(core_index, i)
    core_degree = c(core_degree, length(neighbors(g,i)))
  }
}
core_ave_degree = mean(core_degree)
print(core_index)
print(core_ave_degree)
fastgreedy = fastgreedy.community(g_node_no1)
color_vector = fastgreedy$membership+1
t=fastgreedy$membership+1
vertex_vector = rep(4,vcount(g_node_no1))
vertex_vector[1]=6
print(modularity(fastgreedy))
plot(fastgreedy,g_node_no1,vertex.color=color_vector,vertex.label=NA,vertex.size=vertex_vector)
edgebetween = edge.betweenness.community(g_node_no1)
color_vector = edgebetween$membership+1
print(modularity(edgebetween))
plot(g_node_no1,vertex.color=color_vector,vertex.label=NA,vertex.size=vertex_vector)
infomap = infomap.community(g_node_no1)
color_vector = infomap$membership+1
print(modularity(infomap))
plot(g_node_no1,vertex.color=color_vector,vertex.label=NA,vertex.size=vertex_vector)
hist(fastgreedy$membership, col="red", main="Community structure using Fast-Greedy Algorithm", xlab="Community number", ylab="Number of nodes")
hist(edgebetween$membership, col="blue", main="Community structure using Edge-Betweenness Algorithm", xlab="Community number", ylab="Number of nodes")
hist(infomap$membership,col="yellow",main="Community structure using Infomap Algorithm",xlab="Community number",ylab="Number of nodes")

##########
#Problem 4
g_node_no1_removed = induced.subgraph(g,neighbors(g,1))

fastgreedy_r = fastgreedy.community(g_node_no1_removed)
color_vector = fastgreedy_r$membership+1
plot(g_node_no1_removed, vertex.color=color_vector, vertex.label=NA, vertex.size=4)
edgebetween_r = edge.betweenness.community(g_node_no1_removed)
color_vector = edgebetween_r$membership+1
plot(g_node_no1_removed, vertex.color=color_vector,vertex.label=NA, vertex.size=4)
infomap_r = infomap.community(g_node_no1_removed)
color_vector = infomap_r$membership+1
plot(g_node_no1_removed, vertex.color=color_vector,vertex.label=NA, vertex.size=4)
hist(fastgreedy_r$membership, col="red", main="Community structure using Fast-Greedy Algorithm", xlab="Community number", ylab="Number of nodes")
hist(edgebetween_r$membership, col="blue", main="Community structure using Edge-Betweenness Algorithm", xlab="Community number", ylab="Number of nodes")
hist(infomap_r$membership,col="yellow",main="Community structure using Infomap Algorithm",xlab="Community number",ylab="Number of nodes")
print(modularity(fastgreedy_r))
print(modularity(edgebetween_r))
print(modularity(infomap_r))