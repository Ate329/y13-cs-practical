class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.root = None
        self.num = None

    def add_int(self):
        if self.left == None & self.right == None:
            self.root = self.num
        else:
            if self.left != None & self.num < self.root:
                self.left = self.num
            else:
                self.left.add_int(self.num)

            if self.right != None & self.num > self.root:
                self.right = self.num
            else:
                self.right.add_int(self.num)
    
    def traverse(self):
        if self.left != None:
            print(self.num)
            traverse()
        elif self.right != None:
            print(self.num)
            traverse()
        else:
            break