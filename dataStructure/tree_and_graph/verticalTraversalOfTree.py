"""
Input:- [a, b, c, d, e, 0, f]

                   (a)0
                  /   \
             -1(b)    (c)1
              /   \      \
          -2(d)   0(e)    (f)2

Output:- [[d], [b], [a, e], [c], [f]]            
"""
#from collections import OrderedDict


class Node:
	"""docstring for Node"""
	def __init__(self, value):
		#super(Node, self).__init__()
		self.left = None
		self.value = value
		self.right = None
		self.visited = False

def verticalTraversal(root):
	res = []
	stack = [root]
	label = [0]

	currLabel = 0
	curr = root
	root.visited = True

	count = 0
	labelDict = dict()

	# Go left and save node and label
	while curr.left != None:
		curr = curr.left
		currLabel -= 1
		stack.append(curr)
		label.append(currLabel)
		curr.visited = True

	while stack:
		#print(res)
		item = stack.pop()
		currLabel = label.pop()
		if currLabel not in labelDict.keys():
			labelDict[currLabel] = count
			count += 1
			res.append([item.value])
		else:
			if currLabel < 0:
				res[labelDict[currLabel]].append(item.value)
			else:
				res[labelDict[currLabel]].insert(0, item.value)

		if item.right != None and not item.right.visited:
			currLabel += 1
			stack.append(item.right)
			label.append(currLabel)
			item.right.visited = True

		if item.left != None and not item.left.visited:
			currLabel -= 1
			stack.append(item.left)
			label.append(currLabel)
			item.left.visited = True

	print(labelDict)
	return res
	
if __name__ == "__main__":
	# create binary tree
	root = Node('a')
	# level 1 nodes
	root.left = Node('b')
	root.right = Node('c')

	# level 2 nodes
	root.left.left = Node('d')
	root.left.right = Node('e')
	root.right.right = Node('f')

	print(verticalTraversal(root))