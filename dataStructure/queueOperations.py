"""
from queue import Queue 

if __name__ == '__main__':
	q = Queue()
	print(dir(q))

"""

class Node:
	"""docstring for Node"""
	def __init__(self, arg):
		#super(Node, self).__init__()
		self.arg = arg
		self.left = None
		self.right = None

class Queue:
	"""docstring for Queue"""
	def __init__(self):
		#super(Queue, self).__init__()
		self.front = None
		self.rear = None

	def enQueue(self, value):
		tempNode = Node(value)
		if self.rear == None:
			self.front = self.rear = tempNode
		else:
			self.rear.right = tempNode
			tempNode.left = self.rear
			self.rear = tempNode

	def deQueue(self):
		if self.front == None:
			return ("Queue is empty!")
		else:
			temp = self.front.arg
			self.front = self.front.right
			return temp

	def displayQueue(self):
		res = []
		curr = self.front
		while curr != self.rear:
			res.append(curr.arg)
			curr = curr.right
		res.append(curr.arg)
		print(res)

if __name__ == "__main__":
	q = Queue()
	q.enQueue(1)
	q.enQueue(2)
	q.enQueue(3)
	q.displayQueue()
	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue())