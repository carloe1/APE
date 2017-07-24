#! PYTHON3
# Sender.py - Class containing all sender information

class Sender:

	def __init__(self, emailAddress, password):
		self.address = emailAddress
		self.password = password
		self.port = 587
		self.server = "smtp.gmail.com"

	def __str__(self):
		return self.address

	def __repr__(self):
		return self.address

	## GETTER METHODS ================================
	def getServerName(self):
		return self.server

	def getServerPort(self):
		return self.port

	def getEmailAddress(self):
		return self.address

	def getPassword(self):
		return self.password