import studentfunction
import requests
'''
    SilentListener 提供接口供外部调用
'''

# 检查当前与教务系统的连接情况。连接正常返回 0 ，无网络为 -1，无法访问教务系统为 -2
def CheckConnection():
    try:
        resp = requests.get("http://jxglstu.hfut.edu.cn")
        print(resp.status_code)
        if(resp.status_code!=200):
            print('There was a error during the connection between the system.')
            return -2
    except requests.ConnectionError as e:
        print('Unable to connect the Internet.')
        return -1

    return 0


# 检查当前Cookie状态。连接正常返回 0 ，不可用为 1
def CheckCookie(session,srvid):
    cookie_info = 'SESSION=' + session + '; SRVID=' + srvid

    myheaders = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection':'keep-alive',
        'Cookie':cookie_info,
        'Host':'jxglstu.hfut.edu.cn',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60'
    }

    resp = requests.get('http://jxglstu.hfut.edu.cn/eams5-student/home',headers=myheaders,allow_redirects=False)

    print(resp.status_code)

    if(resp.status_code==302):
        return 1
    
    return 0


# 由 Cookie 访问学生成绩单信息，返回内容为描述字符串
def GetScores(session,srvid):
    return studentfunction.GetStudentScore(session,srvid)

# 由 Cookie 访问学生考试信息，返回内容为描述字符串
def GetExams(cookies):
    return studentfunction.GetStudentExams(session,srvid)

if (__name__=='__main__'):
    # something