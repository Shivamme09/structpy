"""
This is the implementation of Stack data strucuture.
"""

class stack:

	def __init__(self):
		"""
		Initialize the class with an empty list.
		"""
		self._stack = []

	def push(self, data):
		"""
		Push the data on top of the stack.
		"""
		self._stack.append(data)

	def pop(self):
		"""
		Remove and return the element at the top of the stack.
		"""
		if self._stack != []:
			return self._stack.pop()

	def gettop(self):
		"""
		Return the element at the top of the stack.
		"""
		if self._stack != []:
			return self._stack[-1]

	def __len__(self):
		"""
		Return the number of elements in the stack.
		"""
		return len(self._stack)

	def __str__(self):
		"""
		Return a string representation of the stack.
		"""
		return str(self._stack)
