# _*_ coding:utf_8 _*_

import cv2
import matplotlib.pyplot as plt

discern_model = cv2.face.LBPHFaceRecognizer_create()
discern_model.read('video/trainer.yml')

classifier = 'data/haarcascades/haarcascade_frontalface_default.xml'
detection_model = cv2.CascadeClassifier(classifier)

data = plt.imread('人脸识别登录系统模拟/image_database/lixiaol.jpg')

data_gray = cv2.cvtColor(data,cv2.COLOR_RGB2GRAY)
data_len = detection_model.detectMultiScale(data)
x_train = 0
for x,y,w,h in data_len:
    x_train = data_gray[y:(y+h),x:(x+w),]

    cv2.rectangle(data_gray, (x, y), (x + w, y + h), (0, 255, 0), 2)

# plt.imshow(x_train,cmap='gray')
# plt.xticks([]),plt.yticks([])
# plt.show()

label,score = discern_model.predict(x_train)

print(label,100-score)
