#!/usr/bin/python
#Spikey Spammer
#Developed by Jagreet Das Gupta
#Author : V0!D
#Copyright : V!$(3R4
#Version : 1.1

#If you are reading this then you are a serious "Script Kiddie"

import smtplib
import sys
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders



def spam_mail(reci,username,password,message_body,mlserve,number,set_sub,files) :
	if mlserve == 'gmail':
	    smtp_serve = 'smtp.gmail.com'
	    port = 587
	elif mlserve == 'yahoo':
	    smtp_serve = 'smtp.mail.yahoo.com'
	    port = 25
	else:
	    print '~> Sorry, Current Script can only be Executed for Gmail and Yahoo'
	    sys.exit()

	print '\n!> Connecting To SMTP server...'

	try:
	    mlserve = smtplib.SMTP(smtp_serve,port) 
	    mlserve.ehlo()
	    if smtp_serve == "smtp.gmail.com":
	            mlserve.starttls()
	    mlserve.login(username,password)
	    print '\n!> Connection Established ! '
	    #MESSAGE DETAILS
	    print '\n----------Message Details-------------\n'
	    msg = MIMEMultipart()
	    msg['From'] = username
	    msg['To'] = reci
	    msg.attach(MIMEText(message_body))
	    print msg.as_string()
	    print '--------------------------------------'

	    print '\n-> Starting Up Executioner Style XD XD !!\n'
	    for i in range(1, number+1):
	    	if set_sub == 0:
	        	subject = os.urandom(9)
	        #message = 'From: ' + username + '\nSubject: ' + subject + '\n' + message_body
	        #msg['To'] = COMMASPACE.join(send_to)
	        msg = MIMEMultipart()
	    	msg['From'] = username
	    	msg['To'] = reci
	    	msg.attach(MIMEText(message_body))
	        msg['Subject:'] = subject
	        mlserve.sendmail(username,reci,msg.as_string())
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