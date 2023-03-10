import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_server_ip = 'smtp.163.com'
mail_server_port = 25
mail_user = 'd3258169@163.com'
mail_pwd = 'CDRMKZHQLTSBTKKB'
sender = 'd3258169@163.com'
receivers = ['guoyu@fisksoft.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header(sender, 'utf-8')   # 发送者
message['To'] = Header(receivers[0], 'utf-8')        # 接收者

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_server_ip, mail_server_port)
    smtpObj.login(mail_user, mail_pwd)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件", e)
