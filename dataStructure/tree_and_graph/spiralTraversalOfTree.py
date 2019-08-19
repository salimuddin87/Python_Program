class Node:
    """docstring for Node"""
    def __init__(self, arg):
        #super(Node, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None

def spiralTraversal(root):
    # 1 2 3 7 6 5 4
    s1 = [root]
    s2 = []
    leftToRight = True

    while s1:
        #pop top element from stack
        item = s1.pop(0)
        print item.arg ,

        if leftToRight:
            if item.right != None:
                s2.insert(0, item.right)
            if item.left != None:
                s2.insert(0, item.left)
        else:
            if item.left != None:
                s2.insert(0, item.left)
            if item.right != None:
                s2.insert(0, item.right)

        # swap s1 and s2 when s1 is empty
        if s1 == []:
            if leftToRight:
                leftToRight = False
            else:
                leftToRight = True
            s1 = s2
            s2 = []


if __name__ == '__main__':
    # Level 0
    root = Node('1')

    # Level 1
    root.left = Node('2')
    root.right = Node('3')

    # Level 2
    root.left.left = Node('4')
    root.left.right = Node('5')
    root.right.left = Node('6')
    root.right.right = Node('7')

    spiralTraversal(root)