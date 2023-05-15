class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def dfs(node):
    print(node.value)
    for child in node.children:
        dfs(child)


# Create a sample tree
root = Node(1)
root.add_child(Node(2))
root.add_child(Node(3))
root.children[0].add_child(Node(4))
root.children[0].add_child(Node(5))
root.children[1].add_child(Node(6))

# Perform a depth-first search traversal of the tree
dfs(root)
