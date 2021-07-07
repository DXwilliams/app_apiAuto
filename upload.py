#coding=utf-8
from getsign import getSign
import requests
from Login import uLogin
from pprint import pprint


def test_getinfo(databasic):
    url = 'https://apitest.ecowitt.net/api/app/v1/user/info'
    #查询参数
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36'
    }
    userbasic = databasic
    token = uLogin(userbasic)['data']['token']
    header['Token'] = token
    #访问接口
    getinfo_req = requests.request('get',url,headers=header)
    return getinfo_req.json()


def test_upload(filename):
    url = 'https://apitest.ecowitt.net/api/app/v1/user/upload'

    #准备参数和浏览器配置
    Data = {}
    datatest = {'account': '462451569@qq.com', 'password': '123456'}
    token = uLogin(datatest)['data']['token']
    #print(token)
    Data['token'] = token

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36'
    }
    #获取文件
    file_name = filename
    file = {'file': open(filename,'rb')}
    #访问接口
    uploadreq = requests.request('post',url,headers=header,data=Data,files=file)

    return uploadreq.json()


def test_profile(**kwargs):
    url = 'https://apitest.ecowitt.net/api/app/v1/user/profile'

    #修改参数和header传token
    change_data = {}
    datatest = {'account': '462451569@qq.com', 'password': '123456'}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36',
    }
    user_data = uLogin(datatest)['data']
    #print(user_data)
    token = user_data['token']
    header['Token'] = token
    user_id = user_data['id']
    avatar = test_upload('1.jpg')['data']['url']
    #print(avatar)
    change_data['user_id'] = user_id
    #不定长参数传参
    for key,value in kwargs.items():
        change_data[key] = value
    change_data['avatar'] = avatar
    change_data['time'] = '1622795293'
    sign = getSign(change_data)
    change_data['sign'] = sign
    #print(sign)

    #访问接口
    profile_req = requests.request('post',url,headers=header,data=change_data)

    return profile_req.json()

def test_changepwd(oldpassword,newpassword):
    url = 'https://apitest.ecowitt.net/api/app/v1/user/changepwd'

    # 修改参数和header传token
    change_data = {}
    datatest = {'account': '462451569@qq.com', 'password': '123456'}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36',
    }
    user_data = uLogin(datatest)['data']
    #print(user_data)
    token = user_data['token']
    header['Token'] = token
    user_id = user_data['id']
    change_data['user_id'] = user_id
    change_data['oldpassword'] = oldpassword
    change_data['newpassword'] = newpassword
    change_data['time'] = '1622795293'
    sign = getSign(change_data)
    change_data['sign'] = sign
    # 访问接口
    changepwd_req = requests.request('post', url, headers=header, data=change_data)

    return changepwd_req.json()


# def func1(**kwargs):
#     dic = {}
#     for key,values in kwargs.items():
#         dic[key] = values
#     print(dic)

if __name__ == '__main__':
    #testdata = ('DD123456','DDWWW')
    datatest = {'account': '462451569@qq.com', 'password': '123456'}
    #pprint(test_getinfo(datatest))
    #print(test_upload('1.jpg'))
    #pprint(test_profile())
    #pprint(test_changepwd('1234567','123456'))

    print(test_profile(username=123456,nickname="DDDSSS"))