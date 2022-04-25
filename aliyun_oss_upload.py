# -*- coding: utf-8 -*-
import oss2
import os
# 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
auth = oss2.Auth('LTAI5t8nGF3qeirDtC8yvMTV', 'o6QR1rnz6MUGR9KVKFhqzNPccx8m8G')
# yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
# 填写Bucket名称。
bucket = oss2.Bucket(auth, 'https://blog-07.oss-cn-guangzhou.aliyuncs.com', 'blog-07')

   


    # 填写Object完整路径和本地文件的完整路径。Object完整路径中不能包含Bucket名称。
# 如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
bucket.put_object_from_file('exampleobject.txt', 'C:\\Users\\LinQin\\Desktop\\qq.png')            