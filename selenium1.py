from selenium import webdriver
# 配置驱动
option = webdriver.ChromeOptions()
driver = webdriver.Chrome('D:\ChromeDriver\chromedriver.exe', chrome_options=option)
# 控制浏览器打开指定页面
driver.get('https://h5.youzan.com/v2/showcase/homepage?kdt_id=18669836&reft=1538228635262&spm=mid18669836&oid=20205562')
# 找到登录按钮
btn_login = driver.find_element_by_class_xpath('')
# 点击登录按钮
btn_login.click()
# 找到手机标签
input_user = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[8]/div[3]/div/a/div/img')
print(input_user)
# 找到密码标签
input_pwd = driver.find_element_by_xpath('')
# 输入用户名
input_user.send_keys('')
# 输入密码
input_pwd.send_keys('')
# 点击登录按钮
input_submit = driver.find_element_by_xpath('')
input_submit.click()
# 点击跳转
news = driver.find_element_by_xpath('')
news.click()
driver.exceute_script('arguments[0].click();', news)
# 管理浏览器
driver.close()