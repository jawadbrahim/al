class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
    def peek(self):
        if not self.is_empty():
            return self.items[0]
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
queue = Queue()

queue.enqueue(10)
print("Enqueue item 10, Queue:", queue.items)
queue.enqueue(20)
print("Enqueue item 20, Queue:", queue.items)
queue.enqueue(30)
print("Enqueue item 30, Queue:", queue.items)
while not queue.is_empty():
    dequeued_item = queue.dequeue()
    print("Dequeued item:", dequeued_item)
    print("Queue after dequeue:", queue.items)