import requests
import nice
session=requests.Session()
login_url='https://kyfw.12306.cn/otn/login/init'
response=session.get(login_url)

captcha_url='https://kyfw.12306.cn/passport/captcha/captcha-image?log\
in_site=E&module=login&rand=sjrand&0.37989953817611766'
captcha_response=session.get(captcha_url)
print(captcha_response.content)
f=open("captcha.jpg","wb")
f.write(captcha_response.content)
f.close()
code=input("请输入验证码:")
captcha_check_api="https://kyfw.12306.cn/passport/captcha/captcha-check"
data={'answer': code.split(),
      'login_site': 'E',
      'rand': 'sjrand'
}
check_response=session.post(captcha_check_api,data=data)
#print(check_response.text)
check=check_response.json()
if check['result_code']=='4':
      print('验证码检验成功')
      #print(check)
      login_api='https://kyfw.12306.cn/passport/web/login'
      login_data={'username': nice.username,
                  'password': nice.password,
                  'appid': 'otn'}
      res=session.post(login_api,login_data)
      print(res.text)