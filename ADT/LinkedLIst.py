class LinkedList:
    def __init__(self):
        self.startPointer = 5
        self.nullPointer = -1
        self.itemPointer = 0
        self.freePointer = 6
        self.tempPointer = 0
        self.list = [37, 25, 24, 95, 92, 52, None, None, None, None]
        self.pointerList = [-1, 0, 1, 2, 3, 4, 7, 8, 9, -1]
        self.found = False

    def find(self, item):
        self.itemPointer = self.startPointer
        self.found = False

        while self.itemPointer != self.nullPointer and not self.found:
            if self.list[self.itemPointer] == item:
                self.found = True
            else:
                self.itemPointer = self.pointerList[self.itemPointer]

        if self.found:
            print(f"Item {item} found at index {self.itemPointer}")
        else:
            print(f"Item {item} not found in the list")

    def insert(self, item):
        if self.freePointer == self.nullPointer:
            print("List is full")
        else:
            self.tempPointer = self.startPointer
            self.startPointer = self.freePointer
            self.freePointer = self.pointerList[self.freePointer]

            self.list[self.startPointer] = item
            self.pointerList[self.startPointer] = self.tempPointer

    def display(self):
        print("Linked List:", self.list)
        print("Pointer List:", self.pointerList)
        

'''
ll = LinkedList()
ll.find(95)
ll.find(20)
ll.find(100)

ll.insert(99)
ll.find(99)
ll.display()
'''