import time
from selenium import webdriver
import os
import savestate
import sys

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

    try:
        if(os.name=='nt'):
            print("1.Chrome 2.Firefox")
            inu = input()
            if(inu=='1'):
                print("召唤 Chrome 中 （Windows）")
                driver = webdriver.Chrome()
            else:
                print("召唤 Firefox 中 （Windows）")
                driver = webdriver.Firefox()
        
        if(os.name=='posix'):
            print("召唤 Safari 中 （macOS）")
            driver = webdriver.Safari()

    except Exception as e:
        print("调用浏览器功能失败了！请检查浏览器驱动，详情查阅 README.md.")
        sys.exit(0)
    
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
    

    cookiesdata = {'session':sessiondata,'srvid':srvdata}
    #cookie_savefunction(cookiesdata)
    savestate.SaveCookieState(cookiesdata)

    return cookiesdata

