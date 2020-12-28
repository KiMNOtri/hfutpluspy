import time
from selenium import webdriver
import os
import savestate

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

    if(os.name=='nt'):
        print("当前暂不支持 Windows (NT) ！")
        
        return -1

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
    

    cookiesdata = {'session':sessiondata,'srvid':srvdata}
    #cookie_savefunction(cookiesdata)
    savestate.SaveCookieState(cookiesdata)

    return cookiesdata

'''
# 已经弃用
def cookie_savefunction(cookie_data):


    write_string = cookie_data['session'] + '/' + cookie_data['srvid']

    fo = open('cookiedata.archive','w')
    fo.write(write_string)

    fo.close()

    return

# 读取 Cookie 信息
def cookie_readfunction():

    if(not os.path.exists("cookiedata.archive")):
        print("没有找到临时 Cookie 文件。")
        return -1

    fr = open('cookiedata.archive')
    read_string = fr.read()

    print(read_string)

    cookiedata = read_string.split('/')

    cookies = {'session':cookiedata[0],'srvid':cookiedata[1]}

    return cookies

'''