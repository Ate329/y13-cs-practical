import random

print("I love Linear Search")

def generate_list(length):
    myList = []
    
    for i in range(length):
        number = random.randint(0, 100)
        myList.append(number)
    
    return myList

def linear_search_for(num):
    list = generate_list(int(input("Array length: ")))
    # list = [14,20,16,30,1] # FOR TESTING PURPOSES
    index = 0
    found = False
    
    for i in list:
        if i == num:
            print(f"Number {num} found, in index {index}")
            found = True
            break
        
        index += 1

    if not found:
        print(f"The number {num} is not in the array/list")
        
    print(f"list: {list}")
        
def linear_search_while(num):
    list = generate_list(int(input("Array length: ")))
    # list = [14,20,16,30,1] # FOR TESTING PURPOSES
    index = 0
    found = False
    
    while found == False:
        if list[index] == num:
            print(f"Number {num} found, in index {index}")
            found = True
        
        index += 1 

    if not found:
        print(f"The number {num} is not in the array/list")
    
    print(f"list: {list}")
    
def linear_search_question(ValueToFind, length):
    MyList = generate_list(int(length))
    Found = False
    Index = 0
    MaxIndex = len(MyList)
    
    print(f"list: {MyList}")
    
    while Found == False or Index < MaxIndex: 
        if MyList[Index] == ValueToFind:
            Found = True
            print(f"Value found in position {Index}")
            break
        
        Index += 1
            
    if not Found:
        print("Value not found in the list")

# linear_search_question(69, 200)