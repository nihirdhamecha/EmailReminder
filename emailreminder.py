import smtplib
import requests
import json
response = requests.get("https://api.quotable.io/random")


t = response.json()
c = t['content']
q = t['author']
test = c+"\n\n~"+q+"\n\n"
print(test)




gmail_user = 'xyz@gmail.com[your email]'
gmail_password = '****[your password]'

sent_from = gmail_user
to = ['abc@gmail.com'] #list of recivers
subject = 'READy to READ'
body = test

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
