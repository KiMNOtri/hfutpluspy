import os
import requests

'''
    用于存储各种临时信息

    Version 0.1.6~ Cookie 保存功能迁移至此

'''

# 保存临时 Cookie 信息
def SaveCookieState(cookies):
    write_string = cookies['session'] + '/' + cookies['srvid']

    fo = open('cookiedata.archive','w')
    fo.write(write_string)

    fo.close()

    return


# 读取临时 Cookie 信息
def ReadCookieState():
        
    if(not os.path.exists("cookiedata.archive")):
        print("没有找到临时 Cookie 文件。")
        return -1

    fr = open('cookiedata.archive')
    read_string = fr.read()

    print(read_string)

    cookiedata = read_string.split('/')

    cookies = {'session':cookiedata[0],'srvid':cookiedata[1]}

    return cookies


# 验证 Cookie 是否有效
def VerifyCookieState(cookies):

    session_value = cookies['session']
    srvid_value = cookies['srvid']

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

    resp = requests.get('http://jxglstu.hfut.edu.cn/eams5-student/home',headers=myheaders,allow_redirects=False)


    print(resp.status_code)

    if(resp.status_code==302):
        return False
    
    return True

