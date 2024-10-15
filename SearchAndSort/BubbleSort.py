import random

print("We love bubble sort")

def generate_list(length):
    myList = []
    
    for i in range(length):
        number = random.randint(0, 100)
        myList.append(int(number))
    
    return myList

def bubble_sort(list):
    swap = True
    top = len(list)
    interation_counter = 0
    swap_counter = 0
    
    while swap or (top > 0):
        swap = False
        for index in range(top - 1):
            if list[index] > list[index + 1]:
                list[index + 1], list[index] = list[index], list[index + 1]
                swap = True
            
            if swap == True:
                swap_counter += 1
                
            interation_counter += 1
            
        top -= 1

    return interation_counter, swap_counter

# print(bubble_sort(generate_list(int(input("Array length: ")))))
