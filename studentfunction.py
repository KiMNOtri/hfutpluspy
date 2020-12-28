import requests
import re
import sys
import os
import json
import random
import calhelper
from datetime import timedelta
from datetime import datetime

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

    storage_data = list()

    for items in result_list:

        dic_2 = {}
        dic_2['semester'] = items.semester
        scores_list = list()
        
        for datas in items.scoredata:
            dic_3 = {}    
            dic_3['name'] = datas.name
            dic_3['id'] = datas.id
            dic_3['cla'] = datas.cla
            dic_3['points'] = datas.points
            dic_3['gpa'] = datas.gpa
            dic_3['scores'] = datas.scores
            dic_3['des'] = datas.des
            scores_list.append(dic_3)
            
        dic_2['values'] = scores_list
        
        storage_data.append(dic_2)
    
    print(storage_data)

    result_text = json.dumps(storage_data,ensure_ascii=False)


    fo = open('scoredata.json','w',encoding='utf-8')
    fo.write(result_text)

    fo.close()


    return storage_data

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


    result = re.findall(r'<td>(.*?)</td>',my_text,re.S)
    time_result = re.findall(r'<td class="time">(.*?)</td>',my_text,re.S)
    print(result)

    for items in result:
        items = items.replace('<br />',' ')
        

    back_result = list()

    i=0

    while(i<len(time_result)):
        datas = {}
        datas['subject'] = result[i*4]
        datas['time'] = time_result[i]
        datas['location'] = result[i*4+1]

        back_result.append(datas)        
        
        '''back_result += result[4*i]
        back_result += '/'
        back_result += time_result[i]
        back_result += '/'
        back_result += result[i*4+1]
        '''
        i=i+1

    print(back_result)

    result_text = json.dumps(back_result,ensure_ascii=False)


    fo = open('examdata.json','w',encoding='utf-8')
    fo.write(result_text)

    fo.close()

    return back_result

# 获取学生课表信息
def GetStudentClasses(session_value,srvid_value):

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
    resp = requests.get('http://jxglstu.hfut.edu.cn/eams5-student/for-std/course-table/',headers=myheaders,allow_redirects=False)

    print(resp.headers)

    print("已经获取到信息，正在请求课表信息。")

    request_url = resp.headers['Location']
    print(request_url)

    infomation = request_url.split('/')
    student_scoreid = infomation[5]
    print(student_scoreid)

    score_requesturl = 'http://jxglstu.hfut.edu.cn/eams5-student/for-std/course-table/semester/114/print-data/'+student_scoreid

    request_headers = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection':'keep-alive',
        'Cookie':cookie_info,
        'Host':'jxglstu.hfut.edu.cn',
        'Referer':'http://jxglstu.hfut.edu.cn/eams5-student/for-std/course-table/semester/114/print/'+student_scoreid+'?',
        'X-Requested-With':'XMLHttpRequest',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60'
    }

    respond_data = requests.get(score_requesturl,headers=request_headers)
    
    print(respond_data)
    json_data = respond_data.json()
    print(json_data)

    # 对课表的 JSON 信息进行解码

    events_list = list()
    

    jsondata_step1 = json_data['studentTableVm']
    print(jsondata_step1['id'])
    print(jsondata_step1['code'])
    print(jsondata_step1['adminclass'])

    jsondata_step2 = jsondata_step1['activities']

    unit_list = {1:'080000',2:'095000',3:'101000',4:'120000',5:'140000',6:'155000',7:'160000',8:'175000',9:'190000',10:'200000',11:'215000'}

    print("请输入学期开始时间，以YYYY/MM/DD形式输入：")
    starttime = input()

    dates = starttime.split('/')

    date_start = datetime(int(dates[0]),int(dates[1]),int(dates[2]))
    
    i=1
    clock_list = {}
    
    while(i<24):
        #datestr = date_start.strftime('%Y%m%d')
        #datestr = datestr.replace('-','')

        #print(datestr)
        clock_list[i]=date_start

        date_start = date_start+timedelta(days=7)

        i=i+1


    for lessons in jsondata_step2:
        cla_id = str(lessons['courseCode'])
        cla_id = cla_id + str(random.randint(0,9999))
        cla_name = str(lessons['courseName'])
        cla_location = lessons['room']
        
        cla_starttime = ""
        cla_endtime = ""
        cla_teacher = 'null'

        # 待处理，多日期情况，英语课情况 

        temp_eventdays = lessons['weeksStr']
        temp_event = re.split('~|,',temp_eventdays)

        print(lessons['weekStr'])


        begin_week = int(temp_event[0])
        if(len(temp_event)>1):
            if(temp_event[1].isdigit()==True):
                end_week = int(temp_event[1])
            else:
                end_week = int(temp_event[0])
        else:
            end_week = int(temp_event[0])

        cla_looptype = end_week - begin_week + 1

        temp_eventdate = clock_list[begin_week]
        temp_where = int(lessons['weekday'])
        temp_where = temp_where-1

        temp_eventdate = temp_eventdate + timedelta(days=temp_where)
        datestr = temp_eventdate.strftime('%Y%m%d')
        datestr.replace('-','')

        temp_startunit = lessons['startUnit']
        temp_endunit = lessons['endUnit']

        cla_starttime = datestr + 'T' + unit_list[temp_startunit]
        cla_endtime = datestr + 'T' + unit_list[temp_endunit]

        cal = calhelper.ClassEvent(cla_id,cla_name,cla_location,cla_teacher,cla_starttime,cla_endtime,cla_looptype)
        events_list.append(cal)

    calhelper.ClassWriter(events_list)
        
    print("🥳 生成课表完成，复制目录下的 Courses.ics 即可导入～")
    
    return

    
def DeleteStudentInfomation():
    print("🤔 确定要删除你的 Cookie 信息吗？你将需要重新登录。")
    print("n:取消 y:确定")
    
    choose = input()

    if(choose=='y'):
        if os.path.exists("cookiedata.archive"):
            os.remove("cookiedata.archive")
            print("删除成功，重新启动程序后生效 😆")
            sys.exit(0)
        else:
            print("啊嘞？")
            return
    return