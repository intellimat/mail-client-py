import smtplib

server = smtplib.SMTP("smtp.gmail.com", 465)

server.ehlo()

server.login('','')