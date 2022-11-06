class Queue:
    def __init__(self):
        self.queue = []

    def enque(self):
        while True:
            x = input("Enter element to enqueue: ")
            if x == "":
                break
            self.queue.append(int(x))
            print("Element enqueued is: ", x)

    def dequeue(self):
        if not self.queue:
            print("Queue is Empty and can't be dequeue further")
        else:
            popped = self.queue.pop(0)
            return print("Popped element is: ", popped)

    def show(self):
        return print(self.queue)

    def front(self):
        if not self.queue:
            return print("No elements in queue")
        else:
            return print("Front Element is: ", self.queue[0])

    def rear(self):
        if not self.queue:
            return print("No elements in queue")
        else:
            return print("Rear Element is: ", self.queue[len(self.queue) - 1])

    def size(self):
        return print("Length of Queue is", len(self.queue))

    def is_empty(self):
        if len(self.queue) == 0:
            return print("Empty Queue")
        else:
            return print("length is: ", len(self.queue))


queue = Queue()
queue.enque()
queue.show()
queue.size()
queue.front()
queue.rear()
queue.dequeue()
queue.dequeue()
queue.show()
queue.is_empty()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.front()
queue.rear()
