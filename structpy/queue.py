"""
This is the implementation of Queue data structure.
"""

class queue:

	def __init__(self):
		"""
		Initialize this class with an empty list.
		"""
		self._queue = []

	def enque(self, data):
		"""
		This method adds the data at the end of the queue.
		"""
		self._queue.append(data)

	def  deque(self):
		"""
		This method removes and returns the first element from the list.
		"""
		if self._queue != []:
			return self._queue.pop(0)
		return

	def getfront(self):
		"""
		Returns the element at the front of the queue.
		"""
		if self._queue!=[]:
			return self._queue[0]
		return

	def getlast(self):
		"""
		Returns the last element of the queue.
		"""
		if self._queue != []:
			return self._queue[-1]
		return

	def __len__(self):
		"""
		Returns the number of elements in the queue.
		"""
		return len(self._queue)

	def __str__(self):
		"""
		Return the string representation of the queue.
		"""
		return str(self._queue)
