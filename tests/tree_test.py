from structpy import bstree

tree = bstree()
tree.insert(8)
tree.insert(6)
tree.insert(10)
tree.insert(9)
tree.insert(12)

def test_inorder():
	assert(tree.inorder()==[6, 8, 9, 10, 12])

def test_prostorder():
	assert(tree.postorder()==[6, 9, 12, 10, 8])

def test_preorder():
	assert(tree.preorder()==[8, 6, 10, 9, 12])
