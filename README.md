# 合工大教务轮子 Python Ver.


## 使用须知
1. 从命令行形式启动 `main.py` ，初次使用请按照 `requirements.txt` 安装依赖库。
2. 支持 macOS/Windows , 自启动查询程序需要和另外的本地程序配合。
3. 为了调用 `Safari` 浏览器登陆，需要开启 `Safari` 的开发者功能，启用 **允许远程自动化**。
4. Windows 默认使用 `Chrome` 进行登陆与获取 Cookie ,请确保已经提前部署了浏览器驱动。

## 功能
* 📊 读取学生成绩，可以导出为 xlsx 表格文件
* 🤔 记录保存登陆状态，无需每次输入用户名和密码
* 📒 导出课表为 ics 文件，可导入至手机日历，以及添加提醒，再也不怕教务系统崩坏
* 🌝 提供外部接口可供调用，可供进行进一步开发

## 联系作者
你可以通过 Github 中的 issue ，或者联系邮箱：kimnotri@icloud.com。
不接受 IM 软件聊天🌝，有事请通过邮箱联系。

## 免责声明
软件可能随时因为外部系统的变更而无法使用或者是功能异常，开发者会尽可能进行适配或者修复，但开发者没有义务维护和修复软件的功能。并且，软件随时可能因为个人原因或外部不可抗力而停止维护和更新，使用该软件意味着我已经知晓上述事实。

## 更新日志

* Version 0.5.1

    * 对输出课表加入了课程前 5 分钟提醒的功能
    * 加强了程序的稳定性

* Version 0.5.0

    * 适配 `大学英语` 、 `信号与系统` 等课程，现在可以正常输出课表了
    * 现在可以无需输入课表的开始时间了
    * 现在导入的课表可以显示 `教学班` 、 `授课教师`及 `班级` 了
    * 加强了软件的可靠性
    * 修复了部分文字的显示问题

* Version 0.4.2(3)

    * 解除了对 Windows (NT) 系统的限制机制

* Version 0.4.2(2)

    * 修复了无法正确匹配课表资源的问题
    * 下一版本将对课表功能进行重构


* Version 0.4.2

    * 新增了 requirements.txt 供环境配置所需

* Version 0.4.1

    * 现在可以输出成绩及考试信息文件为 JSON 封存档了
    * 改善了程序的运行效率与稳定性

* Version 0.4.0

    * 新增了可以导出课程表为 ics 的功能
    * 后续的开源协议修改为 MIT


* Version 0.3.3

    * 现在可以正常获取课程表信息了
    * 增加了更多可供调用的接口

* Version 0.3.1

    * 修正了部分逻辑策略
    * 修复漏洞，加强了稳定性

* Version 0.3.0

    * 新增了在无网络情况/连接不顺畅下的智能提示
    * 开放了部分接口于 silentlistener 中
    * 精简了部分功能及文件
    * 支持了考试时间的查询功能
    * 追加了个人信息的清除功能
    * 改善了程序的稳定性

* Version 0.2.0

    * 新增了暂存 Cookie 功能，无需反复登陆
    * 成绩统计增加了按学期分类

* Version 0.1.5

    * 下个版本中，有关 Cookie 暂存的功能从 loginfunction 迁移至单独的 savestate
    * 修正了部分错误，加强了稳定性
    

* Version 0.1.4

    * 追加了暂存 Cookie 的功能，在一段时间内无需重新登陆（功能暂时还未完全完成）


* Version 0.1.3

    * 追加了查询学生考试信息的功能
    * 修复 BUG ，增强了稳定性

* Version 0.1.2

    * 修正了教务系统中无法获取到正确的成绩单查询地址的问题
    * 增强了稳定性

* Version 0.1

    挖了个大坑


