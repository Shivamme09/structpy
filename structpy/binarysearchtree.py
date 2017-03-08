"""
Implementation of Binary Search Tree.
"""

class Node:
	"""
	This class will have four fields.
	"""
	def __init__(self, data):
		self.data = data
		self.parent = None
		self.leftChild = None
		self.rightChild = None
		
class bstree:
	"""
	This is the base class for binay search tree.
	"""
	def __init__(self):
		self._root = None

		
	def insert(self, data):
		"""
		Insert a node in the binary tree.
		"""

		self._node = Node(data)
		if self._root == None:	
			self._root = self._node
			
		else:
			currentNode = self._root
			while True:
				if data < currentNode.data:
					#Traversing left
					if currentNode.leftChild is None:
						currentNode.leftChild = self._node
						self._node.parent = currentNode
						return
					currentNode = currentNode.leftChild
				
				else:
					#Traversing right
					if currentNode.rightChild is None:
						currentNode.rightChild = self._node
						self._node.parent = currentNode
						return
					currentNode = currentNode.rightChild

					
	def successor(self, item):
		"""
		Return next node larger than the item.
		"""
		self._item = item
		currentNode = self._root
		while currentNode is not None:
			if currentNode.data == self._item:
				if currentNode.rightChild is None:
					return None
				else:
					right_node = currentNode.rightChild
					if right_node.leftChild is None:
						return right_node.data
					else:
						return right_node.leftChild.data
			elif currentNode.data < self._item:
				#Go right
				currentNode = currentNode.rightChild
			else:
				#Go left
				currentNode = currentNode.leftChild
		return None

		
	def remove(self, item):
		"""
		Removes and returns the item from the tree.
		"""
		self._item = item
		currentNode = self._root

		def delete_none_child(node):
			"""
			Delete the node with no childeren
			"""
			if node==node.parent.leftChild:
				node.parent.leftChild = None
			else:
				node.parent.rightChild = None

		def delete_single_child(node):
			"""
			Delete the node with only one child
			"""
			if node.leftChild:
				if node.parent.leftChild==node:
					node.parent.leftChild = node.leftChild
				else:
					node.parent.rightChild = node.leftChild
			else:
				if node.parent.leftChild==node:
					node.parent.leftChild = node.rightChild
				else:
					node.parent.rightChild = node.rightChild

		def delete_both_child(node):
			"""
			Delete the node with both the child
			"""
			cr_node = node
			while cr_node.leftChild is not None:
				cr_node = cr_node.leftChild
			if node.parent.leftChild==node:
				node.parent.leftChild.data = cr_node.data
			else:
				node.parent.rightChild.data = cr_node.data

			if cr_node.leftChild is None and cr_node.rightChild is None:
				delete_none_child(cr_node)
			else:
				delete_single_child(cr_node)

		while currentNode is not None:
			if currentNode.data==self._item:
				if currentNode.leftChild is None and currentNode.rightChild is None:
					delete_none_child(currentNode)
					return
				elif currentNode.leftChild is not None and currentNode.rightChild is not None:
					delete_both_child(currentNode)
					return
				else:
					delete_single_child(currentNode)
					return
			elif currentNode.data>self._item:
				currentNode = currentNode.leftChild
			else:
				currentNode = currentNode.rightChild


	def find(self, key):
		"""
		Search the tree for the key. Return True if found else False.
		"""

		self._key = key
		currentNode = self._root
		while currentNode is not None:
			if self._key == currentNode.data:
				return True
			elif self._key < currentNode.data:
				currentNode = currentNode.leftChild
			else:
				currentNode = currentNode.rightChild
		return False

		
	def find_min(self):
		"""
		Returns the node with minimum value
		"""
		currentNode = self._root
		while currentNode is not None:
			if currentNode.leftChild is None:
				return currentNode.data
			currentNode = currentNode.leftChild

	
	def find_max(self):
		"""
		Returns the node with maximum value
		"""
		currentNode = self._root
		while currentNode is not None:
			if currentNode.rightChild is None:
				return currentNode.data
			currentNode = currentNode.rightChild


	def preorder(self):
		"""
		Traverse Root-leftChild-rightChild.
		"""
		root = self._root

		def preorder_traverse(root):
			if root.leftChild is None and root.rightChild is None:
				return [root.data]

			if root.leftChild is not None and root.rightChild is None:
				return [root.data]+preorder_traverse(root.leftChild)
			elif root.leftChild is None and root.rightChild is not None:
				return [root.data]+preorder_traverse(root.rightChild)
			else:
				return [root.data]+preorder_traverse(root.leftChild)+preorder_traverse(root.rightChild)

		return preorder_traverse(root)


	def inorder(self):
		"""
		Traverse leftChild-Root-rightChild.
		"""
		root = self._root

		def inorder_traverse(root):
			if root.leftChild is None and root.rightChild is None:
				return [root.data]

			if root.leftChild is not None and root.rightChild is None:
				return inorder_traverse(root.leftChild)+[root.data]
			elif root.leftChild is None and root.rightChild is not None:
				return [root.data]+inorder_traverse(root.rightChild)
			else:
				return inorder_traverse(root.leftChild)+[root.data]+inorder_traverse(root.rightChild)

		return inorder_traverse(root)


	def postorder(self):
		"""
		Traverse leftChild-rightChild-root.
		"""
		root = self._root

		def postorder_traverse(root):
			if root.leftChild is None and root.rightChild is None:
				return [root.data]

			if root.leftChild is not None and root.rightChild is None:
				return postorder_traverse(root.leftChild)+[root.data]
			elif root.leftChild is None and root.rightChild is not None:
				return postorder_traverse(root.rightChild)+[root.data]
			else:
				return postorder_traverse(root.leftChild)+postorder_traverse(root.rightChild)+[root.data]

		return postorder_traverse(root)
