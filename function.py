def display():
    return 4+5

print(display())


def evenOdd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def evenOdd(number):
    return number % 2 == 0 # Return True or False

print(evenOdd(5))

print(evenOdd(6))

def display_student(name, city="Toronto"): # Set Default value
    return {'name': name, 'city': city} # Return a dictionary

print(display_student("Anthony", "Markham"))

def modify_list(numbers):
    # return numbers
    numbers[0] = 100

numbers = [1, 2, 3, 4, 5]
print(modify_list(numbers))

print(numbers)










