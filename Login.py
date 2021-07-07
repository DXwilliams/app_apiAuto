#coding=utf-8
from getsign import getSign
import requests
from urllib.parse import urlencode
from urllib.request import quote
import urllib.parse
from pprint import pprint

#登录
def uLogin(Baisedata):
    #地址
    url = 'https://apitest.ecowitt.net/api/app/v1/user/login'

    #准备参数和浏览器配置
    uData = Baisedata
    uData['time'] = '1622795293'
    #print(uData)
    sign = getSign(uData)
    uData['sign'] = sign
    #print(sign)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36'
    }

    #访问接口
    Loginreq = requests.request('post',url,headers=header,data=uData)
    return Loginreq.json()

#print(uLogin()['data']['token'])

#登出
def uLogout(datatest):
    #地址
    url = 'https://apitest.ecowitt.net/api/app/v1/user/logout'
    #参数
    params = {}
    user_Basic = datatest
    utoken = uLogin(user_Basic)['data']['token']
    #print(utoken)
    params['token'] = utoken
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36'
    }

    #访问接口
    req = requests.request('get',url,headers=header,params=params)
    return req.json()


#获取重置密码验证码
def get_RestetpwdCaptcha():
    url = 'https://apitest.ecowitt.net/api/app/v1/user/getResetpwdCaptcha'

    #准备参数
    userData = {}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36'
    }
    userData['deviceid'] = 'C392D7BC1136648921F704DFB33049CA'
    userData['email'] = '462451569@qq.com'
    userData['time'] = '1622795293'
    sign = getSign(userData)
    #print(sign)
    userData['sign'] = sign
    #print(userData)

    #访问接口
    ResetpwdCatcha_req = requests.request('get',url,headers=header,params=userData)
    return ResetpwdCatcha_req.json()


#重置密码
def resetpwd(captcha):
    url = 'https://apitest.ecowitt.net/api/app/v1/user/resetpwd'

    #准备参数
    userData = {}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36'
    }
    userData['email'] = '462451569@qq.com'
    userData['captcha'] = captcha
    userData['password'] = '123456'
    userData['time'] = '1622795293'
    sign = getSign(userData)
    userData['sign'] = sign

    #访问接口
    resetpwd_req = requests.request('post',url,headers=header,data=userData)
    return resetpwd_req.json()







#print(uLogout())
if __name__=='__main__':
    data = {'account':'462451569@qq.com','password':'123456'}
    passwVCtion = [[(1,2)],
                   {'key':'values'},
                   'おはようございます',
                   '早上好早上好早上好',
                   '<>?:"{}|~!@#$%^&*()_+',
                   '  tirm  <p>{[1,2]}[{}]</p>  ',
                   r'E:\测试\项目资料\2550\软件版本',
                   '__init__&/n/t/r<>^',
                   '0.12int.strim(<div></div>)',
                   '   123  ',
                   ''''<>?:""{}|~!@#$%^&*()_+'     
                       ''',
                   ''' "<>?:""{}|~!@#$%^&*()_+'" ''',
                   '《》？、；’：【】|、·！@#￥%……&*（）——+',
                   '＇＂＜＞？：＂＇｛｝［］｜＼～！＠＃＄％＾＆＊（）～',
                   '''ａｓｄｆｑｗｒｑｔ１２４ａｄｆｍｋｓｄｋｆ''',
                   '''
                   "or 1=1#
                   '''
                   ]
    # s1 = "-*()_~!.'"
    # str = '<>?:"{}|~!@#$%^&*()_+'
    # # str_dic = {}
    # # str_dic['str'] = '<>?:"{}|~!@#$%^&*()_+'
    # #str_en = urlencode(str_dic)
    # str_en = quote(str)
    # str_en1=urllib.parse.quote(str)
    # print(str_en)
    # #data['password'] = str
    # #print(uLogin(data))


    # for x in passwVCtion:
    #     data = {'account': '462451569@qq.com', 'password': '123456'}
    #     if type(x) == str:
    #         strx = x.strip()
    #         data['password'] = strx
    #         #print(data)
    #         print(uLogin(data))
    #     else:
    #         data['password'] = x
    #         #print(data)
    #         print(uLogin(data))

    datatest = {'account': '462451569@qq.com', 'password': '123456'}
    print(uLogin(datatest))
    #pprint(get_RestetpwdCaptcha())
    #pprint(resetpwd(9166))
    #pprint(uLogout(datatest))