import os
import string

def get_valid_drives():

	valid_drives = []

	for drive in string.ascii_uppercase:
		drive += ":\\"
		if os.path.exists(drive):
			valid_drives.append(drive)

	return valid_drives