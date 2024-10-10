#Task 1:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

#Task 2:
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def delete_node(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                temp = None
                return
            temp = temp.next

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.head
        if not current:
            return
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

# Task 3:
if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    # Test insertion
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_beginning(0)
    
    # Test forward traversal
    print("Doubly Linked List after insertions (forward):")
    dll.traverse_forward()
    
    # Test backward traversal
    print("Doubly Linked List after insertions (backward):")
    dll.traverse_backward()
    
    # Test deletion
    dll.delete_node(2)
    print("Doubly Linked List after deleting 2 (forward):")
    dll.traverse_forward()
    
    dll.delete_node(0)
    print("Doubly Linked List after deleting 0 (forward):")
    dll.traverse_forward()
