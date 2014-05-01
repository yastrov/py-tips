#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import imaplib
import email
from email.header import decode_header
from email.base64mime import body_decode
from email.utils import decode_rfc2231
import ssl
 
server = "imap.yandex.ru"
port = "993" # 993 yandex
login = "login"
password = "pass"

context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

mail= None
try:
    mail= imaplib.IMAP4_SSL(server, port, ssl_context=context)
except:
    mail= imaplib.IMAP4(server, port)
    print("No SSL :(")
 
mail.login(login, password)
 
mail.select() # выбираем папку, по умолчанию - INBOX
# result, data = mail.uid('search', None, "ALL") # search and return uids instead
result, data = mail.search(None, 'ALL') # ищем письма
#Search in header
#mail.uid('search', None, '(HEADER Subject "My Search Term")')
#mail.uid('search', None, '(HEADER Received "localhost")')
#result, data = mail.uid('search', None, '(SENTSINCE {date} HEADER Subject "My Subject" NOT FROM "yuji@grovemade.com")'.format(date=date))
# None здесь говорит о том, что нам всё равно, в какой кодировке искать письма
# ALL - искать все письма
# search(None, 'FROM', '"LDJ"') или search(None, '(FROM "LDJ")') - искать письма со строкой LDJ в поле From
 
for num in data[0].split() :
    result, data = mail.fetch(num, '(RFC822)')
    # result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    print('---------------------------\n')
    #print('Message %sn%sn' % (num, data[0][1]))
    raw_email = data[0][1]
    #email_message = email.message_from_string(str(raw_email))
    email_message = email.message_from_bytes(raw_email)
    print(email_message['To'])
    print(email.utils.parseaddr(email_message['From']))
    print(email_message['Subject'])
    #print(email_message.items()) # print all headers
    if isinstance(email_message.get_payload(), list):
        for eachPayload in email_message.get_payload():
            #...do things you want...
            #...real mail body is in eachPayload.get_payload()...
            eachPayload.get_payload(decode=True)
    else:
        #...means there is only text/plain part....
        #...use email_message.get_payload() to get the body...
        r = email_message.get_payload(decode=True)

# note that if you want to get text content (body) and the email contains
# multiple payloads (plaintext/ html), you must parse each message separately.
# use something like the following: (taken from a stackoverflow post)
def get_first_text_block(self, email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()

# Delete
#mail.store(num, '+FLAGS', r'\Deleted')
#mail.expunge()
##

mail.close()
mail.logout()
