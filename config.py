# @TODO: Read config from config.json
class MailerConfig():

	def __init__(self):
		# SMTP Settings
		self.SMTP_HOST = "smtp.gmail.com"
		self.SMTP_PORT = 587

		# Sender mail settings
		self.SENDER_EMAIL_ADDRESS = ""
		self.SENDER_EMAIL_PASSWORD = ""

		# Receiver mail settings
		self.RECEIVER_EMAIL_ADDRESS = "<username>@kindle.com"

		# Path to PWD
		self.BASE_PATH = ""