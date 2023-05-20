class BinaryTree:
    def __init__(self, root_object):
        """
        Initialize a binary tree with a root object.
        """
        self.key = root_object
        self.left_child = None
        self.right_child = None

    def insert_left_node(self, new_node):
        """
        Insert a new node as the left child of the current node.
        """
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = t

    def insert_right_node(self, new_node):
        """
        Insert a new node as the right child of the current node.
        """
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = t

    def get_left_child(self):
        """
        Get the left child of the current node.
        """
        return self.left_child

    def get_right_child(self):
        """
        Get the right child of the current node.
        """
        return self.right_child

    def set_root_value(self, new_key):
        """
        Set the value of the current node.
        """
        self.key = new_key

    def get_root_value(self):
        """
        Get the value of the current node.
        """
        return self.key

    def is_leaf(self):
        """
        Check if the current node is a leaf node (has no children).
        """
        return self.left_child is None and self.right_child is None

    def has_left_child(self):
        """
        Check if the current node has a left child.
        """
        return self.left_child is not None

    def has_right_child(self):
        """
        Check if the current node has a right child.
        """
        return self.right_child is not None

    def preorder_traversal(self):
        """
        Perform a preorder traversal of the binary tree.
        """
        result = [self.key]
        if self.left_child:
            result.extend(self.left_child.preorder_traversal())
        if self.right_child:
            result.extend(self.right_child.preorder_traversal())
        return result

    def inorder_traversal(self):
        """
        Perform an inorder traversal of the binary tree.
        """
        result = [self.key]
        if self.left_child:
            result.extend(self.left_child.inorder_traversal())  # Traverse left subtree
        if self.right_child:
            result.extend(self.right_child.inorder_traversal())  # Traverse right subtree
        return result

    def postorder_traversal(self):
        """
        Perform a postorder traversal of the binary tree.
        """
        result = [self.key]
        if self.left_child:
            result.extend(self.left_child.postorder_traversal())  # Traverse left subtree
        if self.right_child:
            result.extend(self.right_child.postorder_traversal())  # Traverse right subtree
        return result

    def add_subtree(self, subtree):
        """
        Add a subtree to the current node. If a child is already occupied, raise an exception.
        """
        if self.left_child is None:
            self.left_child = subtree
        elif self.right_child is None:
            self.right_child = subtree
        else:
            raise ValueError("Both left and right child are already occupied")

    def print_tree(self):
        """
        Print the binary tree structure with a visual representation.
        """
        self._print_tree_recursive(self, level=0, position='C')  # C for Tree root

    def _print_tree_recursive(self, node, level, position):
        """
        Recursive helper method to print the binary tree structure.
        """
        if node is None:
            return

        prefix = '|   ' * level  # Prefix for indentation

        # Print information about the current node
        print(f'{prefix}|- [{position}] {node.get_root_value()}')

        # Print the left subtree
        if node.get_left_child():
            self._print_tree_recursive(node.get_left_child(), level + 1, 'L')  # Left child

        # Print the right subtree
        if node.get_right_child():
            self._print_tree_recursive(node.get_right_child(), level + 1, 'R')  # Right child

    def remove_left_child(self):
        """
        Remove the left child of the current node.
        """
        if self.left_child is not None:
            self.left_child = None

    def remove_right_child(self):
        """
        Remove the right child of the current node.
        """
        if self.right_child is not None:
            self.right_child = None

    def shift_alt_child(self, existing_value, new_child):
        """
        Shift the alternative child by replacing its value and rearranging the hierarchy.
        """
        if self.key == existing_value:
            old_node = BinaryTree(existing_value)
            old_node.left_child = self.left_child
            old_node.right_child = self.right_child
            self.key = new_child
            self.left_child = old_node
            self.right_child = None
        elif self.left_child is not None and self.left_child.get_root_value() == existing_value:
            old_node = BinaryTree(existing_value)
            old_node.left_child = self.left_child.left_child
            old_node.right_child = self.left_child.right_child
            self.left_child.key = new_child
            self.left_child.left_child = old_node
            self.left_child.right_child = None
        elif self.right_child is not None and self.right_child.get_root_value() == existing_value:
            old_node = BinaryTree(existing_value)
            old_node.left_child = self.right_child.left_child
            old_node.right_child = self.right_child.right_child
            self.right_child.key = new_child
            self.right_child.left_child = old_node
            self.right_child.right_child = None
        else:
            raise ValueError("Cannot find alt child")

    def remove_value(self, value):
        """
        Remove a specific value from the binary tree and replace the hierarchy accordingly.
        """
        if self.key == value:
            if self.left_child:
                self._replace_subtree(self.left_child)
            elif self.right_child:
                self._replace_subtree(self.right_child)
            else:
                # The current node is a leaf node, simply remove it
                self.key = None
                self.left_child = None
                self.right_child = None
        elif self.left_child and self.left_child.key == value:
            self.left_child = None
        elif self.right_child and self.right_child.key == value:
            self.right_child = None
        else:
            if self.left_child:
                self.left_child.remove_value(value)
            if self.right_child:
                self.right_child.remove_value(value)

    def _replace_subtree(self, subtree):
        """
        Replace the current node with the given subtree.
        """
        self.key = subtree.key
        self.left_child = subtree.left_child
        self.right_child = subtree.right_child
