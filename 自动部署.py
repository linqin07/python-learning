from fabric.api import run  # 导入api中的run
      
def look():     
     result = run('ls')        # 执行run函数，把用使用的命令传入
     print(result)

print(look())