# coding:utf-8
__author__ = 'Xu'
# 'Xu'
import smtplib
from email.mime.text import MIMEText


class SendEmail:
    def send_mail(self, user_list, sub, content):
        global send_user
        global email_host
        global password

        email_host = "smtp.163.com"
        send_user = "18245454375@163.com"
        password = "xujingbo1995"
        user = "Xu" + "<" + send_user + ">"

        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)

        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def send_main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num

        pass_result = "%.2f%%"%(pass_num/count_num*100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)

        user_list = ['18245454375@163.com']
        sub = "接口自动化测试报告"
        content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s个,通过率为%s,失败率为%s" % (count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_mail(user_list, sub, content)

if __name__ == '__main__':
    send = SendEmail()
    send.send_main([1, 2, 3, 4],[5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
