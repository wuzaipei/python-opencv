# coding:utf-8

# one

import os
import cv2

def paizhao(image_cache,img_name):
    img =0
    cap = cv2.VideoCapture(0)
    while(True):
        # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture%s"%img_name, frame)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            img = frame
            break
    cap.release()
    cv2.destroyAllWindows()
    return img



def Login_System(img_name,path_cache='image_cache/'):
    img = paizhao(path_cache, img_name)
    cv2.imwrite(path_cache + img_name + '.jpg', img)
    #调用封装好的识别方法
    from face_contrast import face_Contrast
    n = 1
    path = 'image_database/'
    path_file = os.listdir(path)
    # print(path_file)
    if path_file==[]:
        print('查无此人')
    else:
        for i in path_file:
            credibility = face_Contrast(path_cache + img_name + '.jpg', path + i)
            print(credibility)
            if credibility > 85.00:
                print('成功登录,可信度为：%d' % credibility)
                # break
            elif n == len(path_file):
                print('你没有注册！')



def Registration_system(img_name,path_cache='./image_cache/'):
    img = paizhao(path_cache, img_name)
    cv2.imwrite(path_cache + img_name + '.jpg', img)

    from face_contrast import face_Contrast

    path = 'image_database/'
    path_file = os.listdir(path)
    n = 1
    if path_file==[]:
        cv2.imwrite(path + img_name + ".jpg", img)
        print('成功注册，孩子！快去登录吧！')
    else:
        for i in path_file:
            n+=1
            credibility = face_Contrast(path_cache + img_name + '.jpg', path + i)
            if credibility > 85:
                print('你已经注册过了，请不要重复注册，OK？,可信度为：%d' % credibility)
                break

            elif n == len(path_file):
                cv2.imwrite(path + img_name + ".jpg", img)
                print('成功注册，孩子！快去登录吧！')



# 注册
Registration_system(img_name='wuzaipei')   #注册系统 按空格键点击注册、
# 登录
Login_System(img_name='wzp')   #登录系统  按空格键点击登录
