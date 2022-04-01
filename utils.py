import json
from collections import namedtuple
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

Credentials = namedtuple('Credentials','email password')
SmtpConfig = namedtuple('SmtpConfig','server_address port')
EmailData = namedtuple('EmailData','sender to subject body')

def readCredentials():
    f = open('configs/credentials.json')
    data = json.load(f)
    f.close()
    creds = Credentials(data['email'],data['password'])
    print(creds)
    return creds

def readSmtpConfig():
    f = open('configs/smtp_config.json')
    data = json.load(f)
    f.close()
    smtpConfig = SmtpConfig(data['server_address'],data['port'])
    return smtpConfig

def readEmail():
    f = open('configs/email.txt')
    msg = f.read()
    f.close()
    return msg

def readEmailData():
    f = open('configs/emailData.json')
    data = json.load(f)
    f.close()
    emailData = EmailData(data['from'], data['to'], data['subject'], data['body'])
    return emailData

def createMessage(emailData):
    msg = MIMEMultipart()
    msg['From'] = emailData.sender
    msg['To'] = emailData.to
    msg['Subject'] = emailData.subject

    msg.attach(MIMEText(emailData.body,'plain'))

    text = msg.as_string()
    return text