class IslandClass:
    def __init__(self):
        grid = []
        for i in range(10):
            grid.append(['.' for i in range(30)])
        self.Grid = grid
    def HideTreasure(self):
        pass
    def DigHole(self, Row, Column):
        pass
    def GetSquare(self, Row, Column):
        return self.Grid[Row][Column]
    def DisplayGrid(self):
        for i in range(10):
            for j in range(30):
                print(GetSquare(i, j), end='')
            print()
