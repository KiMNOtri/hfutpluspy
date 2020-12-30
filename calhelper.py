import os
import random
from datetime import timedelta
from datetime import datetime

'''
    用于辅助创日历的 .ics 文件，
    可以导入至手机日程表中。

    ics时间格式：
    2017 03 21 T 17 48 00

'''

class CourseHelper:
    def __init__(self):
        self.calandername = 'HFUTPlus 课程表'
        self.courselist = list()
        self.startdate = None           # 这一学期的开始周星期一对应的日期,为一个 datetime 对象
        self.timeTable = {1:'080000',2:'095000',3:'101000',4:'120000',5:'140000',6:'155000',7:'160000',8:'175000',9:'190000',10:'195000',11:'215000',12:'220000'}

    def SetStartDate(self,datestr):
        dates = datestr.split('-')
        self.startdate = datetime(int(dates[0]),int(dates[1]),int(dates[2]))

        print(self.startdate)
    
    def InsertCourse(self,id,name,location,teacher,begin,end,looptype):
        add_class = ClassEvent(id,name,location,teacher,begin,end,looptype)
        self.courselist.append(add_class)

    def PrintCourse(self):
        ClassWriter(self.courselist)

    def TimeGenerate(self,startUnit,endUnit):               # 生成 timeDic 时间字典， startTime 对应开始时间 endTime 对应结束时间
        timeDic = {}
        timeDic['startTime'] = self.timeTable[startUnit]
        timeDic['endTime'] = self.timeTable[endUnit]
        return timeDic

    def ShiftDateGenerate(self,date,weekday):               # 返回对应日期的偏移时间，为对应的 datetime 对象
        weekday = weekday-1
        redate = date + timedelta(days=weekday)
        return redate

    def ShiftWeekGenerate(self,date,weeks):                 # 返回对应日期的偏移星期，返回对应的 datetime 对象
        shiftweek = (int(weeks)-1)*7
        date = date + timedelta(days=shiftweek)
        return date

    def DateStringGenerate(self,date):                       # 由 datetime 对象生成可用的 string 结果
        datestr = date.strftime('%Y%m%d')
        datestr.replace('-','')
        return datestr

    def InsertStringCourse(self,courseCode,courseName,room,teachers,lessonName,lessonCode,startUnit,endUnit,weekday,weeksStr):
        cla_id = courseCode + str(random.randint(0,9999))
        cla_name = courseName
        cla_location = room
        cla_teacher = "授课教师： "
        for items in teachers:
            cla_teacher+=items
            cla_teacher+=" "
        cla_teacher += "，授课班级： "+lessonName +"，教学班： "+lessonCode
        cla_onweek = weekday
        dic_loadtime = self.TimeGenerate(startUnit,endUnit)     # 获取日期信息里面后面的时间，没有加 T

        
        weeksInfo = weeksStr.split(',')
        # InsertCourse(self,id,name,location,teacher,begin,end,looptype): 调用 InsertCourse 方法添加课程

        for i in weeksInfo:                 # 对阴间的多种时间进行处理
            reweek = i.split('~')           # 对结果进行处理 1~4 -> 1 4 || 4 -> 4 || 4~7(单) -> 4 7(单) 1~3(单)
            if(len(reweek)==1):             # 单日期情况
                my_date = self.ShiftWeekGenerate(self.startdate,reweek[0])                  # 得到偏移日期对应首星期
                my_date = self.ShiftDateGenerate(my_date,cla_onweek)                        # 得到偏移日期对应日期
                cla_starttime = self.DateStringGenerate(my_date) + 'T' + dic_loadtime['startTime']
                cla_endtime = self.DateStringGenerate(my_date) + 'T' + dic_loadtime['endTime']

                self.InsertCourse(cla_id+ str(random.randint(0,9999)),cla_name,cla_location,cla_teacher,cla_starttime,cla_endtime,-1)

            if(len(reweek)==2):             # 双日期情况，下面分了三个叉子
                
                if('单' in reweek[1]):      # 英语课限定：单周情况  2~8(单)
                    p = int(reweek[0])
                    t_q = reweek[1]
                    t_q = t_q.replace('(单)','')
                    q = int(t_q)
                    while(p<=q):
                        my_date = self.ShiftWeekGenerate(self.startdate,p)
                        my_date = self.ShiftDateGenerate(my_date,cla_onweek)
                        cla_starttime = self.DateStringGenerate(my_date) + 'T' + dic_loadtime['startTime']
                        cla_endtime = self.DateStringGenerate(my_date) + 'T' + dic_loadtime['endTime']

                        self.InsertCourse(cla_id+ str(random.randint(0,9999)),cla_name,cla_location,cla_teacher,cla_starttime,cla_endtime,-1)
                        p = p+2

                elif('双' in reweek[1]):    # 英语课限定：双周情况  1~8(双)
                    p = int(reweek[0])
                    t_q = reweek[1]
                    t_q = t_q.replace('(双)','')
                    q = int(t_q)
                    while(p<=q):
                        my_date = self.ShiftWeekGenerate(self.startdate,p)
                        my_date = self.ShiftDateGenerate(my_date,cla_onweek)
                        cla_starttime = self.DateStringGenerate(my_date) + 'T' + dic_loadtime['startTime']
                        cla_endtime = self.DateStringGenerate(my_date) + 'T' + dic_loadtime['endTime']

                        self.InsertCourse(cla_id+ str(random.randint(0,9999)),cla_name,cla_location,cla_teacher,cla_starttime,cla_endtime,-1)
                        p = p+2                    
                else:                       # 正常的情况        1~9
                    my_date = self.ShiftWeekGenerate(self.startdate,reweek[0])
                    my_date = self.ShiftDateGenerate(my_date,cla_onweek)
                    looptype = int(reweek[1]) - int(reweek[0]) + 1
                    cla_starttime = self.DateStringGenerate(my_date) + 'T' + dic_loadtime['startTime']
                    cla_endtime = self.DateStringGenerate(my_date) + 'T' + dic_loadtime['endTime']

                    self.InsertCourse(cla_id+ str(random.randint(0,9999)),cla_name,cla_location,cla_teacher,cla_starttime,cla_endtime,looptype)




                
class ClassEvent:
    def __init__(self):
        self.id = ''
        self.name = ''
        self.location = ''
        self.teacher = ''
        self.begin = ''
        self.end = ''
        self.looptype = ''
    def __init__(self,id,name,location,teacher,begin,end,looptype):
        self.id = id
        self.name = name
        self.location = location
        self.teacher = teacher
        self.begin = begin
        self.end = end
        self.looptype = looptype
    def __str__(self):
        return self.name+'/'+self.location+'/'+self.teacher+'/'+self.begin+'/'+self.end+self.looptype
        
# 将 eventdata 列表写入为 ics 文件
def ClassWriter(eventdata):
    writestring = "BEGIN:VCALENDAR\n"
    writestring += "PRODID:-//Apple Inc.//Mac OS X 10.15.7//EN\n"
    writestring += "VERSION:2.0\n"
    writestring += "CALSCALE:GREGORIAN\n"
    writestring += "METHOD:PUBLISH\n"
    writestring += "X-WR-CALNAME:HFUTPlus 课程表\n"
    writestring += "X-WR-TIMEZONE:null\n"
    for event in eventdata:
        writestring += CourseGenerater(event.id,event.name,event.location,event.teacher,event.begin,event.end,event.looptype)

    writestring += "END:VCALENDAR"

    fo = open("Courses.ics","w")
    fo.write(writestring)
    fo.close()

    return

# 生成单个课程描述代码块
def CourseGenerater(id,name,location,teacher,begin,end,looptype):
    string = ""
    string += "BEGIN:VEVENT\n"
    string += "SUMMARY:"+name+"\n"
    if(looptype!=-1):
        string += "RRULE:FREQ=WEEKLY;COUNT="+str(looptype)+"\n"
    string += "ORGANIZER;CN=My Calendar:mailto:tri.studio@outlook.com\n"
    string += "DTSTART;TZID=Asia/Shanghai:"+begin+"\n"
    string += "DTEND;TZID=Asia/Shanghai:"+end+"\n"
    string += "UID:"+id+"\n"
    string += "SEQUENCE:0\n"
    if(teacher!=None):
        string += "DESCRIPTION:"+str(teacher)+"\n"
    if(location!=None):
        string += "LOCATION:"+str(location)+"\n"
    string += "STATUS:CONFIRMED\n"

    string += "BEGIN:VALARM\n"
    string += "UID:"+str(random.randint(0,9999999)) +"\n"
    string += "TRIGGER:-PT5M\n"
    string += "ACTION:AUDIO\n"
    string += "END:VALARM\n"

    string += "END:VEVENT\n"

    return string

if __name__ == '__main__':
    re = list()
    cl1 = ClassEvent('213','asd','sd','tristudio','20200908T151000','20200908T160000',-1)
    cl2 = ClassEvent('21233','aasd','ssd','tridstudio','20201230T151000','20201230T160000',-1)
    re.append(cl1)
    re.append(cl2)

    ClassWriter(re)
    

    