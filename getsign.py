import requests
from urllib.parse import urlencode
import hashlib


def getSign(params):
    #params ={'deviceid':'C392D7BC1136648921F704DFB33049CA','time':'1622795293','email':'462451569@qq.com'}
    enparams = urlencode(params)     #对传进来的参数进行URL转义
    #print(enparams)

    enparamslst = enparams.split('&')
    enparamslst.sort()      #对参数进行排序
    signstr = ''

    for j in range(len(enparamslst)):           #重新拼接字符串
        if j<len(enparamslst)-1:
            signadd = signstr + enparamslst[j] + '&'
            signstr = signadd
        else:
            signadd = signstr + enparamslst[j]
            signstr = signadd

    signstrall = signstr+'@ecowittnet'
    #print(signstrall)
    signhash = hashlib.md5(signstrall.encode("utf-8"))  #md5加密

    return signhash.hexdigest()


if __name__=='__main__':
     data = {'deviceid':'C392D7BC1136648921F704DFB33049CA','time':'1622795293','email':'462451569@qq.com'}
     print(getSign(data))