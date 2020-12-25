import loginfunction
import tkinter
import studentfunction
import getpass

'''
    和用户交互有关的功能都在这里
'''

def loginfun(): 
    print("教务系统学号：")
    username = input()
    print("教务系统密码：（输入内容不会显示）")
    passwd = getpass.getpass()
    
    backinfo = loginfunction.login(username,passwd)

    if(backinfo==-1):
        print("登陆时遇到了问题，请重新再试。")
    else:
        print("获取教务系统 cookie 成功惹")
        print(backinfo)
        studentfunction.GetStudentScore(backinfo['session'],backinfo['srv'])
        

        
