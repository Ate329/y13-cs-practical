import random

print("We prefer binary search")

def generate_list(length):
    myList = []
    
    for i in range(length):
        number = random.randint(0, 100)
        myList.append(int(number))
    
    return myList

def binary_search(num):
    list = generate_list(int(input("Array length: ")))
    # list = [14,20,16,30,1,6]
    # list = ["oiiai", "skibidi", "gyat", "goofy", "ohio"]
    list.sort()
    print(f"List: {list}")
    
    lb  = 0
    ub = len(list)
    found = False
    
    while (not found) and (lb <= ub):
        index = (lb + ub)//2
    
        if list[index] == num:
            position = index
            print(f"Number found {num} in index {position}")
            found = True
            break
        elif num > list[index]:
            lb = index + 1
        elif num < list[index]:
            ub = index - 1
    
    if found == False:
        print(f"Number {num} not found in the list {list}")

binary_search(28)