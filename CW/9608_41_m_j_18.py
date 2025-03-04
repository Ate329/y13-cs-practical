# Q5B
class GameElement:
    def __init__(self, PositionX: int, PositionY: int,
                 Width: int, Height: int, ImageFilename: str):
        self.PositionX = PositionX
        self.PositionY = PositionY
        self.Width = Width
        self.Height = Height
        self.ImageFilename = ImageFilename

    def GetDetails(self):
        return f"Position: {self.PositionX}, {self.PositionY}, Size: {self.Width}x{self.Height}, Image: {self.ImageFilename}"

# Q5C
class Scenery(GameElement):
    def __init__(self, PositionX: int, PositionY: int,
                 Width: int, Height: int, ImageFilename: str,
                 CauseDamage: bool, DamagePoints: int):
        super().__init__(PositionX, PositionY, Width, Height, ImageFilename)
        self.CauseDamage = CauseDamage
        self.DamagePoints = DamagePoints if CauseDamage else 0
    
    def GiveDamagePoints(self):
        return self.DamagePoints if self.CauseDamage else 0
    
    # Q5Dii
    def GetScenery(self):
        return f"Scenery: CauseDamage: {self.CauseDamage}, DamagePoints: {self.DamagePoints}, Details: {self.GetDetails()}"

# Q5Di some funny stuff here
class GiftBox(Scenery):
    def __init__(self, PositionX: int = 150, PositionY: int = 150,
                 Width: int = 50, Height: int = 75,
                 ImageFilename: str = "box.png",
                 CauseDamage: bool = True, DamagePoints: int = 50):
        super().__init__(PositionX, PositionY, Width, Height, ImageFilename,
                        CauseDamage, DamagePoints)
        

# test cases
# Q5C
scenery = Scenery(100, 100, 100, 100, "scenery.png", True, 10)
print(scenery.GetScenery())

# Q5Di
giftbox = GiftBox()
print(giftbox.GetScenery())