# Python program to detect cycle in a linked list 

# Node class 
class Node: 

	# Constructor to initialize the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 

	# Function to initialize head 
	def __init__(self): 
		self.head = None

	# Function to insert a new node at the beginning 
	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	# Utility function to print it the linked LinkedList 
	def printList(self): 
		temp = self.head 
		while(temp): 
			print (temp.data, end =" ") 
			temp = temp.next


	def detectLoop(self): 
		s = set() 
		temp = self.head 
		while (temp): 
		 
			if (temp in s): 
				return True

			s.add(temp) 
	
			temp = temp.next
		
	
		return False

# Driver program for testing 
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(10) 

# Create a loop for testing 
llist.head.next.next.next.next = llist.head; 

if( llist.detectLoop()): 
	print ("1") 
else : 
	print ("0") 

#1 denotes that cycle exists
#0 denotes that cycle does not exist
