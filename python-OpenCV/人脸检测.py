import cv2
import argparse
import numpy as np
# import matplotlib.pyplot as plt
# from faceDetector import FaceDetector
from scipy.misc import imresize

# https://github.com/opencv/opencv 人脸分类器的下载地址
image = cv2.imread('./img/wulinwaizhuan.jpg')  # ./img/img_man.jpg #family_portrait_photograph.jpg  wulinwaizhuan.jpg
image = imresize(image,[700,1200])  #调整图像到最正位置
image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image1.shape)

# 欧美人使用分类器 ： default  亚洲人分类器 alt2

classifier = './data/haarcascades/haarcascade_frontalface_alt2.xml'   #'./data/haarcascades/haarcascade_frontalface_alt2.xml'
# classifier1 = './data/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(classifier)


#探测图片中的人脸
faces = face_cascade.detectMultiScale(image)

print("发现{0}个人脸!".format(len(faces)))
print(faces)
data = [None]*len(faces)
for i in range(len(faces)):
   g = faces[i]
   for[x,y,w,h] in [g]:
      # cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
      cv2.circle(image,(x+w//2,y+h//2),w//2,(255,0,255),2)
      font = cv2.FONT_HERSHEY_SIMPLEX
      cv2.putText(image, 'people-%d'%i, (x-5, y-10), font, 0.6, (255,255,240), 1, cv2.LINE_AA)
      # mg = imresize(image[y:(y+h), x:(x+w), :],[28,28])
      # cv2.imshow('img%d'%(i), mg)  #把每个脸提取出来

      # data[i] = imresize(image[y:(y+h), x:(x+w), :],[28,28])

cv2.imshow('Image Title', image)

# d = np.array(data)
# print(d[0].shape)
# print(mg.shape)
cv2.waitKey()
