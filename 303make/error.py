import os
from os import path


def usage():
	print("USAGE")
	print("\t./302make makefile [file]")
	print("DESCRIPTION")
	print("\tmakefile\tname of the makefile")
	print("\tfile\tname of a recently modified file")
	return 0

def argError(argv):
	if len(argv) == 1:
		usage()
		return True
	if path.exists(argv[1]):
		if os.stat(argv[1]).st_size > 0:
			return False
	usage()
	return True

def loopError(matrice):
	for i in range(len(matrice)):
		for j in range(len(matrice[0])):
			if matrice[j][i] == 1:
				if matrice[i][j] == 1:
					return 84


	