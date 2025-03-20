# a)
global Animals
Animals = ["oiiai" for _ in range(10)]

# b)
Animals = ["horse", "lion", "rabbit", "mouse", "bird", "deer", "whale", "elephant", "kangaroo", "tiger"]

# c)
def SortDescending() -> None:
    global Animals
    ArrayLength = len(Animals)
    for i in range(0, ArrayLength):
        for j in range(0, ArrayLength - i - 1):
            if Animals[j][0] < Animals[i][0]:
                temp = Animals[j + 1]
                Animals[j + 1] = Animals[j]
                Animals[j] = temp

# di)
SortDescending()
print(Animals)

# dii)


# 2e)

def EnterRecord():
    ID = input("Enter ID")
    QuantityP = input("Enter quantoty")
    Record = SaleData(ID, QuantityP)
    if Enqueue(Record) == -1:
        print("Full")
    else:
        print("Stored")
