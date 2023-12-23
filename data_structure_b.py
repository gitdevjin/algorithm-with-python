
"""
- For Stack Class, I will do Stack implementation by using Python list based. I do not use any builtin functions for the list such as: pop(),
append(), extend().
- Stack class implements a First In Last Out data structure.
- In Stack class, I will implement all these functions: Stack Constructor __init__(), check stack's capacity capacity(), push item to stack push(),
pop item from stack pop(), get the most top item get_top(), and count item in stack __len__()
- For the class in Python, in each function, we need to give it a "self" arguement, which is treated as "this" pointer
"""
class Stack:
	# This is Constructor function for the Stack class that will receive a "cap" parameter with a default value is 10.
	# It is used to initilize a Stack with capacity, size
	def __init__(self, cap = 10):
		self.capa = cap

		# I initilize the stack'items to all None with the size is its capacity
		self.stack = [None] * cap
		self.size = 0

	# This function will return the Stack's capacity by accessing the "capa" data member
	def capacity(self):
		return self.capa

	# This function add data to the top of the Stack, that will receive a "data" as parameter
	def push(self, data):	
		# When the Stack is full, I double its size to have more space to add data
		if self.size >= self.capa:
			self.capa *= 2
			# Create an temporary array with new capacity
			new_stack = [None] * self.capa

			# Copy items from old array to temporary array
			for i in range(self.size):
				new_stack[i] = self.stack[i]
			
			# Assign all items in the temporary array with new capacity to the old array
			self.stack = new_stack

		# When Stack is not full
		# Adding new data to the Stack
		self.stack[self.size] = data
		self.size += 1
		
	# This function does not receive any parameter, it will remove the newest value from the stack and return that value
	# Because in Stack implementation, if we push item to the back of the array based list, then we have to pop the item from the back first
	def pop(self):
		# Check if stack is empty, then raising error
		if self.size == 0:
			raise IndexError('pop() used on empty stack')
		# If the stack is not empty
		else: 
			# Get the pop_item by accessing to the end value in array
			pop_item = self.stack[self.size - 1]
			# Set the value at the pop_item to the None
			self.stack[self.size - 1] = None
			self.size -= 1
			return pop_item

	# This function does not receive any parameter, it will return the newest value from the Stack 
	def get_top(self):
		# If the stack is empty then return None
		if (self.is_empty()):
			return None
		return self.stack[self.size - 1]

	# This function does not receive any parameter, it will check if stack is empty then return True, otherwise returning False
	def is_empty(self):
		if self.size == 0:
			return True
		return False

	# This function does not receive any parameter, it will return the number of meaningful valued items in the Stack
	def __len__(self):
		return self.size


"""
- For Queue Class, I will do Queue implementation by using Python list based. I do not use any builtin functions for the list such as: pop(),
append(), extend().
- Queue class implements a First In First Out data structure.
- In Queue class, I will implement all these functions: Queue Constructor __init__(), check queue's capacity capacity(), push item to the
end of queue enqueue(), remove item from the front of the queue dequeue(), get the front item get_front(), and count item in queue __len__()
- I will implement the Queue class by applying the Circular array, its purpose is to make use of the memery or spaces in a Queue
- For the class in Python, in each function, we need to give it a "self" arguement, which is treated as "this" pointer
"""

class Queue:
	# This is Constructor function for the Queue class that will receive a "cap" parameter with a default value is 10.
	# It is used to initilize a Queue with its data memebers: capacity, size, front, back
	def __init__(self, cap = 10):
		self.capa = cap
		self.queue = [None] * cap

		# Initially, the front and back pointer all start from index 0
		self.front = 0
		self.back = 0
		self.size = 0

	# This function does not receive any parameter, it will return the Queue's capacity by accessing the "capa" data member
	def capacity(self):
		return self.capa

	# This function receive "data" parameter, it will add data to the back of the Queue, and return nothing
	def enqueue(self, data):
		# Check if the queue is full
		if self.size >= self.capa:
			# Then make a temporary array with the capacity doubled
			temp = [None] * (self.capa * 2)
			
			# If the front index is less than back index, this only happen when we do enqueue() only until the queue is full, that increases 
			# the back pointer, but keep the front pointer 
			if (self.front < self.back):
				for i in range(0, self.size):
					temp[i] = self.queue[i]
			else:
				# Set j = 0 for the first index position in the temporary arary
				j = 0
				# When front > back pointer, imagine it split queue into 2 parts, one part from front pointer to the last index
				for i in range(self.front, self.size):
					temp[j] = self.queue[i]
					# Incresing j by 1
					j += 1
				# The second part will from the index 0 to the back pointer (included)
				for i in range(0, self.back + 1):
					temp[j] = self.queue[i]
					j += 1
			# Assign the temporary array back to old array
			self.queue = temp
			# Reset the front and back pointer to starting and ending index
			self.front = 0
			self.back = self.size
			# Double the size of queue
			self.capa *= 2
			
		# If the queue is not full
		self.queue[self.back] = data
		self.back += 1
		self.size += 1
		# If back pointer is greater or equal than/to the queue's capacity, applying the circular buffer array to set the back pointer
		if self.back >= self.capa:
			self.back = self.back % self.capa

	# This function does not receive any parameters, it will remove the oldest value (front) value in the queue and return that value
	def dequeue(self):
		# If the queue is not empty
		if not self.is_empty():
			# get the value at the front pointer
			pop = self.queue[self.front]
			# Set it to None
			self.queue[self.front] = None
			# Then increase the front pointer by 1 index
			self.front += 1
			# Decrease the size by 1 unit
			self.size -= 1
			# If dequeue() (remove) all items then it increases the front pointer until it's = the size of the queue, then applying circular buffer
			# reset the front pointer to the index 0
			if self.front >= self.capa:
				self.front = self.front % self.capa
			return pop
		# If the queue is empty, raising error
		else:
			raise IndexError("dequeue() used on empty queue")
	
	# This function does not receive any parameters, it will return the oldest value (front) value from the queue
	def get_front(self):
		# If the queue is empty
		if self.is_empty():
			return None
		# If queue is not empty
		else:
			return self.queue[self.front]

	# This function does not receive any parameter, it will check if queue is empty then return True, otherwise returning False
	def is_empty(self):
		if self.size == 0:
			return True
		return False

	# This function does not receive any parameter, it will return the number of meaningful valued items in the Stack
	def __len__(self):
		return self.size

"""
- For Dequeue Class, I will do Dequeue implementation by using Python list based. I do not use any builtin functions for the list such as: pop(),
append(), extend().
- Dequeue class will allow to add or remove items from front or back of the data structure
- In Dequeue class, I will implement all these functions: Dequeue Constructor __init__(), check dequeue's capacity capacity(), push item to the
front of dequeue push_front(), remove item from the front of the dequeue pop_front(), push item to the back of dequeue push_back(), remove item 
from the back of the dequeue pop_back(), get the front item get_front(), get the back item get_back(), and count item in dequeue __len__()
- I will implement the Dequeue class by applying the Circular array, its purpose is to make use of the memery or spaces in a Dequeue
- For the class in Python, in each function, we need to give it a "self" arguement, which is treated as "this" pointer

"""

class Deque:
	# This is Constructor function for the Dequeue class that will receive a "cap" parameter with a default value is 10.
	# It is used to initilize a Dequeue with its data memebers: capa, size, front, back
	def __init__(self, cap = 10):
		self.capa = cap
		self.front = 0
		self.back = 0
		self.size = 0
		self.deque = [None] * cap

	# This function does not receive any parameter, it will return the Dequeue's capacity by accessing the "capa" data member
	def capacity(self):
		return self.capa

	# This function receive "data" as parameter, it will add data to the front of the Dequeue and return nothing
	def push_front(self, data):
		# If the Dequeue is full
		if self.size >= self.capa:
			# Double the size 
			self.capa *= 2
			# Create a temporary array with new capacity
			temp = [None] * (self.capa * 2)
			
			# Set the j to the position that is behind the last index of the old dequeue
			j = self.size

			# If the front pointer is less than back pointer, it only happens when we only push items to the back until the dequeue is full,
			# that increases the back pointer while still keeping the front pointer at the first index.
			if (self.front < self.back):
				for i in range(0, self.size):
					# Copy value from the old array, this case the front pointer is at index 0, and back pointer is at the last index.
					# I copy values to the j index in the temporary array
					temp[j] = self.deque[i]
					j += 1
			# If front pointer < back pointer, it splits the dequeue into 2 parts
			else:
				# Part 1: from the front index to the last index in the dequeue
				for i in range(self.front, self.size):
					temp[j] = self.deque[i]
					j += 1
				# Part 2: from the 0 index to the back pointer's index
				for i in range(0, self.back + 1):
					temp[j] = self.deque[i]
					j += 1

			# Assign the temporary array back to old array
			self.deque = temp
			# Set the new front pointer to the index to the last index in the old dequeue
			self.front = self.size - 1
			self.deque[self.front] = data
			# Set the back pointer to the end index of the dequeue with new capacity
			self.back = (self.capa - 1) % self.capa
			self.size += 1
		# If the queue is not full
		else:
			# Set the front pointer using the circular buffer
			# When the dequeue is empty and I push front item, the front index will go the the last index value, and it decreases the pointer value
			# when I do push front
			self.front = (self.front - 1) % self.capa
			self.deque[self.front] = data
			self.size += 1

			# If the size  = 1, I just set the front and back pointer at the same index
			if (self.size == 1):
				self.back = self.front
				
	# This function receive "data" parameter, it will add data to the back of the dequeue and return nothing
	def push_back(self, data):
		# If the dequeue is full
		if self.size >= self.capa:
			# Double the size
			self.capa *= 2
			# Create a temporary array with a new capacity
			temp = [None] * (self.capa * 2)

			# Set j = 0, it's the first index in the temp array
			j = 0

			# If the front pointer is less than back pointer, it only happens when we only push items to the back until the dequeue is full,
			# that increases the back pointer while still keeping the front pointer at the first index.
			if (self.front < self.back): 
				for i in range(0, self.size):
					temp[i] = self.deque[i]
			# If front pointer < back pointer, it splits the dequeue into 2 parts
			else:
				# Part 1: from the front index to the last index in the dequeue
				for i in range(self.front, self.size):
					temp[j] = self.deque[i]
					j += 1
				# Part 2: from the 0 index to the back pointer's index
				for i in range(0, self.back + 1):
					temp[j] = self.deque[i]
					j += 1
			# Assign the temporary array back to old array	
			self.deque = temp

			# Set the front poitner to index 0 (starting point)
			self.front = 0
			# Set the back pointer to the position that is behind the last index of the old dequeue
			self.back = (self.size) % self.capa	
			self.deque[self.back] = data
			self.size += 1

		# if the dequeue is not full
		else:	
			# if the dequeue is empty
			if (self.size == 0):	
				# Set (Reset) the front and back pointer to index 0
				self.back = 0	
				self.front = 0			
			# if the dequeue is not empty
			if (self.size >= 1):
				# Increase the back pointer by applying the circular buffer
				self.back = (self.back + 1) % self.capa	
			
			# Set the data to the new back position and increase the dequeue's size
			self.deque[self.back] = data	
			self.size += 1		

	# This function does not receive any parameters, it will remove value from the front of the dequeue and return that value
	def pop_front(self):
		# If the dequeue is empty
		if self.is_empty():
			raise IndexError('pop_front() used on empty deque')
		else: 
			# Get the value at the front poitner
			front_item = self.deque[self.front]
			# Set that value to None
			self.deque[self.front] = None
			# Increase the front pointer by applying the circular buffer
			self.front = (self.front + 1) % self.capa
			self.size -= 1
			return front_item

	# This function does not receive any parameters, it will remove the value from the back pointer, and return that value
	def pop_back(self):
		# If the dequeue is empty
		if self.is_empty():
			raise IndexError('pop_back() used on empty deque')
		else: 
			# Get the value at the back pointer
			pop_item = self.deque[self.back]
			# Set that value to None
			self.deque[self.back] = None
			# Decrease the front pointer by applying the circular buffer
			self.back = (self.back - 1) % self.capa
			self.size -= 1
			return pop_item

	# This function does not receive any parameter, it will return the value at the front pointer
	def get_front(self):
		# If the dequeue is empty
		if self.is_empty():
			return None
		# If the queue is not empty
		return self.deque[self.front]

	# This function does not receive any parameter, it will return the value at the back pointer
	def get_back(self):
		# If the dequeue is empty
		if self.is_empty():
			return None
		# If the queue is not empty
		return self.deque[self.back]

	# This function does not receive any parameter, it will check if queue is empty then return True, otherwise returning False
	def is_empty(self):
		if self.size == 0:
			return True
		return False

	# This function does not receive any parameter, it will return the number of meaningful valued items in the Stack
	def __len__(self):
		return self.size

	# This function receive "k" paramter, it will return the k'th value from the front of the Dequeue 
	def __getitem__(self, k):
		# If k is greater or equal than/to the Dequeue's capacity, raising error
		if k >= self.capa:
			raise IndexError('Index out of range')
		# If k is less than the Dequeue's capacity
		else:
			# Finding the index of k
			index = (self.front + k) % self.capa
			return self.deque[index]