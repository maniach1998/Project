import smtplib
smtpUser = 'sagarraspproject@gmail.com'
smtpPass = 'sagarrasp'


def check_email(email):
	if email[-10:]=="@gmail.com":
		return "VALID"
	else:
		return "INVALID"

def send_mail(emailid,content):
	s= smtplib.SMTP('smtp.gmail.com',587)
	toAdd = emailid
	fromAdd= smtpUser
	
	subject ='Restaurant Bill(project)'
	header ='To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' +'Subject: '+subject
	body = content
	
	print(header + '\n' + body)
	
	s.starttls()
	
	s.login(smtpUser,smtpPass)
	s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

	s.quit() 
	
