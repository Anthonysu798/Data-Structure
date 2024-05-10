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
    #numbers[0] = 100
    new_numbers = numbers.copy()
    new_numbers[0] = 100

numbers = [1, 2, 3, 4, 5]
print(modify_list(numbers))

print(numbers)

# get the max number from the list
def get_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
    # Alternative way
    # return max(numbers)

# get the min number from the list
def get_min(numbers):
    return min(numbers)

numbers = [2, 1, 5, 3, 4]

print(get_max(numbers))

print(get_min(numbers))

def is_palindrome(str):
    return str == str[::-1] # Reverse the string and compare it with the original string
print(is_palindrome("wow"))

class Vehicle:
    def __init__(self, name, kms):
        # Automatically called the data members name and kms
        self.name = name
        self.kms = kms

    def display(self):
        print(f"Name: {self.name} KMs: {self.kms}")



v1 = Vehicle("Car", 1000)
v1.display()


class Car(Vehicle):
    def __init__(self, name=None, kms=None, color=None):
        super().__init__(name, kms) # Parent class constructor

        # if color is not in the parent constructor you can do this
        self.color = color

    def display(self):
        super().display() # call the display method from the parent class | only print name and KMS
        print("Color:", self.color)


car = Car("Toyota", 1000, "Red")
car.display()

class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers

    def display(self):
        # display array elements
        for number in self.numbers:
            print(number, end=" ")

    def get_max(self):
        # max element of the array
        # maxNumber = self.numbers[0]
        # for number in self.numbers:
        #     if number > maxNumber:
        #         maxNumber = number
        return max(self.numbers)

    def get_min(self):
        # min element of the array
        # minNumber = self.numbers[0]
        # for number in self.numbers:
        #     if number < minNumber:
        #         minNumber = number
        return min(self.numbers)

    def get_sum(self):
        # sum of the array
        return sum(self.numbers)

    def get_avg(self):
        # average of the array
        return sum(self.numbers) / len(self.numbers)

    def search(self, number):
        # search for a number in the array return True or False
        return number in self.numbers

    def even_numbers(self):
        # return all the even numbers from the array
        return [even for even in self.numbers if even % 2 == 0]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = Numbers(nums)
print("Original Array:", numbers.display())
print("\nMax:", numbers.get_max())
print("Min:", numbers.get_min())
print("Sum:", numbers.get_sum())
print("Avg:", numbers.get_avg())
print("Search 5:", numbers.search(5))
print("Search 11:", numbers.search(11))
printf("Search:", "Found" if numbers.search(5) else "Not Found")
print("Even Numbers:", numbers.even_numbers())








