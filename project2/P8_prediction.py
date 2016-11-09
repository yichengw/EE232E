# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 00:34:51 2016

@author: Gaoxiang
"""
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn import cross_validation
from sklearn import linear_model
import statsmodels.api as sm

import math
t_feature = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/feature_pagerank.txt","r")
t_target = open("C:/Users/Gaoxiang/Desktop/232E/PROJ2/project_2_data/target_rating.txt","r")
test_feature=np.load('test_feature.npy')
print(test_feature)
test_feature=test_feature[:,1:]
test_feature[0,7]=0
test_feature[1,7]=1
test_feature[2,7]=0
print(test_feature)
pagerank_1=[]
pagerank_2=[]
pagerank_3=[]
pagerank_4=[]
pagerank_5=[]
sumPage=[]
avePage=[]
isTop100=[]
target=[]
for lines in t_feature.readlines():
    tokens=lines.split("\t")
    pagerank_1.append(float(tokens[1]))
    pagerank_2.append(float(tokens[2]))
    pagerank_3.append(float(tokens[3]))
    pagerank_4.append(float(tokens[4]))
    pagerank_5.append(float(tokens[5]))
    sumPage.append(float(tokens[6]))
    avePage.append(float(tokens[7]))
    isTop100.append(float(tokens[8]))

for lines in t_target.readlines():
    tokens=lines.split("\t")
    target.append(float(tokens[1]))

X=[pagerank_1,pagerank_2,pagerank_3,pagerank_4,pagerank_5,sumPage,avePage,isTop100]
X=np.asarray(X)
X=np.asarray(X).T
Y=np.asarray(target)
#regressor = RandomForestRegressor(n_estimators=40, max_features=6, max_depth=10)
#regressor.fit(X,Y)
#y_predict=regressor.predict(test_feature)
print(sm.OLS(Y, X).fit().summary())

lr = linear_model.LinearRegression()
lr.fit(X,Y)
y_predict = lr.predict(test_feature)
test_target=[6.4,7.5,7.0]
error=(sum(y_predict)-sum(test_target))/3
print(y_predict)
scores=cross_validation.cross_val_score(lr,X,Y,cv=10, scoring='mean_squared_error')
y_predict=cross_validation.cross_val_predict(lr,X,Y,cv=10)
rmse=math.sqrt(-np.mean(scores))
print(rmse)

t_feature.close()
t_target.close()