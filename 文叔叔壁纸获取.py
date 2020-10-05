import os
import requests
import time
import json
import re

def dowimg(t,i,link):
    global c
    dir = t + '\\' + i  # 构造完整文件名称
    print(dir)
    f = requests.get(link)
    with open(dir, "wb") as code:
        code.write(f.content)  # 保存文件


'''
s = {'hot':21,
     'design':19,
     'landscape':59,
     'sea':32,
     'city':49,
     'sky':21,
     'technology':21,
     'retro':20,
     'sexy':18,
     'office':12,
     'animals':21,
     'sports':29,
     'texture':39
     }'''
def get_info():
    data = requests.get('https://www.wenshushu.cn/ag/gls?prod=com.wenshushu.web.pc').text
    pattern = '\\\\"data\\\\":(.*?)","PACK_DOWNLOAD_NUM'
    result = re.compile(pattern).findall(data)[0][:-1]
    result = result.replace('\\','')
    a = json.loads(result)
    info = {}
    for i in a:
        info[i] = a.get('hot').get('images')[1]
    return info


link = 'https://wss-static.wenshushu.cn/images/background/'
info = get_info()
for t,k in info.items():
    os.mkdir(t)
    for i in range(1,k+1):
        name = str(i)+'.jpg'
        dowimg(t,name,link+t+'/'+name)
        time.sleep(0.5)
print("Done.")
