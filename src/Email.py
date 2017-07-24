#! PYTHON3
## SendEmails.py - Send Personal Email to Clients

import sys
import openpyxl
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


class Email:

	def __init__(self, sender, recipient, subject, body, attachments):

		self.message = MIMEMultipart()
		self.message["To"] 		= recipient
		self.message["From"] 	= sender.getEmailAddress()
		self.message["subejct"]	= subject

		self.sender 	= sender
		self.attachments = attachments

	def sendEmail(self):
		#print("smpt")
		smtpObj = smtplib.SMTP(self.sender.getServerName(), self.sender.getServerPort(), timeout=30)
		#print("ehlo")
		smtpObj.ehlo()
		#print("starttls")
		smtpObj.starttls()
		#print("login")
		smtpObj.login(self.sender.getEmailAddress(), self.sender.getPassword())
		#print("sending email..")
		smtpObj.sendmail(self.sender.getEmailAddress(), self.recipient, self.subject + self.body)
		#print("Messagesent")
		smtpObj.quit()

	def __str__(self):
		emailString = "To: " + self.recipient + "\n"
		emailString += "From: " + self.sender.getEmailAddress() + "\n"
		emailString += self.subject + "\n"
		emailString += "Body =======================\n"
		emailString += self.body + "\n"
		emailString += "=============================\n"
		emailString += "Attachemnts==================\n"
		for attachment in self.attachments:
			emailString += attachement + "\n"
		emailString += "==============================\n"

		return emailString

	def __repr__(self):
		emailString = "To: " + self.recipient + "\n"
		emailString += "From: " + self.sender + "\n"
		emailString += self.subject + "\n"
		emailString += "Body =======================\n"
		emailString += self.body + "\n"
		emailString += "=============================\n"
		emailString += "Attachemnts==================\n"
		for attachment in self.attachements:
			emailString += attachment + "\n"
		emailString += "==============================\n"

		return emailString