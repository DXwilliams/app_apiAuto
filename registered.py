#coding=utf-8
import requests
from getsign import getSign



def getVerificationcode(email):
    #获取基础地址
    url = 'https://apitest.ecowitt.net/api/app/v1/user/getRegisterCaptcha'
    #获取参数,获取sign
    params = {}
    params['deviceid'] = 'C392D7BC1136648921F704DFB33049CA'
    params['email'] = email
    params['time'] = '1622795293'
    sign = getSign(params)
    params['sign'] = sign
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36'
    }

    #访问接口
    Vcodereq = requests.request('get',url,headers=header,params=params)
    return Vcodereq.json()


def userRegister(captcha):
    #地址
    url = 'https://apitest.ecowitt.net/api/app/v1/user/register'
    #post,表单参数
    registerData = {}
    registerData['email'] = '462451569@qq.com'
    registerData['captcha'] = captcha
    registerData['password'] = '123456'
    registerData['time'] = '1622795293'
    sign = getSign(registerData)
    registerData['sign'] = sign
    #访问接口
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36'
    }

    userreq = requests.request('post',url,headers=header,data=registerData)
    return userreq.json()



if __name__ == '__main__':
    #print(getVerificationcode('4624519@qq.com'))
    #userRegister(7506)
    #注册验证码接口测试邮箱正确性
    emailstr = ['46245169.com','462451569@ssss.com','1@qq.com','462451569@qq.cn','!#$%^@@.us']
    # for x in emailstr:
    #     print(getVerificationcode(x))
    print(getVerificationcode('456412312qweqweqweqweAeqwe23423423423234234@qq.com'))