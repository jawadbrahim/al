class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        self.display()

    def pop(self):
        if not self.is_empty():
            item = self.items.pop()
            self.display()
            return item

    def display(self):
        print("Current stack:", self.items)
    

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
while not stack.is_empty():
    item = stack.pop()
    print("Popped:", item)
