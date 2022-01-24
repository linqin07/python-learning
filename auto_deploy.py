from fabric.api import run  
from collections.abc import Mapping

# 导入api中的run
def look():     
     run('uname -o')        # 执行run函数，把用使用的命令传入