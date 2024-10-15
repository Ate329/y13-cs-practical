import random

print("We prefer insertion sort")

def generate_list(length):
    myList = []
    
    for _ in range(length):
        number = random.randint(0, 100)
        myList.append(int(number))
    
    return myList

def insertion_sort(list):
    # print(f"original list: {list}")
    counter = 0
    
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
            counter += 1 
        
        list[j + 1] = key
        
    # print(f"sorted list: {list}")
    
    return counter
    
# print(insertion_sort(generate_list(int(input("Array length: ")))))