class IslandClass:
    def __init__(self):
        self.Grid = [['.' for _ in range(30)] for _ in range(10)]

    def HideTreasure(self):
        import random
        TREASURE = "T"
        Row = random.randint(0, 9)  # Fixed range to match grid size
        Column = random.randint(0, 29)  # Fixed range to match grid size
        self.Grid[Row][Column] = TREASURE

    def DigHole(self, Row, Column):
        HOLE = "X"
        if 0 <= Row < 10 and 0 <= Column < 30:  # Added bounds checking
            if self.Grid[Row][Column] == "T":  # Changed TREASURE to "T"
                self.Grid[Row][Column] = HOLE
                return True  # Return whether treasure was found
            else:
                self.Grid[Row][Column] = HOLE
        return False

    def GetSquare(self, Row, Column):
        if 0 <= Row < 10 and 0 <= Column < 30:  # Added bounds checking
            return self.Grid[Row][Column]
        return None  # Return None for invalid coordinates

    def DisplayGrid(self):
        for row in self.Grid:
            print(''.join(row))  # Simplified grid display
