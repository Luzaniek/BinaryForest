from Tree import BinaryTreeNode, BinarySearchTreeNode


# node = BinaryTree(None)

def test_default_init():
    node = BinaryTreeNode(None, None, None)
    # N - Trzy warosci None
    assert node.left is None
    assert node.right is None
    assert node.data is None
    print ("Test NNN przeszedl")


def test_data_init():
    # D - jakas wartosc dla value
    # T - drzewo
    # N - None
    custom_data = 5
    custom_left = BinaryTreeNode()
    node = BinaryTreeNode(data=custom_data, left=custom_left, right=None)
    assert node.left == custom_left
    assert node.right == None
    assert node.data == custom_data
    print ("Test DTN przeszedl")


def test_none_tree_tree():
    custom_left = BinaryTreeNode()
    custom_right = BinaryTreeNode()
    node = BinaryTreeNode(None, custom_left, custom_right)
    assert node.left == custom_left
    assert node.right == custom_right
    assert node.data == None
    print ("Test NTT przeszedl")


def test_none_none_tree():
    custom_right = BinaryTreeNode()
    node = BinaryTreeNode(None, None, custom_right)
    assert node.data == None
    assert node.left == None
    assert node.right == custom_right
    print ("Test NNT przeszedl")


def test_none_tree_none():
    custom_left = BinaryTreeNode()
    node = BinaryTreeNode(None, custom_left, None)
    assert node.data == None
    assert node.left == custom_left
    assert node.right == None
    print ("Test NTN przeszedl")


def test_data_none_none():
    custom_data = 13
    node = BinaryTreeNode(custom_data, None, None)
    assert node.data == custom_data
    assert node.left == node.right == None
    print ("Test DNN przeszedl")


def test_data_tree_tree():
    custom_data = 13
    custom_left = BinaryTreeNode()
    custom_right = BinaryTreeNode()
    node = BinaryTreeNode(custom_data, custom_left, custom_right)
    assert node.data == custom_data
    assert node.left == custom_left
    assert node.right == custom_right
    print ("Test DTT przeszedl")
    print node.data
    print node.right


def test_no_data():
    node = BinarySearchTreeNode()
    assert node.left is None
    assert node.right is None
    assert node.data is None



test_default_init()
test_data_init()
test_none_tree_tree()
test_none_none_tree()
test_none_tree_none()
test_data_none_none()
test_data_tree_tree()

test_no_data()
nodeLeft = BinarySearchTreeNode(222, None, None)
nodeRight = BinarySearchTreeNode(333, None, None)
node = BinarySearchTreeNode(112, nodeLeft, nodeRight)
print (node.data)
print (node.left.data)

a = 77

node.add_val(a)
print (node.data)

node.add_left(BinaryTreeNode())
print (node.left)

node.add_right(BinaryTreeNode())
print (node.right)
