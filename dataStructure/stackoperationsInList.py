class stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, info):
		self.items.append(info)

	def pop(self):
		return self.items.pop()

	def top(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

	def display(self):
		print(self.items)

if __name__ == '__main__':
	status = True
	s = stack()
	while status:
		print("0. To exit from program")
		print("1. To check stack is empty")
		print("2. To push an item in stack")
		print("3. To pop an item from stack")
		print("4. To see top element of stack")
		print("5. To know the size of stack")
		print("6. To display the stack")

		x = int(input("Enter an integer "))
		if x == 0:
			status = False
		elif x == 1:
			print(s.isEmpty())
		elif x == 2:
			item = int(input("Enter an element for stack "))
			s.push(item)
		elif x == 3:
			print("%d is popped" % s.pop())
		elif x == 4:
			print("%d is top element" % s.top())
		elif x == 5:
			print("%d is size of stack" % s.size())
		elif x == 6:
			s.display()
		else:
			print("Wrong item entered")
