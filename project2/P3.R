library('igraph')
#read file
# May be changed according to the directory of the file
fileDir = "O://UCLA 16S/232E Graphs and Network Flow/final project/project_2_data/act_graph.txt"
# Generate the graph from the file
g = read.graph(file = fileDir , format = "ncol", directed = T)
pr = page.rank(g, directed = TRUE, damping = 0.85)
pr_sort = sort(pr$vector, decreasing = TRUE, index.return = TRUE)
print(pr_sort$ix[1:10])
print(pr_sort$x[1:10])


# write actor/actress id and its pagerank to a list
prlist = list()
for (i in 1:length(pr$vector)){
  key = names((pr$vector)[i])
  #key = as.numeric(key)
  value = as.numeric((pr$vector)[i])
  prlist[[key]] = value
  if( i %% 1000 == 0){
    print(i)
  }
}
#print(prlist[2])
#print(pr$vector[1])


filecon = file("O://UCLA 16S/232E Graphs and Network Flow/final project/project_2_data/top10.txt")
top10_id = numeric(0)
for (i in 1:10){
  top10_id = c(top10_id, as.character(names(pr_sort$x[i])))
}
print(top10_id)
writeLines(top10_id, filecon, sep = "\n")
close(filecon)

#print the top10 pageranks 
for (i in 1: length(top10_id)){
  print(prlist[[top10_id[i]]])
}

#print (one of) my top10 favorite movie star
print(prlist[["116087"]])


#prlist1 = list()
#key = "1"
#value = "Hello"
#prlist1[[key]] = value

#print(as.numeric(names(prlist1[1])))


#write prlist to file 
filecon1 = file("O://UCLA 16S/232E Graphs and Network Flow/final project/project_2_data/prlist.txt","w")
for ( i in 1: length(prlist)){
  key = as.numeric(names(prlist[i]))
  writeLines(key,filecon1,sep="\t\t")
  writeLines(as.numeric(prlist[[key]]),con=filecon1,sep ="\n")
}
close(filecon1)
