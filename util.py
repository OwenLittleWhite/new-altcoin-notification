from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def sendEmail(subject, *body):
    # 配置邮件
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = 'xx'
    message["Subject"] = subject
    for i in body:
        message.attach(MIMEText(i, "html"))
    # 连接到SMTP服务器并发送电子邮件
    with smtplib.SMTP("smtp.qq.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, 'xx', message.as_string())
    print("Email sent successfully!")
