import fabric.api as api
import time
import os
import sys

# 设置目标主机
api.env.hosts = ['192.168.233.128']
# 设置多台主机用户名及密码
api.env.passwords = {'root@192.168.233.128:22': '123456'}
api.env.user = "root"

path = {"D:\IDEAWorkspace\gitbook"}
uploadPath = {"/data/uploadPath"}


def start():
    api.run('mkdir test')


# 设置一个任务

def upload():
    print("检查本地环境")
    api.local("java -version")
    print("java 环境正常")
    api.local("mvn -v")
    print("maven 环境正常")




def package(path='D:\IDEAWorkspace\gitbook'):
    print("path=", path)
    

#     临时性
    with api.lcd('D:'):
      with api.lcd(r"cd D:\IDEAWorkspace\gitbook"):   
       api.local("dir")
       api.local("mvn clean package -Dmaven.test.skip=true")
