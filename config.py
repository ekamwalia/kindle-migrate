# @TODO: Read config from config.json
class MailerConfig():

	def __init__(self):
		# SMTP Settings
		self.SMTP_HOST = "smtp.gmail.com"
		self.SMTP_PORT = 587

		# Sender mail settings
		self.SENDER_EMAIL_ADDRESS = "abhinavmathur2503@gmail.com"
		self.SENDER_EMAIL_PASSWORD = "abhinav2003"

		# Receiver mail settings
		self.RECEIVER_EMAIL_ADDRESS = "abhinavmathur2503@gmail.com"

		# Path to PWD
		self.BASE_PATH = "./"