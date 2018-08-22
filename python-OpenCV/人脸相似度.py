# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import pandas as pd
pathName = os.listdir('./img_test')

print(pathName)

tuple_img = pd.DataFrame(data=np.zeros((5,10000)),index=[i.split('.')[0] for i in pathName])
for i in pathName:
    tuple_img.loc[[i.split('.')[0]],:] = cv2.cvtColor(plt.imread('./img_test/%s'%i),cv2.COLOR_BGR2GRAY).reshape(1,-1)

print(tuple_img.index[0])

# 夹角余弦
def angle_Cosine(x,y):
    x,y = np.array(x),np.array(y)
    return np.sum(x*y)/np.sqrt(np.sum(x*x)*np.sum(y*y))


# x =np.array([1,2,3])
# y=np.array([3,2,1])
# print(angle_Cosine(x,y))

for i in range(tuple_img.shape[0]-1):
    for j in range(i+1,tuple_img.shape[0]):
        print(tuple_img.index[i],'与',tuple_img.index[j],'相似度为：',angle_Cosine(tuple_img.iloc[i,:],tuple_img.iloc[j,:]))


