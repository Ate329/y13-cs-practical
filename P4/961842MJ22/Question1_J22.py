# a)
StackData = [None for _ in range(10)]
StackPointer = 0

# b)
def output():
    print("List: ")
    for i in range(0, 10):
        print(StackData[i], end=" ")
    
    print("\nThe stack pointer is:", StackPointer)
    return

# c)
def Push(num : int) -> bool:
    global StackPointer
    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = num
        StackPointer += 1
        return True

# di)
def test_push():
    global StackPointer
    for i in range(0, 11):
        num = input("Enter number: ")
        flag = Push(num)
        if flag == True:
            print(f"The number {num} is added to the arrary in index {StackPointer - 1}")
        else:
            print("The stack is full")

    output()

# dii)
test_push()

# ei)
def Pop():
    global StackPointer
    if StackPointer <= 0:
        return -1
    else:
        StackPointer -= 1
        current_item = StackData[StackPointer]
        StackData[StackPointer] = None
        return current_item  

# eii)
def test_pop():
    for i in range(0, 2):
        Pop()
    
    print("Array: ", end="")
    for i in range(0, 10):
        print(StackData[i], end=" ")
    print("")

test_pop()
