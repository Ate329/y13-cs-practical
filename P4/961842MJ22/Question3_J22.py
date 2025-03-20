import typing

# a)
class Card():
    def __init__(self, Number:int, Colour:str):
        self.__Number = Number
        self.__Colour = Colour
    
    def __str__(self):
        return f"Number: {self.__Number}, Colour: {self.__Colour}"

# b)
def GetNumber(card) -> int:
    print(f"The card number is {card.__Number}")
    return card.__Number

def GetColour(card) -> str:
    print(f"The card colour is {card.__Colour}")
    return card.__Colour

# c)
card = Card(1, "oiiai")
cards = [card for i in range(30)]

with open("CardValues.txt", "r") as file:
    for i in range(30):
        number = file.readline()
        colour = file.readline()
        cards[i] = Card(number, colour)
    
    file.close()

for i in cards:
    print(i)


class Card:
    def __init__(self, number: int, colour: str):
        self._number = number   # single underscore for "protected" attribute
        self._colour = colour

    @property
    def number(self) -> int:
        return self._number

    @property
    def colour(self) -> str:
        return self._colour

    def __str__(self):
        return f"Number: {self._number}, Colour: {self._colour}"


def get_number(card: Card) -> int:
    print(f"The card number is {card.number}")
    return card.number

def get_colour(card: Card) -> str:
    print(f"The card colour is {card.colour}")
    return card.colour


# Create a default card and a list of cards
card = Card(1, "oiiai")
cards = [card for _ in range(30)]

# Read card values from file
with open("CardValues.txt", "r") as file:
    for i in range(30):
        number_line = file.readline()
        colour_line = file.readline()
        if not number_line or not colour_line:
            break  # Exit if there are not enough lines
        # Convert number to int and strip newline from colour
        number = int(number_line.strip())
        colour = colour_line.strip()
        cards[i] = Card(number, colour)

for c in cards:
    print(c)
