from Tree import BinaryTree


# node = BinaryTree(None)

def test_default_init():
    node = BinaryTree(None, None, None)
    # N - Trzy warosci None
    assert node.left is None
    assert node.right is None
    assert node.value is None
    print ("Test NNN przeszedl")


def test_data_init():
    # D - jakas wartosc dla value
    # T - drzewo
    # N - None
    custom_data = 5
    custom_left = BinaryTree()
    node = BinaryTree(value=custom_data, left=custom_left, right=None)
    assert node.left == custom_left
    assert node.right == None
    assert node.value == custom_data
    print ("Test DTN przeszedl")


def test_none_tree_tree():
    custom_left = BinaryTree()
    custom_right = BinaryTree()
    node = BinaryTree(None, custom_left, custom_right)
    assert node.left == custom_left
    assert node.right == custom_right
    assert node.value == None
    print ("Test NTT przeszedl")


def test_none_none_tree():
    custom_right = BinaryTree()
    node = BinaryTree(None, None, custom_right)
    assert node.value == None
    assert node.left == None
    assert node.right == custom_right
    print ("Test NNT przeszedl")


def test_none_tree_none():
    custom_left = BinaryTree()
    node = BinaryTree(None, custom_left, None)
    assert node.value == None
    assert node.left == custom_left
    assert node.right == None
    print ("Test NTN przeszedl")


def test_data_none_none():
    custum_data = 13
    node = BinaryTree(custum_data, None, None)
    assert node.value == custum_data
    assert node.left == node.right == None
    print ("Test DNN przeszedl")

def test_data_tree_tree():
    custum_data = 13
    custum_left = BinaryTree()
    custum_right = BinaryTree()
    node = BinaryTree(custum_data, custum_left, custum_right)
    assert node.value == custum_data
    assert node.left == custum_left
    assert node.right == custum_right
    print ("Test DTT przeszedl" )

test_default_init()
test_data_init()
test_none_tree_tree()
test_none_none_tree()
test_none_tree_none()
test_data_none_none()
test_data_tree_tree()