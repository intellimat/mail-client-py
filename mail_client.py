# Script to send emails using SMTP

import smtplib
import ssl
from utils import readCredentials, readEmailData, readSmtpConfig, createMessage

smtpConfig  = readSmtpConfig()
creds       = readCredentials()
emailData   = readEmailData()
recipient   = emailData.to

server  = smtplib.SMTP(smtpConfig.server_address, smtpConfig.port)
context = ssl.create_default_context()
server.starttls(context=context)

server.login(creds.email,creds.password)

msg = createMessage(emailData)
server.sendmail(creds.email, recipient, msg)
server.quit()
