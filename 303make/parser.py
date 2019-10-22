import error

def parser(file):
	dep = {}
	command = {}
	try:
		with open(file) as f:
			line = f.readline()
			act_dep = None
			while(line):
				if (':' in line):
					line = line.split()
					line[0] = line[0][:-1]
					if (line[0] not in dep):
						dep[line[0]] = []
					for i in range(1, len(line)):
						if (line[i] in dep):
							dep[line[i]].append(line[0])
						else:
							dep[line[i]] = [line[0]]
					act_dep = line[0]
				elif (act_dep):
					if (act_dep not in command):
						command[act_dep] = []
					line = line.rstrip()
					if line:
						command[act_dep].append(line)

				line = f.readline()

			node = list(dep.keys())
			node.sort()
			for item in node:
				dep[item].sort()
			if (error.loopError(matrice(dep, node)) == 84):
				return 84
			return dep, node, command, matrice(dep, node)
	except PermissionError:
		return 84

def matrice(dep, node):
	m = []
	for item in node:
		tmp = [0]*len(node)
		for child in dep[item]:
			tmp[node.index(child)] = 1
		m.append(tmp)
	return(m)

def dependency(dep, node):
	for item in node:
		if dep[item]:
			print_dep(dep, item)

def print_dep(dep, item, path=""):
	if not dep[item]:
		path += item
		print(path)
	else:
		path += item
		path += " -> "
		for child in dep[item]:
			print_dep(dep, child, path)

def print_matrice(m):
	for line in m:
		print("[", end='')
		for i in range(len(line) - 2):
			print(str(line[i]), end=' ')
		print(str(line[len(line) - 2]) + "]")
	print()