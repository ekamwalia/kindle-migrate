from os import listdir
from os.path import isfile, join

from config import MailerConfig

def isPDF(filename):

	if not isfile(filename):
		return False

	extension = filename.split('.')[-1]
	if extension == 'pdf':
		return True

	return False


def list_books(mailer_config):
	base_path = mailer_config.BASE_PATH

	files = [file for file in listdir(base_path) 
			 if isPDF(join(base_path, file))
		    ]

	return files


