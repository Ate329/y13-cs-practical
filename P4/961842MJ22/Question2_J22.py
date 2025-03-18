# bii)
def print_2d_array(array):
    for row in array:
        print(row)
    print("**********************************")

# a)
import random

list1 = [[random.randint(1,100) for _ in range(10)] for _ in range(10)]
list1[0][5] = 69
print_2d_array(list1)

# bi)
ArrayLength = 10

for i in range(0, ArrayLength):
    for j in range(0, ArrayLength - 1):
        for z in range(0, ArrayLength - j - 1):
            if list1[i][z] > list1[i][z + 1]:
                list1[i][z], list1[i][z + 1] = list1[i][z + 1], list1[i][z]

print_2d_array(list1)

# ci)
def binary_search(SearchArray, Lower, Upper, SearchValue) -> int:
    if Lower <= Upper:
        Mid = (Lower + Upper) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return binary_search(SearchArray, Lower, Mid - 1, SearchValue)
        else:
            return binary_search(SearchArray, Mid + 1, Upper, SearchValue)
    return -1

print(binary_search(list1, 0, len(list1[0]) - 1, 69))
print(binary_search(list1, 0, len(list1[0]) - 1, 101))
