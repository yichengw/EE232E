#####Problem 7##### 

library("igraph")
filePath = "/Users/jtr/Desktop/EE232EPRO1/gplus/"

# Fine all the ego in the data
all_ego = dir(filePath,pattern = "circles")
# Store all ego id
ego_id = list()
# Count the number of users with number of circles > 2
userNum = 0

for (i in 1:length(all_ego)){
    
  #Get the id of ego
  ego_id[[i]] = strsplit(all_ego[i],".circles")
  #Get the path of each edgelist
	edgelist_path = paste(filePath, ego_id[[i]], ".edges" , sep="")
  #Get the path of each circle
	circles_path = paste(filePath, ego_id[[i]] , ".circles" , sep="")
  
  #Get the content of the circle
	open_circle = file(circles_path , open="r")
  lines_in_circle = readLines(open_circle)
  close(open_circle)
  
  #Find the users with more than 2 circles
  if(length(lines_in_circle)>2){
		
		print ("The ID of the user =")
		print(i)
		print("The number of the circle =")
		print (length(lines_in_circle))
		
		circles = list()
    edge_new = c()
		userNum = userNum + 1
		
		g = read.graph(edgelist_path, format = "ncol", directed=TRUE)
		
		for (j in 1:length(lines_in_circle)) {
		  temp = strsplit(lines_in_circle[j],"\t")
		  circles[[j]] = temp[[1]][-1]
    }
		
		#Add the ego node
		gNew = add.vertices(g,1,name=ego_id[[i]])
		for (vidx in 1:(vcount(gNew)-1)) {
		  edge_new = c(edge_new , c(vcount(gNew),vidx))
		}
		gNew = add.edges(gNew,edge_new)
		
		#Extract the community structure
		community_structure = walktrap.community(gNew)
		#community_structure = infomap.community(gNew)
	  
  	#plot(community_structure,gNew,vertex.label=NA,vertex.size=7,edge.arrow.size=0.2,main="Community Structure of No.7 using Walktrap")
		#plot(community_structure,gNew,vertex.label=NA,vertex.size=7,edge.arrow.size=0.2,main="Community Structure of No.7 using Infomap")
		  
    for(m in 1:max(community_structure$membership)){
      
      #Find the common node between community and circle. Then compute the overlap
      community_node = vector()
			for(n in 1:length(community_structure$membership)){
				if(community_structure$membership[n]==m){
				  community_node = c(community_node,(community_structure$name[n]))
				}
			}
      overlap = vector()
			for(n in 1:length(lines_in_circle)){
				common = intersect(community_node,circles[[n]])
				temp2 = length(common)/length(community_node)
				overlap = c(overlap, temp2)
			}
			print(overlap)
	  }	
  }
  
  #If the number of circle <= 2, go to the next
	else 
		next		
}
  
 