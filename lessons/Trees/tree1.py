class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, key_value):
        # Comparing value to insert and the parent node
        if key_value < self.value:
            # Checking if it is none. If it is you insert a value
            if self.left is None:
                self.left = TreeNode(key_value)
            else:
                self.left.insert(key_value)
        # If it is greater than self.value, on the right side
        else:
            if self.right is None:
                self.right = TreeNode(key_value)
            else:
                self.right.insert(key_value)
                
    # Checking the traversals
    def preorder_traversal(self):
        """
        Preorder: Root -> Left -> Right
        Like reading a book from top to bottom, left to right
        """
        print(self.value)  # Visit root first
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
    
    # Looping through binary tree and when we find a value we print it
    def inorder_traversal(self):
        """
        Inorder: Left -> Root -> Right
        This visits nodes in sorted order for a BST
        """
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def post_order_traversal(self):
        """
        Postorder: Left -> Right -> Root
        Like cleaning up - deal with children before parent
        """
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.value)  # Visit root last

    def search(self, target):
        """
        Search for a value in the BST
        Like looking for a book in a library - go left if smaller, right if larger
        """
        if self.value == target:
            return True
        elif target < self.value:
            if self.left:
                return self.left.search(target)
            else:
                return False
        else:
            if self.right:
                return self.right.search(target)
            else:
                return False

    def find_min(self):
        """
        Find the minimum value in the tree
        Keep going left until you can't anymore
        """
        current = self
        while current.left:
            current = current.left
        return current.value

    def find_max(self):
        """
        Find the maximum value in the tree
        Keep going right until you can't anymore
        """
        current = self
        while current.right:
            current = current.right
        return current.value

    def height(self):
        """
        Calculate the height of the tree
        Like measuring how many floors a building has
        """
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)

    def display(self, level=0, prefix="Root: "):
        """
        Visual representation of the tree
        Like drawing a family tree sideways
        """
        if self.right:
            self.right.display(level + 1, "R--- ")
        print(" " * (level * 4) + prefix + str(self.value))
        if self.left:
            self.left.display(level + 1, "L--- ")


if __name__ == "__main__":
    # Create a binary search tree with root value 17
    tree_obj = TreeNode(17)
    
    # Insert some values to build the tree
    values_to_insert = [10, 25, 5, 15, 20, 30, 3, 7, 12, 18]
    
    print("Building the tree...")
    for value in values_to_insert:
        tree_obj.insert(value)
    
    print("\nTree structure:")
    tree_obj.display()
    
    print("\nPreorder traversal (Root -> Left -> Right):")
    tree_obj.preorder_traversal()
    
    print("\nInorder traversal (Left -> Root -> Right) - sorted order:")
    tree_obj.inorder_traversal()
    
    print("\nPostorder traversal (Left -> Right -> Root):")
    tree_obj.post_order_traversal()
    
    print(f"\nTree height: {tree_obj.height()}")
    print(f"Minimum value: {tree_obj.find_min()}")
    print(f"Maximum value: {tree_obj.find_max()}")
    
    # Test searching
    test_values = [15, 100, 5]
    for val in test_values:
        found = tree_obj.search(val)
        print(f"Searching for {val}: {'Found' if found else 'Not found'}")