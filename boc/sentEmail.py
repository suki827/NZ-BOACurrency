import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(body, recipient_email,subject='新西兰实时汇率'):
    """
    发送邮件的函数
    :param subject: 邮件主题
    :param body: 邮件正文
    :param recipient_email: 收件人邮箱地址
    """
    smtp_server = 'smtp.qq.com'  # QQ邮箱SMTP服务器地址
    smtp_port = 465  # QQ邮箱SMTP端口
    email_address = '625506030@qq.com'  # 发送者的QQ邮箱地址
    email_password = 'tpozldvwquqvbfhj'  # QQ邮箱的授权码
    # 创建邮件
    message = MIMEMultipart()
    message['From'] = email_address
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain', 'utf-8'))

    # 发送邮件
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(email_address, email_password)
            server.sendmail(email_address, recipient_email, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPResponseException as e:
        if e.smtp_code == -1 and e.smtp_error == b'\x00\x00\x00':
            print("邮件发送成功，但收到了意外的响应，可以忽略。")
        else:
            print(f"邮件发送失败: {e}")
    except Exception as e:
        print(f"邮件发送失败: {e}")


# 程序入口
if __name__ == "__main__":
    # 示例调用
    subject = "测试邮件"
    body = "这是一封通过 Python 发送的测试邮件。"
    recipient_email = 'hugo.huan@outlook.com'

    # 调用函数发送邮件
    send_email(body, recipient_email)
