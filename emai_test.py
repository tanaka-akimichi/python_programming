from email import message
from email.mime import multipart
from email.mime import text
import smtplib

smtp_host = 'smtp.ocn.ne.jp'
smtp_port = 587
from_email = 'akimichi@sepia.ocn.ne.jp'
to_email = 'a8ki1mi9chi@docomo.ne.jp'
user_name = 'akimichi@sepia.ocn.ne.jp'
password = 'fftg44'

# msg = message.EmailMessage()
msg = multipart.MIMEMultipart()
# msg.set_content('Test email.')

msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email
msg.attach(text.MIMEText('日本語の表示は問題ありませんか？', 'plain'))

with open('lesson.py', 'r') as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment',
        filename='lesson.py'
    )
    msg.attach(attachment)

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(user_name, password)
server.send_message(msg)
server.quit()



