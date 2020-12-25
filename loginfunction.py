import time
from selenium import webdriver

'''
    ** 外置功能，作为模块调用无需此模块 **

    用于获取登陆 cookie ，调用浏览器登陆以防止教务系统更换密码加密方式

    调用功能：
    * 无需此文件，只需通过 WebKit 获取登陆 cookie ，通过 cookie 调用 studentfunction.py 中
      的功能即可

'''

# 从教务系统登陆界面获取 cookie
def login(username, password):
    url = 'http://jxglstu.hfut.edu.cn/eams5-student/login'

    print("召唤 Safari 中 （macOS）")
    driver = webdriver.Safari()
    driver.get(url)
    
    name_input = driver.find_element_by_id('u') 
    pass_input = driver.find_element_by_id('p')  
    login_button = driver.find_element_by_id('submit')  

    name_input.clear()
    name_input.send_keys(username)  
    time.sleep(0.2)
    pass_input.clear()
    pass_input.send_keys(password) 
    time.sleep(0.2)
    login_button.click()            

    time.sleep(0.2)
    
    if(driver.title!="首页"):
        print("没有获取到正确的页面")
        return -1
    
    time.sleep(2)

    print(driver.get_cookies())

    cookies_infomation = driver.get_cookies()
    my_sessionid = driver.get_cookies()[0]
    my_srvid = driver.get_cookies()[1]

    sessiondata = my_sessionid['value']
    srvdata = my_srvid['value']

    driver.close()
    

    cookiesdata = {'session':sessiondata,'srv':srvdata}
    return cookiesdata

    