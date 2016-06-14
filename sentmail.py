import smtplib

sender = 'jitendra.k@indictranstech.com'
receivers = ['khatrijitendra3@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test
This is a test e-mail message.
"""

try:
	smtpObj = smtplib.SMTP("mail.gmail.com", 587)
	smtpObj.sendmail(sender, receivers, message)         
	print "Successfully sent email"
except:
	print "Error: unable todomain send email"