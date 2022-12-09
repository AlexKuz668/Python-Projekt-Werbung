import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version
def sendmessage(emails:list, message:str):
    server = 'smtp.mail.ru'
    user = 'okd88@inbox.ru'
    password = 'x0Ggv6bahjLmsJAdqbra'  # токен

    recipients = emails
    sender = 'okd88@inbox.ru'
    subject = 'Werbung'
    text = message

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Python project-Werbung <' + sender + '>' # Отправитель ( например, название компании)
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/' + (python_version())

    part_text = MIMEText(text, 'plain')

    msg.attach(part_text)

    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()