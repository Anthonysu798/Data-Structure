def search(numbers, number):
    pass

print(search([1, 2, 3, 4, 5], 3)) 
# worse case scenario: O(n)
# best case scenario: O(1)
# average case scenario: O(n)

def get_number(number):
    return number

# All regular statement 
    # 5 + 6 = 11 O(1) constant time
    # if 5 < 6 (1 ms)
    # return (1 ms)

def sum_of_elements(numbers): # size = n - size of this array is n
    sum = 0 # O(1)

    for i in range(len(numbers)): # ) O(1) + 0(1) * n + 0(1) * n - i, range, and len function so i will be three O(1)
        sum += numbers[i] # O(1) * n
    
    return sum # O(1)

# O(1) + O(1) + O(n) + O(n) + O(n) +  O(1) = O(3n +3)
# Apply first rule Rule: O(3n)
# Rule 2 = O(n)

# Time complexity of this function based on the size of the array = O(n) linear time complexity 


print(sum_of_elements([1, 2, 3, 4, 5]))


def display_pairs(numbers): # size = n
    for i in range(len(numbers)): # O(1) + O(1) * n + O(1) * n 
        for j in range(len(numbers)): # O(1) * n + O(1) * n + O(1) * n
            print(f"({numbers[i]}, {numbers[j]})") # O(1) * n * n | becase this is inside the nested loop


# Time complexity with respect to size of the array: Use five steps analysis
display_pairs([1, 2, 3]) # (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3) - 9 pairs


# Step 1: Define variable - n is the size of the array. T(n) as the time complexity of the function
# Step 2: Find the time complexity of each statement
# Step 3: Create a mathematical equation O(1) + O(n) + O(n) + O(1) + O(n) + O(n) + O(n^2)
# Step 4: Simplify the equation = O(n^2) + O(4n) + O(2) = O(n^2) | keep fastest growing term and remove constants, power is not contant
# Step 5: Final result = T(n) = O(n^2) 

# Nested is O(n^2) - Quadratic time complexity
# 3 nested loops = O(n^3) - Cubic time complexity
# 4 nested loops = O(n^4) - Quartic time complexity

