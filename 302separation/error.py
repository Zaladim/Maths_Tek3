import os.path
from os import path


def usage():
	print("USAGE")
	print("\t./302separation file [n | p1 p2]")
	print("DESCRIPTION")
	print("\tfile\tfile that contains the list of Facebook connections")
	print("\tn\tmaximum length of the paths")
	print("\tpi\tname of someone in the file")
	return 0

def argError(argv):
	if len(argv) > 4 or len(argv) < 3:
		usage()
		return True
	if path.exists(argv[1]):
		return False
	usage()
	return True
	