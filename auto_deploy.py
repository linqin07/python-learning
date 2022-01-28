from fabric.api import *
import time
import os
import sys

# 设置目标主机
env.hosts = ['192.168.233.128']
# 设置多台主机用户名及密码
env.passwords = {'root@192.168.233.128:22': '123456'}
env.user = "root"

path = "F:\\youcai\\"
uploadPath ="/data/uploadPath/"


def start():
    run('mkdir test')


# 设置一个任务

def upload():
    print("检查本地环境")
    local("java -version")
    print("java 环境正常")
    local("mvn -v")
    print("maven 环境正常")


def tar():
    print("打包tar 路径 path:", path)
    with lcd(path):
        local('tar cf  package.tar .')

def upload():
    run("mkdir -p " + uploadPath)
    print("开始上传包, 上传路径为 ", uploadPath)
    put(path + "package.tar", uploadPath + "package.tar")

# 解包并执行
def task_exc():
    with cd(uploadPath):
        run('tar xf package.tar')

@task
def start():
    tar()
    upload()
    task_exc()
