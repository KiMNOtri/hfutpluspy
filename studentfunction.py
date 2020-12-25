import requests
import re

# 获取学生成绩单信息
def GetStudentScore(session_value,srvid_value):
    print("正在获取重定向地址...")
    
    cookie_info = 'SESSION=' + session_value + '; SRVID=' + srvid_value

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
    resp = requests.get('http://jxglstu.hfut.edu.cn/eams5-student/for-std/grade/sheet',headers=myheaders,allow_redirects=False)

    print(resp.headers)

    print("已经获取到信息，正在请求成绩。")

    request_url = resp.headers['Location']
    print(request_url)

    infomation = request_url.split('/')
    student_scoreid = infomation[6]
    print(student_scoreid)

    score_requesturl = 'http://jxglstu.hfut.edu.cn/eams5-student/for-std/grade/sheet/info/'+student_scoreid+'?semester='

    request_headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection':'keep-alive',
        'Cookie':cookie_info,
        'Host':'jxglstu.hfut.edu.cn',
        'Referer':'http://jxglstu.hfut.edu.cn'+request_url,
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60'
    }

    respond_data = requests.get(score_requesturl,headers=request_headers,params='semester:')
    
    my_text = respond_data.text

    print(my_text)

    result = re.findall(r'<td>(.*?)</td>',my_text,re.S)
    print(result)

    for items in result:
            items = items.replace('<br />',' ')
            print(items)


# 获取学生考试信息
def GetStudentExams(session_value,srvid_value):
    print("正在获取重定向地址...")
    
    cookie_info = 'SESSION=' + session_value + '; SRVID=' + srvid_value

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
    resp = requests.get('http://jxglstu.hfut.edu.cn/eams5-student/for-std/exam-arrange',headers=myheaders,allow_redirects=False)

    print(resp.headers)

    print("已经获取到信息，正在请求考试信息。")

    request_url = resp.headers['Location']
    print(request_url)

    infomation = request_url.split('/')
    student_scoreid = infomation[5]
    print(student_scoreid)

    score_requesturl = 'http://jxglstu.hfut.edu.cn/eams5-student/for-std/exam-arrange/info/'+student_scoreid+'?semester='

    request_headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection':'keep-alive',
        'Cookie':cookie_info,
        'Host':'jxglstu.hfut.edu.cn',
        'Referer':'http://jxglstu.hfut.edu.cn'+request_url,
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60'
    }

    respond_data = requests.get(score_requesturl,headers=request_headers)
    
    my_text = respond_data.text

    print(my_text)

    result = re.findall(r'<td>(.*?)</td>',my_text,re.S)
    print(result)

    for items in result:
            items = items.replace('<br />',' ')
            print(items)
    return


    