import smtplib
import requests
import json





gmail_user = 'xyz@gmail.com[your email]'
gmail_password = '****[your password]'

sent_from = gmail_user
to = ['abc@gmail.com'] #list of recivers
subject = 'READy to READ'
body = 'Time to read boy!'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')
