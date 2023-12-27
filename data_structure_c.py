
"""
For HashTable class, I will implement a hash table by using the linear probing approach. I will use the built-in hash() function to hash
a key, then return a value as an index in a list. 
Using linear probing, I can handle the collision more easier by finding the next index where this spot is still available to store the key
The formula to find the next index: (hashed_key_index + 1) % array_capacity
"""
# fmt: off
class HashTable:
    # You cannot change the function prototypes below.  Other than that
    # how you implement the class is your choice as long as it is a hash table

    # This is Constructor function for the HashTable class that will receive a "cap" parameter with a default value is 32.
	# It is used to initialize an empty hash table with capacity
    def __init__(self, cap=32):
        self.cap = cap
        self.table = [None] * self.cap
        self.size = 0


    # This function will receive 2 parameters as key and value. This function will whether or not add this key-value pair to the hash table
	# that depends on some specific cases below. It return True if a new key-value pair would be added to the table, otherwise False
    def insert(self, key, value):

        # Get a index from the key.
        index = hash(key) % self.cap
        
        # Check if the key already exists in the hash table
        if self.search(key) is None:
            # Collisions handling
            while self.table[index] is not None:
                # Apply linear probing formula to find the next index
                index = (index + 1) % self.cap
        else:
            return False
    
        # Add key-value pair to the hash table, and increase it's size
        self.table[index] = (key, value)
        self.size += 1

        # Resize if the tables are filled more than 70% of the capacity
        if self.size / self.cap > 0.7:
            # Create a temporary hash table with a new capacity
            new_table = [None] * (self.cap * 2)

            # Re-calculate to move the cells of current table into the new hash table
            for cell in self.table:

                # Check if the cell is empty
                if cell is not None:
                    # Get a new index for the new hash table using the new size.
                    index = hash(cell[0]) % (self.cap * 2)

                    # Check collision at this new index
                    while new_table[index] is not None:
                        # if Collision happens, moves to the next index.
                        index = (index + 1) % (self.cap * 2)

                    # insert the cell into the new hash table
                    new_table[index] = (cell[0], cell[1])

            # Change the capacity to the new one and copy from the new table     
            self.table = new_table
            self.cap *= 2   

        return True


    # This funtion will receive a key-value pair, it will modifies an existing key-value pair into the table. If no record 
	# with matching key exists in the table, the function does nothing and returns False. Otherwise, function changes 
	# the existing value into the one passed into the function and returns True
    def modify(self, key, value):
        # Get a index from the key.
        index = hash(key) % self.cap

        # This while loop Checks if the key exists in the hash table
        # Start from the cell of the index that we got from the key
        # Stops when there is no cell in the cluster
        while self.table[index] is not None:

            # Check if the key of the cell is the same as the key we need
            if self.table[index][0] == key:

                # Set a new value into the cell
                self.table[index] = (key, value)

                # return True, when the cell is found
                return True
            
            # Move to the next index in case there was a collision
            index = (index + 1) % self.cap
        
        # Return False, if no cell with the key found,
        return False
        

    # This function receive a key as a parameter, removes the key-value pair with the matching key. 
	# If no record with matching key exists in the table, the function does nothing and returns False. 
	# Otherwise, record with matching key is removed and returns True
    def remove(self, key):
        # Get a index from the key.
        index = hash(key) % self.cap


        # This while loop Checks if the key exists in the hash table
        # Start from the cell of the index that we got from the key
        # Stops when there is no cell in the cluster
        while self.table[index] is not None:

            # Compare the key in the index with the key that we are looking for.
            if self.table[index][0] == key:
                # Set the cell to None (delete)
                self.table[index] = None
                # Change the current size
                self.size -= 1
                # Move to the next cell to check if there was a collision.
                index = (index + 1) % self.cap

                # Check collision until there is no a cell within the same cluster
                while self.table[index] is not None:
                    # Temporarily store the key, value pair 
                    current_key = self.table[index][0]
                    current_value = self.table[index][1]

                    # Set the cell to None
                    self.table[index] = None

                    # Set the size again.
                    self.size -= 1

                    # Insert the pair into the hash table again
                    self.insert(current_key, current_value)
                    
                    # Move to the next index
                    index = (index + 1) % self.cap
                
                # return True when the cell of the key is deleted
                return True
            
            # Move to the next index
            index = (index + 1) % self.cap

        # return False when the cell of the key is not found
        return False


    # This function will receive 1 key parameter. It will find the key's value based on the key parameter.
	# This function return its key's value if the key existed in the table. Otherwise return None
    def search(self, key):

        # Get a index from the key
        index = hash(key) % self.cap

        # This While loop Checks if the key exists in the hash table at the index
        # Starts from the cell of the index that we got from the key
        # Stops when there is no cell in the cluster
        while self.table[index] is not None:

            # Check if the key of the cell is the same with our key
            if self.table[index][0] == key:
                
                # If they're the same, return the value of the cell
                return self.table[index][1]
            
            # Move to the next index
            index = (index + 1) % self.cap

        # If not found, return None
        return None


    # This function return the capacity of the hash table
    def capacity(self):
        return self.cap


    # return how many cells(key, value pair) are stored in the hash table
    def __len__(self):
        return self.size
# fmt: on