import os
import string
import platform
import sys

def get_valid_drives():

	valid_drives = []

	for drive in string.ascii_uppercase:
		drive += ":\\"
		if os.path.exists(drive):
			valid_drives.append(drive)

	return valid_drives

def file_search(find_file):

	drives = get_valid_drives()
	found_files = []

	for drive in drives:
		print(f"Searching {drive} drive")
		for root, directory, files in os.walk(drive):
			for file in files:
				if file == find_file:
					found_files.append(os.path.join(root, file))
		print(f"Completed searching {drive} drive \n")

	return found_files


def quit():
	print("Exiting program..")
	sys.exit()

def main():
	if platform.system() == "Windows":
		
		file = input("Enter filename to search (q to quit): ")
		if file == 'q':
			quit()

		else:
			found_files = file_search(file)

	if len(found_files) == 0:
		print("0 files found.")
	else:
		print("Files found: ")
		for file in found_files:
			print(file)

	print()
	print("Exiting program..")


if __name__ == "__main__":
	main()
