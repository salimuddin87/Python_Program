"""

Level 0               (a)
                     /   \
Level 1           (b)    (c)
                 /   \      \
Level 2        (d)   (e)    (f)

Input		Output
--------------------
  d 		  e
  e 		  d,f
--------------------  
"""

class Node:
	"""docstring for Node"""
	def __init__(self, value):
		#super(Node, self).__init__()
		self.left = None
		self.value = value
		self.right = None
		self.level = 0

def neighbourNode(root, s):
	nodeList = []
	queue = [root]

	while queue:
		currNode = queue.pop(0)
		#print(currNode.value, currNode.level)
		nodeList.append(currNode)

		if currNode.left != None:
			queue.append(currNode.left)
			currNode.left.level = currNode.level + 1

		if currNode.right != None:
			queue.append(currNode.right)
			currNode.right.level = currNode.level + 1

	# check for neighbour node
	neighbour = []
	for i in range(len(nodeList)):
		#print(nodeList[i].value)
		if nodeList[i].value == s:
			if i > 0:
				if nodeList[i-1].level == nodeList[i].level:
					neighbour.append(nodeList[i-1].value)
			if i < len(nodeList)-1:
				if nodeList[i+1].level == nodeList[i].level:
					neighbour.append(nodeList[i+1].value)

	return neighbour

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

	print(neighbourNode(root, 'e'))
