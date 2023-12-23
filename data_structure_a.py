
class DoublyLinked:
	class Node:
		# Initialize a node within a Doubly Linked List, this constructor function will receive 3 parameters, including "data" of that node, 
		# "next" pointer points to the next node, "prev" pointer points to the previous node. 2 of these pointers be set to None as Default
		def __init__(self, data, next = None, prev = None):
			self.data = data
			self.next = next
			self.prev = prev

		# This function does not receive any parameters and return the data stored in node
		def get_data(self):
			return self.data

		# This function does not receive any parameters, it will return the next node
		def get_next(self):
			return self.next

		# This function does not receive any parameters, it will return the previous node
		def get_previous(self):
			return self.prev

	# Initialize a Doubly Link List, this constructor will receive a "data" parameter that set by default as None
	def __init__(self, data = None):
		# If data is not None, that means it will create a new DList with the first node stores the data
		if data is not None:
			new_node = self.Node(data)
			self.tail = new_node
			self.head = new_node
			self.size = 1
		# If data is None, it just create a new DList with no node within it, then set the head and tail pointer to None
		else:
			self.head = None
			self.tail = None
			self.size = 0

	# This function does not receive any parameters, it will return the first node in the list.
	def get_front(self):
		# If the list is empty
		if self.is_empty():
			return None
		else:
			return self.head

	# This function does not receive any parameters, it will return the last node in the list.
	def get_back(self):
		# If the list is empty
		if self.is_empty():
			return None
		else:
			return self.tail

	# This function receive a "data" parameter, it will add data to the front of the DList and return nothing
	def push_front(self, data):
		# Create new node with "data" value
		new_node = self.Node(data)

		#  If the list is empty, it will set the head and tail pointer to the new_node
		if self.is_empty():
			self.head = new_node
			self.tail = new_node
		# If the list has at least 1 node
		else:
			# Set the head's previous pointer to the new node
			self.head.prev = new_node
			# Set the new_node's next pointer to the head node
			new_node.next = self.head
			# Set new_node to the head node
			self.head = new_node
		self.size += 1

	# This function receive a "data" parameter, it will add data to the back of the DList and return nothing		
	def push_back(self,data):
		# Create new node with "data" value
		new_node = self.Node(data)

		#  If the list is empty, it will set the head and tail pointer to the new_node
		if self.is_empty():
			self.head = new_node
			self.tail = new_node
		# If the list has at least 1 node
		else:
			new_node.prev = self.tail
			self.tail.next = new_node
			self.tail = new_node
			self.tail.next = None
		self.size +=1

	# This function does not receive any parameters, it will return the fist data node, and return that node's data
	def pop_front(self):
		# If DList is empty
		if self.is_empty():
			raise IndexError('pop_front() used on empty list')
		# If Dlist is not empty
		else:
			# Get the head node to pop
			pop_node =  self.head
			# If the DList has more than 1 node
			if (self.head.next is not None):
				self.head = self.head.next
				self.head.prev = None
			# If the DList only has 1 node
			else:
				self.head = None
				self.tail = None
			self.size -= 1
			return pop_node.get_data()

	# This function does not receive any parameters, it will return the last data node, and return that node's data
	def pop_back(self):
		# If DList is empty
		if self.is_empty():
			raise IndexError('pop_back() used on empty list')
		# If Dlist is not empty
		else: 
			# Get the last node to pop
			pop_node = self.tail
			# If the DList has more than 1 node
			if (self.tail.prev is not None):
				self.tail = self.tail.prev
				self.tail.next = None	
			# If the DList only has 1 node
			else:
				self.head = None
				self.tail = None
			self.size -= 1
			return pop_node.get_data()

	# This function does not receive any parameters, it will return true if the list is empty, otherwise false
	def is_empty(self):
		return self.size == 0

	# This function receive 2 parameters: data and node. It will insert a new node with data value after the "node" parameter and return nothing
	def insert_after(self, data, node):
		# Create a new node with data
		new_node = self.Node(data)

		# if the given node is None, set the data to head
		if node is None:
			self.push_front(data)

		 # if the given node is tail, insert_after is the same as push_back
		elif node is self.tail:
			self.push_back(data)
		
		# otherwise
		else:
			new_node.next = node.next
			new_node.next.prev = new_node
			node.next = new_node
			new_node.prev = node
			self.size += 1
		
	# This function receive a "data" as parameter, it will return a node where data is found
	def search(self, data):
		# current is the pointer that refers to currently searching node.
        # head will be the first node to search
		current = self.head

		# Loop the elements until there is no node
		while current is not None:
			 # if data is found, return the current node that has the data that you want to find
			if (current.data == data):	
				return current
			 # if the data is not the one that you are looking for, move the pointer to the next node
			current = current.next

		# If data is not found in any node, then return None
		return None

	# This function does not receive any parameters, it will return the size of DList
	def __len__(self):
		return self.size

	# This function does not receive any parameters, it will return True if values in DList form a palindrome, otherwise False
	def is_palindrome(self):
		# Using a support recursice function to check
		return self.is_palindrome_recursive(self.head, self.tail)
	
	def is_palindrome_recursive(self, head, tail):
		# if there is only one node is left to compare or if there is none, return true,
		# since it means it is palindrome
		if head is tail or head.next is tail.prev:
			return True

		# otherwise,
		else:
			# if head and tail have different values, return false
			# since it means they are not palindrome
			if head.data != tail.data:
				return False

			# if they are the same, call another recursive function to compare the next nodes.
			# set the arguments with the next nodes of head nad tail
			# head.next is now the new head of the new recursive function, and tail.prev will be the new tail.
			else:
				return self.is_palindrome_recursive(head.next, tail.prev)