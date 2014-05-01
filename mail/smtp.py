#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.header import Header
from base64 import encodebytes
import email
import mimetypes
import os
try:
    import ssl
except:
    print("Unsecured mail sending")

mail_from   = 'from@gmail.ru'	# отправитель
mail_to     = 'to@mail.ru'	# получатель
mail_text   = 'Тестовое письмо!\nПослано из python' # текст письма
mail_subj   = 'Тестовое письмо' # заголовок письма
mail_coding = 'utf-8'

#Параметры SMTP-сервера
smtp_server = "smtp.gmail.com"
smtp_port   = 587 #465 for smtp.yandex.ru
smtp_user   = "mail_send@gmail.com" # пользователь smtp
smtp_pwd    = "pwt_gmail"           # пароль smtp

isfile = os.path.isfile
exists = os.path.exists
basename = os.path.basename

def newMail(mail_from, mail_to, mail_subj, mail_text, attach_list=[], mail_coding='utf-8'):
    """формирование сообщения"""
    multi_msg = MIMEMultipart()
    multi_msg['From'] = Header(mail_from, mail_coding)
    multi_msg['To'] = Header(mail_to, mail_coding)
    multi_msg['Subject'] =  Header(mail_subj, mail_coding)

    msg = MIMEText(mail_text.encode('utf-8'), 'plain', mail_coding)
    msg.set_charset(mail_coding)
    multi_msg.attach(msg)

    # присоединяем атач-файл
    for _file in attach_list:
        if exists(_file) and isfile(_file):
            with open(_file, 'rb') as fl:
                attachment = MIMEBase('application', "octet-stream")
                attachment.set_payload(fl.read())
                email.encoders.encode_base64(attachment)
                only_name_attach = Header(basename(_file), mail_coding)
                attachment.add_header('Content-Disposition',\
                    'attachment; filename="%s"' % only_name_attach)
                multi_msg.attach(attachment)
        else:
            if(attach_file.lstrip() != ""):
                print("Файл для атача не найден - %s" %_file)
    return multi_msg

def Connection(smtp_server, smtp_port, smtp_user, smtp_pwd):
    """Создание соединения с сервером"""
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.ehlo()
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
        context.verify_mode = ssl.CERT_REQUIRED
        context.check_hostname = True
        context.load_default_certs()
        smtp.starttls(context=context)
    except:
        smtp.starttls()
    smtp.ehlo()
    try:
        smtp.login(smtp_user, smtp_pwd)
    except Exception as e:
        print(e)
    return smtp

def sendMail(smtp, mail_from, mail_to, msg):
    """Отправить сообщение msg через smtp= smtplib.SMTP()"""
    smtp.sendmail(mail_from, mail_to, msg.as_string())

if __name__ == '__main__':
    smtp_server = 'smtp.yandex.ru'
    smtp_port = 465
    smtp_user = 'yurias90'
    smtp_pwd = 'q4h@9l'
    smtp = Connection(smtp_server, smtp_port, smtp_user, smtp_pwd)
    attach_list = []
    mail = newMail(mail_from, mail_to, mail_subj, mail_text, attach_list, mail_coding)
    sendMail(smtp, mail_from, mail_to, mail)
    smtp.quit()
