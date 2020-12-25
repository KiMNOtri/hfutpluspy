import time
from selenium import webdriver

# 从教务系统登陆界面获取 cookie
def login(username, password):
    url = 'http://jxglstu.hfut.edu.cn/eams5-student/login'

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
    print(driver.get_cookies())

    if(driver.title!="首页"):
        print("Login Error")
    

    time.sleep(2)

    driver.close()