
from subprocess import call

filepath = r'D:\free.txt'


with open(filepath, 'r') as f:
    modules_info = f.readlines()
    modules_info = [c.replace('\n','') for c in modules_info]

count = 0
for single in modules_info:
    count += 1
    print(count)

    try:
        import os
        os.chdir(r'D:\free')
        cmd = 'python -m pip --default-timeout=100 download ' + single +' -i http://pypi.douban.com/simple --trusted-host pypi.douban.com'
        print(cmd)
        re = call(cmd,shell=True)
        print(re)
    except:
        print('waring: '+single)
    else:
        print('ok: '+single)
