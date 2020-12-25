import loginfunction
import tkinter
import studentfunction
import getpass

'''
    和用户交互有关的功能都在这里
'''

def loginfun(): 
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
        print("选择选项：1、获取成绩 2、获取考试信息")
        letter = input()
        if(letter=='1'):
            studentfunction.GetStudentScore(backinfo['session'],backinfo['srv'])
        if(letter=='2'):
            studentfunction.GetStudentExams(backinfo['session'],backinfo['srv'])

        

        
