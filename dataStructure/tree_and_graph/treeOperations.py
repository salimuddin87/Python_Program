class Node:
    """docstring for Node"""
    def __init__(self, value):
        #super(Node, self).__init__()
        self.value = value
        self.left = None
        self.right = None

class BSTree:
    """docstring for Tree"""
    def __init__(self):
        #super(Tree, self).__init__()
        self.root = None

    def createBST(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(value)
                        break
                elif value > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(value)
                        break
                else:
                    break
    
    def preorder(self):
        self.__preorder(self.root)

    def __preorder(self, current):
        if current != None:
            print(current.value, end=" ")
            self.__preorder(current.left)
            self.__preorder(current.right)

    def inorder(self):
        self.__inorder(self.root)

    def __inorder(self, current):
        if current != None:
            self.__inorder(current.left)
            print(current.value, end=" ")
            self.__inorder(current.right)

    def postorder(self):
        self.__postorder(self.root)

    def __postorder(self, current):
        if current != None:
            self.__postorder(current.left)
            self.__postorder(current.right)
            print(current.value, end=" ")

    def __heightOfTree(self, current):
        if current == None:
            return 0

        return (1 + max(self.__heightOfTree(current.left), 
                self.__heightOfTree(current.right)))

    def heightOfTree(self):
        return self.__heightOfTree(self.root)-1


if __name__ == '__main__':

    bst = BSTree()
    arr = [11,6,15,1,7,12,18]
    for item in arr:
        bst.createBST(item)

    print("\nPreorder traversal")
    bst.preorder()

    print("\nInorder traversal")
    bst.inorder()

    print("\nPostorder traversal")
    bst.postorder()

    print("\nHeight of Tree is {}".format(bst.heightOfTree()))