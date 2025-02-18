class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

    def add_int(self, num):
        if self.value is None:
            self.value = num
        else:
            if num < self.value:
                if self.left is None:
                    self.left = Tree()
                self.left.add_int(num)
            else:
                if self.right is None:
                    self.right = Tree()
                self.right.add_int(num)

    def traverse(self):
        if self.left is not None:
            self.left.traverse()
        print(self.value)
        if self.right is not None:
            self.right.traverse()

tree = Tree()
tree.add_int(27)
tree.add_int(19)
tree.add_int(36)
tree.add_int(42)
tree.add_int(16)
tree.traverse()
