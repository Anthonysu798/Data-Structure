# Description: Bubble sort algorithm implementation in Python
def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap
                tmp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = tmp
    return numbers
    # Time complexity of this function based on the size of the array = O(n^2) - Quadratic time complexity

print(bubble_sort([2, 1, 8, 5, 4, 3]))


# Selection sort algorithm implementation in Python
# Smallest element alway at index 0
def selection_sort(numbers):
    for i in range(len(numbers)):
        smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[smallest]:
                smallest = j

        if i != smallest:
            # Swap
            numbers[i], numbers[smallest] = numbers[smallest], numbers[i]

    return numbers


print(selection_sort([2, 1, 8, 5, 4, 3]))

# Merge Sort
def merge_sort(numbers):
    size = len(numbers)

    if size < 2:
        return 
    
    mid = size // 2 # // Give integer division instead of float divisionf
    left = numbers[:mid] 
    right = numbers[mid:]

    # Split the array into two halves
    merge_sort(left)
    merge_sort(right)

    # Time complexity = O(nlogn) - Logarithmic time complexity

    merge(numbers, left, right)

def merge(numbers, left, right):
    size = len(numbers)
    left_size = len(left)
    right_size = len(right)

    i = j = k = 0

    while (i < left_size and j < right_size):
        if (left[i] <= right[j]):
            numbers[k] = left[i]
            i+=1
        else:
            numbers[k] = right[j]
            j+=1

        k+=1
    
    # Copy the remaining elements of left array if any 
    while (i < left_size):
        numbers[k] = left[i]
        k+=1
        i+=1

    while(j < right_size):
        numbers[k] = right[j]
        k+=1
        j+=1

numbers = [2, 1, 8, 5, 4, 3]
merge_sort(numbers)
print(numbers)

# Quick Sort
# Select a pivot - last element

def swap(numbers, i, j):
    tmp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = tmp

def partition(numbers, start, end):
    pivot = numbers[end]
    i = start - 1

    for j in range(start, end):
        if numbers[j] < pivot: # If first element is less than pivot increment i by one
            i+=1
            swap(numbers, i, j)
    i+=1 # Putting pivot in the correct position
    swap(numbers, i, end)

    return i

def quick_sort(numbers, start, end):
    if (start < end):
        pivotIndex = partition(numbers, start, end)
        quick_sort(numbers, start, pivotIndex - 1) # Left side of the pivot
        quick_sort(numbers, pivotIndex + 1, end) # Right side of the pivot

numbers = [2, 1, 8, 5, 4, 3]

quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)