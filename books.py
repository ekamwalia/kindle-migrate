from os import listdir
from os.path import isfile, join

import logging

from config import MailerConfig

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def isPDF(filename):

	if not isfile(filename):
		logging.warning("file {} doesn't exist".format(filename))
		return False

	extension = filename.split('.')[-1]
	if extension == 'pdf':
		return True
	logging.warning("file {} is not of type pdf".format(filename))
	return False


def list_books(mailer_config):
	base_path = mailer_config.BASE_PATH

	files = [file for file in listdir(base_path) 
			 if isPDF(join(base_path, file))
		    ]

	return files


