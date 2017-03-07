"""
This is the implementation of Linked List data strucutre.
linkedlist = singly linked list
dlinkedlist = doubly linked list
"""

class Node:
	"""
	This is the node class.
	This class will later be implemented to make a node of the list.
	"""

	def __init__(self, data):
		"""
		This initializes the class with three attributes Data,
		NextPointer and PrevPointer.
		"""
		self.data = data
		self.next_ptr = None
		self.prev_ptr = None


class linkedlist:
	"""
	This is the linked list class which implents the main class
	for singly linked list.
	"""

	def __init__(self):
		"""
		Initialize the class with a head pointer.
		"""
		self._head = None


	def insert(self, data):
		"""
		This method adds an element to the list.
		First the data is initiazed as the Node in the linked list.
		"""

		self._node = Node(data)

		if self._head == None:
			self._head = self._node
		else:
			self._node.next_ptr = self._head
			self._head = self._node


	def delete(self, data):
		"""
		This method will delete the data from the list.
		"""
		self._item = data
		cuurent_node = self._head

		if cuurent_node is None:
			return

		if cuurent_node.data == self._item:
			self._head = cuurent_node.next_ptr

		while cuurent_node.next_ptr is not None:
			if cuurent_node.next_ptr.data == self._item:
				cuurent_node.next_ptr = cuurent_node.next_ptr.next_ptr
				break
			cuurent_node = cuurent_node.next_ptr


	def search(self, data):
		"""
		This method rerturns True if the data is present in the list.
		"""

		cuurent_node = self._head
		while cuurent_node is not None:
			if cuurent_node.data == data:
				return True
			cuurent_node = cuurent_node.next_ptr
		return False

	def gethead(self):
		"""
		This method returns the head of the linked list.
		"""
		if self._head is not None:
			return self._head.data
		return self._head


	def __len__(self):
		"""
		This function returns the number of nodes in the linked list.
		"""
		number = 0
		cuurent_node = self._head
		while cuurent_node is not None:
			number+=1
			cuurent_node = cuurent_node.next_ptr
		return number


	def __str__(self):
		"""
		This method prints the elements of the linked list in
		human readable form.
		The head is the first element.
		"""
		_list = []
		cuurent_node = self._head
		while cuurent_node is not None:
			_list.append(cuurent_node.data)
			cuurent_node = cuurent_node.next_ptr
		return(str(_list)[1:-1])



class dlinkedlist(linkedlist):
	"""
	This class implements the doubly linked list.
	All the methods of above class is inherited in this class.
	"""

	def insert(self, data):
		"""
		Overriding the insert method from LinkedList.
		"""

		self._node = Node(data)
		if self._head == None:
			self._head = self._node
		else:
			self._node.next_ptr = self._head
			self._head.prev_ptr = self._node
			self._head = self._node


	def delete(self, data):
		"""
		Overriding the method from LinkedList.
		"""

		self._item = data
		cuurent_node = self._head

		if cuurent_node is None:
			return

		if cuurent_node.data == self._item:
			self._head = cuurent_node.next_ptr
			if self._head is not None:
				self._head.prev_ptr = None
			return

		while cuurent_node.next_ptr is not None:
			if cuurent_node.next_ptr.data == self._item:
				cuurent_node.next_ptr = cuurent_node.next_ptr.next_ptr
				if cuurent_node.next_ptr is not None:
					cuurent_node.next_ptr.prev_ptr = cuurent_node
				return
			cuurent_node = cuurent_node.next_ptr
