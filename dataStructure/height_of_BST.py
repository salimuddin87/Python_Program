class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    NodeObj = root
    if NodeObj.left != None and NodeObj.right != None:
        return 1 + max(height(NodeObj.left), height(NodeObj.right))

    elif NodeObj.left != None and NodeObj.right == None:
        return 1 + height(NodeObj.left)

    elif NodeObj.left == None and NodeObj.right != None:
        return 1 + height(NodeObj.right)

    else:
        return 0

tree = BinarySearchTree()
t = int(raw_input("Enter no of elements : "))

arr = list(map(int, raw_input("Enter array element : ").split()))

for i in xrange(t):
    tree.create(arr[i])

print height(tree.root)

