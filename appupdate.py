#coding=utf-8
import requests
import threading
from getsign import getSign



def reqGetsign(category,version='V1.0.0'):
    #获取地址
    url = 'https://apitest.ecowitt.net/api/app/v1/version/get_sign'
    #获取参数
    par = {}
    par['deviceid'] = 'C392D7BC1136648921F704DFB33049CA'
    par['category'] = category
    par['platform'] = 'android'
    par['system'] = 'Android10'
    par['brand'] = 'HUAWEI'
    par['model'] = 'MHA-AL00'
    par['version'] = version
    par['time'] = '1622795293'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36'
    }

    #访问接口
    reqsign = requests.request('get',url,headers=header,params=par)
    return reqsign.json()['data']['sign']



def appUpdate(category,version='V1.0.0'):
    # 获取地址
    url = 'https://apitest.ecowitt.net/api/app/v1/version/info'
    #获取sign
    #Version = version
    #gSign = reqGetsign(category,Version)
    #print(gSign)
    # 获取参数
    param = {}
    param['deviceid'] = 'C392D7BC1136648921F704DFB33049CA'
    param['category'] = category
    param['platform'] = 'android'
    param['system'] = 'Android10'
    param['brand'] = 'HUAWEI'
    param['model'] = 'MHA-AL00'
    param['version'] = version
    param['time'] = '1622795293'
    sign = getSign(param)
    param['sign'] = sign

    #print(param)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36'
    }


    # 访问接口
    reqUpdate = requests.request('get', url, headers=header,params=param)
    return reqUpdate.json()



if __name__ == '__main__':
    # 多线程
    # for x in range(500):
    #     proc = threading.Thread(target=appUpdate,args=('Ecowitt',))
    #     proc.start()
    data = {'deviceid':'C392D7BC1136648921F704DFB33049CA','time':'1622795293','email':'462451569@qq.com'}
    print(appUpdate('Ecowitt','1000'))
