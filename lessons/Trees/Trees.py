class TreeNode:
    """
    A class representing a node in a binary search tree.
    Attributes:
        data (int): The value stored in the node.
        left (TreeNode): The left child of the node.
        right (TreeNode): The right child of the node.
    """
    def __init__(self,data):
        """
        Initializes a new TreeNode with the given data.
        """
        self.left = None
        self.right = None
        self.data = data

    # Insertion operation
    def insert(self,data):
        """
        Inserts a new node with the given data into the tree.
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    # Search Operation
    def search(self,value):
        """
        Searches for the given value in the tree.
        """
        if(value < self.data):
            if self.data is None:
                return str(value) + "Not found, tree is empty"
            return self.left.search(value)
        elif value > self.data:
            if self.right is None:
                return str(value) + " not found"
            return self.right.search(value)
        else:
            print(str(self.data) + 'is found')

    #Inorder
    def inorder(self):
        """
        Prints the values in the tree in ascending order.
        """
        # Follow from left subtree to root to right subtree
        if self.left:
            self.left.inorder()
        
        print(self.data, " -> ",end=" ")

        if self.right:
            self.right.inorder()

    #Preorder
    def preorder(self):
        """
        Prints the values in the tree in pre-order.
        """
        # Follow from root to left subtree to right sub tree
        print(self.data)
        
        if(self.left):
            self.left.inorder()
        if(self.right):
            self.right.inorder()

    #Postorder
    def postorder(self):
        """
        Prints the values in the tree in post-order.
        """
        # Follow from right sub tree to left sub tree to finally root

        if(self.right):
            self.right.inorder()
        if(self.left):
            self.left.inorder()

        print (self.data)

treeNode1 = TreeNode(10)
treeNode1.insert(2)
treeNode1.insert(12)
treeNode1.insert(3)
treeNode1.insert(13)

treeNode1.search(2)
