# !PYTHON3
## Client.py - Responsible login the user in and

import Sender, DataSheet, Email

email 		= "@gmail.com"
password 	= ""
fileName 	= "contacts.xlsx"
subject 	= "Subject: \n"
body  		= "HELLO. I AM FROM APE. OOH...! OOH! OOH! AHH! AHH!"
attachments = list()

sender = Sender.Sender(email, password)

sheet = DataSheet.DataSheet(fileName)

print(sheet)

sheet = sheet.getData()
for row in sheet:
	email = Email.Email(sender, row["Email"], subject, body, attachments)
	print(email)
	email.sendEmail()