#coding=UTF-8
"""
用于上传图片到gitee中，使用gitee作为图床
"""

import base64
import requests
import sys
import os
import jsonpath
import json
# print(os.sep)

url = "https://gitee.com/api/v5/repos/{0}/{1}/contents/{2}"
# print("上传的url路径为: ", url)

# 自己账号的token
access_token = "8a5b58cd187031a2d5816ba3e82d7e92"


# params = {"access_token": access_token, "content": , "message": "test"}

for address in sys.argv[1:]:
    # print(address)
    # 处理输入参数获取文件名称
    # fileName = address[address.rfind(".")+1:]
    # fileName=address[address.rfind(os.sep)+1:]
    fileName=address[address.rfind("/")+1:]
    fileName=fileName[fileName.rfind("\\")+1:]
    #获取base64编码
    base64_str = ""
    with open(address, "rb") as f:
        base64_str= base64.b64encode(f.read());
        f.close()
    
    parms = {"access_token": access_token, "content": base64_str, "message": "this is a pic!"}
    formatUrl = url.format("linqin07", "pic-bed", fileName)
    response = requests.post(formatUrl, parms)
    # print(response.text)

    jsonStr = json.loads(response.text)
    
    # json取值,取第一个值，jsonpath返回的一定是一个数组
    download_url = jsonpath.jsonpath(jsonStr, "$.content.download_url")
    print(download_url[0])




    

    

