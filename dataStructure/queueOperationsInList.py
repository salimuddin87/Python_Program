from queue import Queue 

if __name__ == '__main__':
	q = Queue()
	#print(dir(q))
	q.put(1)
	q.put(2)
	q.put(3)
	q.put(4)

	print(q.get())
	print(q.get())
