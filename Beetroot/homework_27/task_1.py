class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def printTree(self):
        self._printTree(self, 0)

    def _printTree(self, node, level):
        if node is not None:
            print('  ' * level + str(node.key))
            self._printTree(node.leftChild, level + 1)
            self._printTree(node.rightChild, level + 1)

    def insertTreeLeft(self, newTree):
        if self.leftChild is None:
            self.leftChild = newTree
        else:
            t = BinaryTree(newTree)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertTreeRight(self, newTree):
        if self.rightChild is None:
            self.rightChild = newTree
        else:
            t = BinaryTree(newTree)
            t.rightChild = self.rightChild
            self.rightChild = t

    def removeSubtree(self, node):
        if self.leftChild == node:
            self.leftChild = None
        elif self.rightChild == node:
            self.rightChild = None
        else:
            if self.leftChild is not None:
                self.leftChild.removeSubtree(node)
            if self.rightChild is not None:
                self.rightChild.removeSubtree(node)

    def deleteLeftChild(self):
        if self.leftChild is not None:
            self.leftChild = None

    def deleteRightChild(self):
        if self.rightChild is not None:
            self.rightChild = None

    def deleteTree(self):
        self.leftChild = None
        self.rightChild = None

    def isLeaf(self):
        return self.leftChild is None and self.rightChild is None


# Создание дерева
tree = BinaryTree("a")
tree.insertLeft("b")
tree.insertRight("c")
tree.getLeftChild().insertRight("d")
tree.getRightChild().insertLeft("e")
tree.getRightChild().insertRight("f")

# Создание нового дерева
subtree = BinaryTree("x")
subtree.insertLeft("y")
subtree.insertRight("z")

# Вставка нового дерева в существующее дерево
tree.getLeftChild().insertTreeLeft(subtree)

# Печать всего дерева
tree.printTree()

# # Печать только левой ветки
# tree.getLeftChild().printTree()

# # Удаление правой ветки
# tree.deleteRightChild()
#
# # Удаление левого листа
# tree.getLeftChild().deleteRightChild()
#
# # Удаление всего дерева
# tree.deleteTree()
