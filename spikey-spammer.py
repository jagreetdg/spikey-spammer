#!/usr/bin/python
#Spikey Spammer
#Developed by Jagreet Das Gupta
#Author : V0!D
#Copyright : V!$(3R4
#Version : 1.1

#If you are reading this then you are a serious "Script Kiddie"

import getpass
import smtplib
import sys
import os

print '\nOUTPUT INFO : '
print '\n\'->\' before an output indicates it is a non-verbose log'
print '\n\'!>\' before an output indicates it is a verbose log'
print '\n\'~>\' before an output indicates it is an error log'
print '\n\'?>\' before an output indicates it is an input'
print '\n--------------------------------------------------'

#My Publicity :) :)
print '\n-> Spikey Spammer v1.1'
print '\n-> Developed by Jagreet Das Gupta'
print '\n-> Copyright : V!$(3R4'
print '\n'
print '----------------------------------------------------'
mlserve = raw_input ('?> Service Provider ? (gmail/yahoo) : ')
reci = raw_input('?> Recipient\'s Email: ')
username = raw_input('?> Sender\'s Email : ')
password = getpass.getpass('?> Sender\'s Password: ')
y = raw_input('?> Do you want to include a predefined subject ? (y/n)')
set_sub = 0
if y=='y':
	subject = raw_input('?> Subject: ') 
	set_sub = 1

message_body = raw_input('?> Message: ')
number = input('?> Number of messages to send: ')

if mlserve == 'gmail':
    smtp_serve = 'smtp.gmail.com'
    port = 587
elif mlserve == 'yahoo':
    smtp_serve = 'smtp.mail.yahoo.com'
    port = 25
else:
    print '~> Sorry, Current Script can only be Executed for Gmail and Yahoo'
    sys.exit()

print '\n-> Starting Up Executioner Style XD XD !'

try:
    mlserve = smtplib.SMTP(smtp_serve,port) 
    mlserve.ehlo()
    if smtp_serve == "smtp.gmail.com":
            mlserve.starttls()
    mlserve.login(username,password)
    for i in range(1, number+1):
    	if set_sub == 0:
        	subject = os.urandom(9)
        message = 'From: ' + sender_name + '\nSubject: ' + subject + '\n' + message_body
        mlserve.sendmail(sender_name,reci,message)
        print "\r!> E-Mail Packet Number #%i Sent..." % i
        sys.stdout.flush()
    mlserve.quit()
    print '\n-> Operation Executed Successfully !'
except KeyboardInterrupt:
    print '~> Operation Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n~> Error 404 : The username or password you entered is wrong, Please Try Again.'
    sys.exit()

#That's It....There's Nothing more...Go Now !
