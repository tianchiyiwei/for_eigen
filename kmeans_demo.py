# -*- coding: cp936 -*-
from numpy import *


#随机生成数据，多台机器时则为机器各自分配得到的数据
m=200;n=20
X=random.rand(m,n)

#定义度量方法，一般用欧氏距离
def Dist(v1,v2):
    return sqrt(sum(power(v2 - v1, 2)))

#k-means方法
#初始化
k=5
centers=zeros((k,n))
for i in range(k):
    index = int(random.uniform(0, m))
    centers[i,:]=X[index,:]

clusterAssment = mat(zeros((m, 2)))
clusterChanged = True

#开始聚类
while clusterChanged: 
    clusterChanged = False
    for i in xrange(m):
        minDist  = 100000.0
        minIndex = 0

        for j in range(k):
            distance = Dist(centers[j, :], X[i, :])
            if distance < minDist:
                minDist  = distance
                minIndex = j

        if clusterAssment[i, 0] != minIndex:
            clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist**2

    for j in range(k):
        pointsInCluster = X[nonzero(clusterAssment[:, 0].A == j)[0]]
        centers[j, :] = mean(pointsInCluster, axis = 0)
        '''
        若为分布式版本，则对每一台机器，记录下该机器中数据对应的类中心centers[j, :]和每一类中的样本个数pointsInCluster.shape[0],
        将这两个数据作为一个pair发送出去。将各个机器上对应的pair汇总并重新计算，得出全部样本各个簇的中心，发送回各个机器，并对各个机器中对应的
        centers[j, :]进行更新。其余的代码与单机式的完全相同。
        '''


print 'Done'















        
