import os

from books import list_books
from config import MailerConfig
from draft import MailDraft
from server import MailingServer

import logging

if __name__ == "__main__":
	logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
	# Setup Configuration
	mailer_config = MailerConfig()

	logging.info("Mailer configured")
	# Get a list of all PDF docs in PWD
	files = list_books(mailer_config)
	total_files = len(files)

	# Setup SMTP Server
	smtp_server = MailingServer(mailer_config)

	# Mail all files
	for file_num in range(0,total_files):
		
		print("Sending file {} of {}\n{}".format(file_num+1,
		 	  total_files,
		 	  files[file_num])
			 )
		
		mail = MailDraft(files[file_num], mailer_config)
		mail_string = mail.get_mail_string()

		smtp_server.send_mail(mail_string)
		print("Sent")
		logging.info("file {} of {} sent".format(file_num+1,total_files))

		print("Deleting file {}".format(files[file_num]))
		os.remove(files[file_num])
		logging.info("file {} deleted".format(file_num+1))
		print("Deleted")


	smtp_server.destroy_server()
