# 自动安装模块包

import os
from subprocess import call

m_path = r'D:\free.txt'
path = r'D:\free'

with open(m_path, 'r') as f:
    modules = f.readlines()

name = []
version = []

for module in modules:
    var = module.split("==", -1)
    name.append(var[0])
    version.append(var[1][:-1])

files = os.listdir(path)

pk_name = []
pk_version = []
for file in files:
    sv = file.split('-')
    pk_name.append(sv[0])
    if len(sv) > 2:
        if sv[1][0].isdigit():
            pk_version.append(sv[1])
        elif len(sv) == 3:
            pk_version.append(sv[2][-7])
        else:
            pk_version.append(sv[2])
    else:
        pk_version.append([1][-7])

for i in range(len(pk_name)):
    if pk_name[i] in name:
        loc = name.index(pk_name[i])
        if pk_version[i] != version[loc]:
            call('pip install -U ' + path + '/' + files[i])
            print(str(i + 1) + ' Updata: ' + files[i])
        else:
            print(str(i + 1) + ' Exist: ' + files[i])
    else:
        call('pip install ' + path + '/' + files[i])
        print(str(i + 1) + ' Setup: ' + files[i])

