from Tree import BinaryTree


#node = BinaryTree(None)

def test_default_init():
    node = BinaryTree(None, None, None)
    print ("Test NNN")
    #N - Trzy warosci None
    assert node.left is None
    assert node.right is None
    assert node.value is None
    print ("Test NNN przeszedl")


def test_data_init():

    print ("Test DTN:")
    #D - jakas wartosc dla value
    #T - drzewo
    #N - None
    custom_data = 5
    custom_left = BinaryTree()
    node = BinaryTree(value=custom_data, left = custom_left, right = None )
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



test_default_init()
test_data_init()
test_none_tree_tree()