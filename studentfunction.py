import requests
import re

class ScoreInfo:
    def __init__(self):
        self.name = ''
        self.id = ''
        self.cla = ''
        self.points = ''
        self.gpa = ''
        self.scores = ''
        self.des = ''

class ScoreDescrip:
    def __init__(self):
        self.semester = ''
        self.scoredata = list()
    
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

    result = re.findall(r'<div class="row">(.*?)</tbody>',my_text,re.S|re.M)
    
    result_list = list()

    for items in result:
        data_info = ScoreDescrip()
        semester = re.findall(r'<h3>(.*?)</h3>',items,re.S|re.M)
        #print(semester)
        data_info.semester = semester[0]
        scores = re.findall(r'<td>(.*?)</td>',items,re.S|re.M)
        #print(scores)
        count = 0
        while(count<len(scores)):
            temp_scoredata = ScoreInfo()
            temp_scoredata.name = scores[count]
            temp_scoredata.id = scores[count+1]
            temp_scoredata.cla = scores[count+2]
            temp_scoredata.points = scores[count+3]
            temp_scoredata.gpa = scores[count+4]
            temp_scoredata.scores = scores[count+5]
            temp_scoredata.des = scores[count+6]
            temp_scoredata.des = temp_scoredata.des.replace('<br />',' ')
            data_info.scoredata.append(temp_scoredata)
            count = count + 7
        
        result_list.append(data_info)

    storage_data = ''

    for items in result_list:
        storage_data = storage_data + items.semester
        storage_data = storage_data + '?'
        for datas in items.scoredata:
            storage_data = storage_data + datas.name+'/'+datas.id+'/'+datas.cla+'/'+datas.points+'/'+datas.gpa+'/'+datas.scores+'/'+datas.des
            storage_data = storage_data + '#'
        storage_data = storage_data + '\n'
    
    print(storage_data)

    return result

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

    return result

# 获取学生课表信息
def GetStudentClasses(session_value,srvid_value):


    return

    