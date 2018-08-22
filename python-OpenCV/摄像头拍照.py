import cv2

from scipy.misc import imresize

cap = cv2.VideoCapture(0)
while(True):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        cv2.imwrite("./img/zipai.jpeg", frame)
        break
cap.release()
cv2.destroyAllWindows()


image = cv2.imread('./img/zipai.jpeg')  # ./img/img_man.jpg #family_portrait_photograph.jpg  wulinwaizhuan.jpg
image = imresize(image,[750,1000])
# image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# print(image1.shape)

# 欧美人使用分类器 ： default  亚洲人分类器 alt2

classifier = './data/haarcascades_cuda/haarcascade_frontalface_alt2.xml'   #'./data/haarcascades/haarcascade_frontalface_alt2.xml'
face_cascade = cv2.CascadeClassifier(classifier)

#探测图片中的人脸
faces = face_cascade.detectMultiScale(image)
print(faces)
print("发现{0}个人脸!".format(len(faces)))

for(x,y,w,h) in faces:
   cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
   # mg = image[y:(y+h), x:(x+w), :]

cv2.imshow('Image Title', image)


# cv2.imshow('rl', mg)

# print(mg.shape)


cv2.waitKey()
