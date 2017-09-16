# -*- coding: cp936 -*-
from numpy import *


#����������ݣ���̨����ʱ��Ϊ�������Է���õ�������
m=200;n=20
X=random.rand(m,n)

#�������������һ����ŷ�Ͼ���
def Dist(v1,v2):
    return sqrt(sum(power(v2 - v1, 2)))

#k-means����
#��ʼ��
k=5
centers=zeros((k,n))
for i in range(k):
    index = int(random.uniform(0, m))
    centers[i,:]=X[index,:]

clusterAssment = mat(zeros((m, 2)))
clusterChanged = True

#��ʼ����
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
        ��Ϊ�ֲ�ʽ�汾�����ÿһ̨��������¼�¸û��������ݶ�Ӧ��������centers[j, :]��ÿһ���е���������pointsInCluster.shape[0],
        ��������������Ϊһ��pair���ͳ�ȥ�������������϶�Ӧ��pair���ܲ����¼��㣬�ó�ȫ�����������ص����ģ����ͻظ������������Ը��������ж�Ӧ��
        centers[j, :]���и��¡�����Ĵ����뵥��ʽ����ȫ��ͬ��
        '''


print 'Done'















        
