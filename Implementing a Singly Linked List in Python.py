#Task 1:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Task 2:
class SinglyLinkedList:
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

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Task 3:
if __name__ == "__main__":
    sll = SinglyLinkedList()
    
    # Test insertion
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_end(3)
    sll.insert_at_beginning(0)
    
    # Test traversal
    print("Linked List after insertions:")
    sll.traverse()
    
    # Test deletion
    sll.delete_node(2)
    print("Linked List after deleting 2:")
    sll.traverse()
    
    sll.delete_node(0)
    print("Linked List after deleting 0:")
    sll.traverse()
 