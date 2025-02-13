class IslandClass:
    def __init__(self):
        grid = []
        for i in range(10):
            grid.append(['.' for i in range(30)])
        self.Grid = grid

    def HideTreasure(self):
        import random
        TREASURE = "T"
        Row = random.randint(0, 11)
        Column = random.randint(0, 31)
        self.Grid[Row][Column] = TREASURE

    def DigHole(self, Row, Column):
        HOLE = "X"
        FOUND_HOLE = False
        if self.Grid[Row][Column] == TREASURE:
            self.Grid[Row][Column] = HOLE
            FOUND_HOLE = True
        else:
            self.Grid[Row][Column] = HOLE

    def GetSquare(self, Row, Column):
        return self.Grid[Row][Column]

    def DisplayGrid(self):
        for i in range(10):
            for j in range(30):
                print(GetSquare(i, j), end='')
            print()
