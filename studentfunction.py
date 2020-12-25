import requests


# 获取学生成绩单信息
def GetStudentScore(session_value,srvid_value):
    cookie_info = 'SESSION=' + session_value + '; SRVID=' + srvid_value

    myheaders = {
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer':'http://jxglstu.hfut.edu.cn/eams5-student/for-std/grade/sheet/semester-index/134599',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Host':'jxglstu.hfut.edu.cn',
        'Cookie':cookie_info
    }
    resp = requests.get('http://jxglstu.hfut.edu.cn/eams5-student/for-std/grade/sheet/info/134599?semester=',headers=myheaders)
    my_text = resp.text

    