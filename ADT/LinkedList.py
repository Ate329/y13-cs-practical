class LinkedList:
    def __init__(self):
        self.startPointer = 0
        self.nullPointer = -1
        self.itemPointer = 0
        self.freePointer = 0
        self.tempPointer = 0
        self.found = False

    def generateList(self, length):
        from random import randint
        
        self.list = [None for i in range(0, length)]
        
        self.freePointer = randint(1, length -1)
        self.startPointer = self.freePointer - 1
        
        for i in range(0, self.freePointer):
            self.list[i] = randint(0, 100)
        
        for i in range(self.freePointer, length):
            self.list[i] = None
                
        print(f"Generated list: {self.list}")

        self.generatePointerList()
        
    def generatePointerList(self):
        self.pointerList = [None for i in range(0, len(self.list) + 2)]
        
        self.pointerList[0] = self.nullPointer
        
        for i in range(1, len(self.list) + 1):
            self.pointerList[i] = i - 1

        self.pointerList.remove(None)

        self.pointerList.append(self.nullPointer)
        self.pointerList.remove(self.startPointer)
        self.pointerList.remove(self.freePointer)
        
        print(f"Generated pointer list: {self.pointerList}")
    
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
            
            print(f"{item} inserted at index {self.startPointer}")

    def delete(self, item):
        if self.startPointer == self.nullPointer:
            print("List is empty")
        else:
            self.itemPointer = self.startPointer
            
            while (self.list[self.itemPointer] != item) and (self.itemPointer != self.nullPointer):
                self.itemPointer = self.pointerList[self.itemPointer]
                
            if self.list[self.itemPointer] == item:
                self.pointerList[self.itemPointer] = self.freePointer
                self.freePointer = self.itemPointer
                self.list[self.itemPointer] = None
                print(f"{item} deleted at index {self.itemPointer}")
            else:
                print(f"{item} not found in the list")
                
            if self.freePointer == self.nullPointer:
                print("Free pointer points to null")
                       
    def display(self):
        print(f"Free Pointer: {self.freePointer}")
        print(f"Start Pointer: {self.startPointer}")
        print(f"Linked List: {self.list}")
        print(f"Pointer List: {self.pointerList}")
        

ll = LinkedList()

'''
ll.generateList(10)

ll.find(95)
ll.find(20)
ll.find(100)

ll.insert(99)
ll.find(99)
ll.display()
'''

''' # test delete function
ll.generateList(10)
ll.delete(25)
ll.display()
'''
