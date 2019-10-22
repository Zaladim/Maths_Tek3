import error

def parser(file):
	people = []
	try:
		with open(file) as f:
			line = f.readline()
			while (line):
				name = ""
				size = 0
				for word in line.split():
					if (word == "is"):
						if (name) not in people:
							people.append(name)
						name = line.split(' ',size +  3)[size + 3].rstrip("\n\r")
						if (name) not in people:
							people.append(name)
						break
					if (name):
						name += " "
					name += word
					size += 1
				
				line = f.readline()
		people.sort()
		return people, adjacency(file, people)
	except PermissionError:
		error.usage()
		return 84

def adjacency(file, people):
	inf = len(people) + 1
	m = set_m(len(people))

	with open(file) as f:
		line = f.readline()
		while (line):
			name = ""
			size = 0
			x = -1
			y = -1
			for word in line.split():
				if (word == "is"):
					x = people.index(name)
					name = line.split(' ',size +  3)[size + 3].rstrip("\n\r")
					y = people.index(name)
					break
				if (name):
					name += " "
				name += word
				size += 1

			m[x][y] = 1
			m[y][x] = 1
			line = f.readline()

		# for i in range(len(m)):
		# 	for j in range(len(m[i])):
		# 		if m[i][j] == 0:
		# 			m[i][j] = inf
		return m

def set_m(nb):
	m = []
	for i in range(nb):
		tmp = []
		for j in range(nb):
			tmp.append(0)
		m.append(tmp)
	return m

def peoples(list):
	for name in list:
		print(name)

def matrice(m):
	for line in m:
		for i in range(len(line)):
			print(line[i], end='')
			if (i + 1 >= len(line)):
				print("")
			else:
				print("", end = ' ')
		# for elem in line:
		# 	print(elem, end=' ')
		# print("")
		
			
	return 0