#!/usr/bin/python
#Spikey Spammer
#Developed by Jagreet Das Gupta
#Author : V0!D
#Copyright : V!$(3R4
#Version : 1.1

import getpass
from spikey_spammer import spam_mail

print '\nSCRIPT OUTPUT INFO : '
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
spam_mail(reci,username,password,message_body,mlserve,number,set_sub)