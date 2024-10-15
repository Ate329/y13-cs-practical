from BubbleSort import bubble_sort
from InsertionSort import insertion_sort

def generate_list(length):
    import random
    
    myList = []
    
    for _ in range(length):
        number = random.randint(0, 1000)
        myList.append(int(number))
    
    return myList

def benchmark(times, length):
    total_insertion_counter = 0
    total_bubble_counter = 0
    total_bubble_swap_counter = 0
    
    for _ in range(times):
        insertion_counter = insertion_sort(generate_list(length))
        bubble_counter, bubble_swap_counter = bubble_sort(generate_list(length))

        total_insertion_counter += insertion_counter
        total_bubble_counter += bubble_counter
        total_bubble_swap_counter += bubble_swap_counter
    
    avg_insertion_counter = total_insertion_counter / times
    avg_bubble_counter = total_bubble_counter / times
    avg_bubble_swap_counte = total_bubble_swap_counter / times 
    
    print(f"total times of iteration for bubble sort: {total_bubble_counter}, the average in {times} sorts: {avg_bubble_counter}")
    print(f"total times of swaps for bubble sort: {total_bubble_swap_counter}, the average in {times} sorts: {avg_bubble_swap_counte}")
    print(f"total times of iteration for insertion sort: {total_insertion_counter}, the average in {times} sorts: {avg_insertion_counter}")

# benchmark(100,100)