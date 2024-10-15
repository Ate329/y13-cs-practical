class Queue:
    def __init__(self):
        self.frontPointer = 0
        self.rearPointer = -1
        self.queueSize = 0
        self.queueCapacity = 10
        self.queue = [None for _ in range(self.queueCapacity)]

    def enQueue(self, item):
        if self.queueSize == self.queueCapacity:
            print("The queue is full, cannot enqueue")
        else:
            self.rearPointer += 1
            if self.rearPointer == self.queueCapacity:
                self.rearPointer = 0
            self.queue[self.rearPointer] = item
            self.queueSize += 1
            print(f"Queue after enqueue: {self.queue}")

    def deQueue(self):
        if self.queueSize == 0:
            print("Queue is empty, cannot dequeue")
            return None
        else:
            item = self.queue[self.frontPointer]
            self.queue[self.frontPointer] = None
            self.frontPointer += 1
            if self.frontPointer == self.queueCapacity:
                self.frontPointer = 0
            self.queueSize -= 1
            print(f"Dequeued item: {item}")
            return item

    def display(self):
        if self.queueSize == 0:
            print("Queue is empty")
        else:
            print("Queue contents:", end=" ")
            index = self.frontPointer
            for _ in range(self.queueSize):
                print(self.queue[index], end=" ")
                index += 1
                if index == self.queueCapacity:
                    index = 0
            print()


def test():
    q = Queue()

    # Test enQueue
    for i in range(1, 12):
        q.enQueue(i)

    q.display()

    # Test deQueue
    for _ in range(5):
        q.deQueue()

    q.display()

    # Test enQueue after deQueue
    for i in range(20, 25):
        q.enQueue(i)

    q.display()

    # Test deQueue until empty
    while q.deQueue() is not None:
        pass

    q.display()

    # Test enQueue after empty
    q.enQueue(100)
    q.display()
