# A) Singly Linked List


class SinglyNode:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, data):
		new_node = SinglyNode(data)
		new_node.next = self.head
		self.head = new_node

	def display(self):
		current = self.head
		values = []
		while current:
			values.append(str(current.data))
			current = current.next
		print(" -> ".join(values) + " -> None")


linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.display()


# B) Doubly Linked List


class DoublyNode:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None


class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def insert(self, data):
		new_node = DoublyNode(data)
		new_node.next = self.head
		if self.head:
			self.head.prev = new_node
		self.head = new_node

	def display(self):
		current = self.head
		values = []
		while current:
			values.append(str(current.data))
			current = current.next
		print("None <-> " + " <-> ".join(values) + " <-> None")


doubly_list = DoublyLinkedList()
doubly_list.insert(5)
doubly_list.insert(10)
doubly_list.insert(15)
doubly_list.display()


# C) Circular Linked List


class CircularNode:
	def __init__(self, data):
		self.data = data
		self.next = None


class CircularLinkedList:
	def __init__(self):
		self.head = None

	def insert(self, data):
		new_node = CircularNode(data)
		if self.head is None:
			self.head = new_node
			new_node.next = self.head
			return

		current = self.head
		while current.next != self.head:
			current = current.next
		current.next = new_node
		new_node.next = self.head

	def display(self):
		if self.head is None:
			print("Empty list")
			return

		values = []
		current = self.head
		while True:
			values.append(str(current.data))
			current = current.next
			if current == self.head:
				break
		print(" -> ".join(values) + " -> (back to head)")


circular_list = CircularLinkedList()
circular_list.insert(5)
circular_list.insert(10)
circular_list.insert(15)
circular_list.display()