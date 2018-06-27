from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from config import MailerConfig


class MailDraft():
	

	def __init__(self, filename, mailer_config):

		# Create message
		self.message = MIMEMultipart()
		self.message['From'] = mailer_config.SENDER_EMAIL_ADDRESS
		self.message['To'] = mailer_config.SENDER_EMAIL_ADDRESS
		self.message['Subject'] = "Convert"

		# Attach file
		attachment = open(filename, "rb")

		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

		self.message.attach(part)

		return


	def get_mail_string(self):
		# Convert the message to a string
		return self.message.as_string()