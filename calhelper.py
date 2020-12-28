import os

'''
    用于辅助创日历的 .ics 文件，
    可以导入至手机日程表中。

    ics时间格式：
    2017 03 21 T 17 48 00

'''



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


    string += "END:VEVENT\n"

    return string

if __name__ == '__main__':
    re = list()
    cl1 = ClassEvent('213','asd','sd','tristudio','20200908T151000','20200908T160000',-1)
    cl2 = ClassEvent('21233','aasd','ssd','tridstudio','20201230T151000','20201230T160000',-1)
    re.append(cl1)
    re.append(cl2)

    ClassWriter(re)
    

    