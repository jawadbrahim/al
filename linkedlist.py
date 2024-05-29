class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data, at_beginning=False):
        new_node = Node(data)
        if at_beginning or not self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def delete(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            return 
        if prev:
            prev.next = current.next
        else:
            self.head = current.next
        current = None
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    def display(self):
        current = self.head
        while current:
            if current.next:
                print(current.data, end=" -> ")
            else:
                print(current.data, end=" ")
            current = current.next
        
#linkedlist = SingleLinkedList()
#linkedlist.append(0, at_beginning=True)
#linkedlist.append(1)
#linkedlist.append(2)
#linkedlist.append(3)
#linkedlist.display()
#print(linkedlist.search(2))
#linkedlist.delete(2)
#linkedlist.display()
#print(linkedlist.search(2))
