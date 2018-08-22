# coding:utf-8
import requests
from json import JSONDecoder

def face_Contrast(img1_path,img2_path):

    faceId1 = img1_path
    faceId2 = img2_path
    # face++ API的调用方法
    compare_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
    key = "5Ut_EUtu3dG8Q60UBQdj8_LICgc4KByR"    #调用自己的face++ API
    secret = "cWXtsKOMx62m8zHUx810MG-0oGoOnhSO"
    data = {"api_key": key, "api_secret": secret}

    files = {"image_file1": open(faceId1, "rb"), "image_file2": open(faceId2, "rb")}

    response = requests.post(compare_url, data=data, files=files)

    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    # print(req_dict)
    # 置信度，越高说明越像
    confindence = req_dict['confidence']
    return confindence


# print(face_Contrast('image_cache/wuzaipei_1.jpg','image_database/wuzaipei.jpg'))