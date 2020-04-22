import os
from git.repo import Repo

# 拉取git上的代码
def pullcode():
    # 创建本地路径用来存放远程仓库下载的代码
    download_path = os.path.join('NB')
    # 拉取代码
    Repo.clone_from('http://github.com/jinge324/test.git', to_path=download_path, branch='master')




if __name__ == '__main__':
    pullcode()