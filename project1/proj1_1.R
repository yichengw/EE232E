############## PROBLEM 1 #############
library('igraph')
library('netrw')
library('ggplot2')

#read file
# May be changed according to the directory of the file
fileDir = "O:/UCLA 16S/232E Graphs and Network Flow/project1/facebook_combined.txt"

# Generate the graph from the file
g = read.graph(file = fileDir , format = "ncol", directed = F)

#Check connectivity
Connectivity = is.connected(g)
#diameter
d <- diameter(g)
#degree distribution
dd <-degree.distribution(g)
deg = degree(g)
plot(dd,type = "h", main = "Facebook Graph Degree Distribution",xlab = "degree", ylab = "density")


# a smattering of possible models
r <- hist(degree(g), breaks=seq(0, by=1 , length.out=max(deg)+1))
dat_r = data.frame(x=r$mids, y=r$density)
models<-list(lm(y ~ log(x),data = dat_r),
             nls(y ~ I(1/x*a) + b*x, data = dat_r, start = list(a = 1, b = 1)),
             nls(y ~ I(exp(1)^(a + b * x)), data = dat_r, start = list(a=0,b=0)),
             nls(y ~ I(1/x*a)+b, data=dat_r, start = list(a=1,b=1)))
# have a quick look at the visual fit of these models
ggplot(dat, aes(x, y)) + geom_point(size = 1)+
  stat_smooth(method = "lm", formula = as.formula(models[[1]]), size = 1, se = FALSE, colour = "red")+
  stat_smooth(method = "nls", formula = as.formula(models[[2]]), data=dat_r, start = list(a=0,b=0), size = 1, se = FALSE, colour = "blue")+
  stat_smooth(method = "nls", formula = as.formula(models[[3]]), data=dat_r, start = list(a=0,b=0), size = 1, se = FALSE, colour = "yellow")+
  stat_smooth(method = "nls", formula = as.formula(models[[4]]), data=dat_r, start = list(a=0,b=0), size = 1, se = FALSE, colour = "orange")
#after a quick look we find models[[3]] is the best
summary(models[[3]])
#model: y=exp(1)^(-3.594_0.029*x)
dat_f = data.frame(x=r$mids, y=exp(1)^(-3.594-0.029*r$mids))
MSE=sum((dat_r$y-dat_f$y)^2)/max(deg)
d_average = mean(deg)
