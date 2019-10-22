import error

def start(argv):
	if (error.argError(argv)):
		return 84
	list = read(argv[1])
	if len(list) > 1:
		print(str(len(list)) + " elements")
	else:
		print("1 element")
	print("Selection sort: " + str(select(list)) + " comparisons")
	list = read(argv[1])
	print("Insertion sort: " + str(insert(list)) + " comparisons")
	list = read(argv[1])
	print("Bubble sort: " + str(bubble(list)) + " comparisons")
	list = read(argv[1])
	print("Quicksort: " + str(quick_sort(list)) + " comparisons")
	list = read(argv[1])
	print("Merge sort: " + str(fusion(list)) + " comparisons")

def read(file):
	try:
		f = open(file, "r")
	except (FileNotFoundError, PermissionError):
		print("Error with file")
		exit(84)
	str = f.read()
	lst = []
	num = ""
	try:
		for char in str:
			if char != ' ':
				num += char
			else:
				lst.append(float(num))
				num = ""
		lst.append(float(num))
	except ValueError:
		print("Error in file")
		exit(84)
	if lst == []:
		print("Empty file")
		exit(84)
	return lst

def select(list):
	cpt = 0
	for i in range(len(list)):
		min = i
		for j in range(i+1, len(list)):
			if (list[min] > list[j]):
				min = j
			cpt += 1
		tmp = list[i]
		list[i] = list[min]
		list[min] = tmp
	return cpt

def insert(list):
	count = 0
	for i in range(1, len(list)):
		for j in range(i):
			count += 1
			if list[j] > list[i]:
				elem = list.pop(i)
				list = list[:j] + [elem] + list[j:]
				break
	return count

def bubble(list):
	n = len(list)
	cpt = 0
	for i in range(n):
		for j in range(n - i - 1):
			cpt += 1
			if (list[j] > list[j + 1]):
				(list[j], list[i]) = (list[i], list[j])
	return cpt

def fusion(list):
	cpt = 0
	if len(list) > 1:
		mid = len(list)//2
		left = list[:mid]
		right = list[mid:]

		cpt += fusion(left)
		cpt += fusion(right)

		i = j = k = 0

		while i < len(left) and j < len(right):
			cpt += 1
			if left[i] < right[j]:
				list[k] = left[i]
				i+=1
			else:
				list[k] = right[j]
				j+=1
			k+=1

		while i < len(left):
			list[k] = left[i]
			i+=1
			k+=1

		while j < len(right):
			list[k] = right[j]
			j+=1
			k+=1
	return cpt

def partition(list, count):
	if (len(list) <= 1):
		return (list, count)
	pivot = list[0]
	(list_inf, list_sup) = ([], [])
	for l in list[1:]:
		count += 1
		if (l < pivot):
			list_inf.append(l)
		else:
			list_sup.append(l)
	l1, count = partition(list_inf, count)
	l2, count = partition(list_sup, count)
	return (list, count)

def quick_sort(list):
	(list, count) = partition(list, 0)
	return count
