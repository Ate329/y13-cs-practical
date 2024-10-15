class Stack:
    def __init__(self):
        self.stackFull = 10
        self.basePointer = 0
        self.topPointer = -1
        self.stack = [None for i in range(self.stackFull)]

    def push(self, item):
        if self.topPointer >= self.stackFull - 1:
            print("Stack is full, cannot push")
        else:
            self.topPointer += 1
            self.stack[self.topPointer] = item
            print(f"stack after push: {self.stack}")

    def pop(self):
        if self.topPointer == self.basePointer - 1:
            print("Stack is empty")
            return None
        else:
            item = self.stack[self.topPointer]
            self.stack[self.topPointer] = None
            self.topPointer -= 1
            print(f"stack after pop: {self.stack}")
            return item

# Test code
if __name__ == "__main__":
    stack = Stack()

    # Test pushing elements
    for i in range(1, 12):
        stack.push(i)

    # Test popping elements
    for _ in range(5):
        popped = stack.pop()
        print(f"Popped item: {popped}")

    # Push more elements
    stack.push(100)
    stack.push(200)

    # Pop until empty
    while stack.topPointer >= stack.basePointer:
        stack.pop()

    # Try to pop from empty stack
    stack.pop()

    # Push to previously full stack
    stack.push(300)
