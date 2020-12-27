import studentfunction
'''
    SilentListener 提供接口供外部调用
'''

# 检查当前与教务系统的连接情况。连接正常返回 0 ，不正常为 -1
def CheckConnection():
    
    return 0

# 由 Cookie 访问学生成绩单信息，返回内容为描述字符串
def GetScores(cookies):
    return studentfunction.GetStudentScore(cookies['session'],cookies['srvid'])

# 由 Cookie 访问学生考试信息，返回内容为描述字符串
def GetExams(cookies):
    return studentfunction.GetStudentExams(cookies['session'],cookies['srvid'])

