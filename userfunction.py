import loginfunction
import studentfunction
import getpass
import os
import requests
import savestate
import sys

'''
    和用户交互有关的功能都在这里
'''

def checknet():
    try:
        resp = requests.get("http://jxglstu.hfut.edu.cn")
        print(resp.status_code)
        if(resp.status_code!=200):
            print('和教务系统的连接出现问题！这可能是暂时性的错误，请更换网络或者稍后再试。')
            sys.exit(0)
    except requests.ConnectionError as e:
        print('无法连接到互联网...请检查你的连接之后再试。')
        sys.exit(0)

    return 0

def userfun(): 

    checknet()
    
    backinfo = -1
    if(os.path.exists('cookiedata.archive')):
        backinfo = savestate.ReadCookieState()
        current_state = savestate.VerifyCookieState(backinfo)
        if(current_state==False):
            print("Cookie 似乎已经失效了...")
            backinfo = -1

    
    if(backinfo==-1):
        print("🤔 请输入教务系统账号信息：")
        print("学号：")
        username = input()
        print("密码：（输入内容不会显示）")
        passwd = getpass.getpass()
    
        backinfo = loginfunction.login(username,passwd)

        if(backinfo==-1):
            print("登陆时遇到了问题，请重新再试。")
        else:
            print("获取教务系统 cookie 成功惹")
        
    print(backinfo)

    while(True):
        print("选择选项：1、获取成绩 2、获取考试信息 3、获取课表信息 4、重置个人信息")
        letter = input()
        if(letter=='1'):
            checknet()
            studentfunction.GetStudentScore(backinfo['session'],backinfo['srvid'])
        if(letter=='2'):
            checknet()
            studentfunction.GetStudentExams(backinfo['session'],backinfo['srvid'])
        if(letter=='3'):
            checknet()
            studentfunction.GetStudentClasses(backinfo['session'],backinfo['srvid'])
        if(letter=='4'):
            studentfunction.DeleteStudentInfomation()

def webviewhelper():
    os_type = ''
    if(os.name=='posix'):
        os_type = 'macOS'
    else:
        os_type = 'Windows'
    
    if(os_type == 'macOS'):
        print('当前你的系统为：'+os_type)
        print('建议使用 Safari 浏览器进行模拟登陆操作。')
        print('操作指引：打开 Safari 浏览器，在偏好设置面板中开启开发选项，在顶栏的开发者选单中激活「允许远程自动化」，重新运行程序即可。')
    else:
        print('当前你的系统为：'+os_type)
        print('建议使用 Chrome 浏览器进行模拟登陆操作。')
        print('请将程序附赠的 chromedriver.exe/geckodriver.exe 拷贝至 python.exe 的所在目录下，重新运行程序后再试。(请确定 Python 已经被添加至环境变量)')
        


        


        
