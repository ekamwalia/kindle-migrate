import smtplib

from config import MailerConfig


class MailingServer():

	config = MailerConfig()


	# SMTP Server Setup
	def __init__(self, mailer_config):
		self.server = smtplib.SMTP(mailer_config.SMTP_HOST, mailer_config.SMTP_PORT)
		self.server.starttls()
		self.server.login(mailer_config.SENDER_EMAIL_ADDRESS, mailer_config.SENDER_EMAIL_PASSWORD)


	# Sends a mail to the Reciever address from config
	def send_mail(self, mail_body):
		self.server.sendmail(mailer_config.SENDER_EMAIL_ADDRESS,
							 mailer_config.RECEIVER_EMAIL_ADDRESS,
							 mailer_config.mail_body
							)

		return


	def destroy_server(self):
		self.server.quit()
		return
