class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def add_val(self, v):
        self.data = v

    def add_left(self, l):
        self.left = l

    def add_right(self, r):
        self.right = r



class BinarySearchTreeNode(BinaryTreeNode):
    pass
