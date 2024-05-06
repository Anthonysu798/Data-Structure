message = "    Seneca  "

print(len(message))


i = 5.6
j = 6.2

result = i / j 

print(result)

print(f"Result: {result}")

print("Result: {} / {} = {:.2f}".format(i, j, result))

num = 7

if (num % 2 == 0):
    print("Even")
else:
    print("Odd")

marks = 40

if (marks >= 90):
    print("A+")
elif (marks >= 80):
    print("A")
elif (marks >= 70):
    print("B")
elif (marks >= 60):
    print("C")
elif (marks >= 50):
    print("D")
else:
    print("F");


first = "Seneca"
last = "College"

if (first == "Seneca" or last == "College"):
    print("I like it")
else:
    print("I don't like it")

if (first not in "Seneca College Newnham"):
    print("I like it")
else:
    print("I don't like it")

num = 5

if (num !=5):
    print("Not a five")
else: 
    print("Five")


flag = True
if (not flag):
    print("False")
else: 
    print("True")

# Ask the user to enter a number
num = int(input("Enter a number: "))

if (num % 2 == 0):
    print("Even")
else:
    print("Odd")


i = 1

while (i <= 10):
    # print(i, end = " ") print the output in the same line
    print(i)
    i += 1

# Keep asking the user to enter a fruit until they enter "q"
prompt = input("Enter a fruit (q to quit): ")

while (prompt != "q"):
    prompt = input("Enter a fruit (q to quit): ")

# Using break to exit the loop
while (True):
    if (prompt == "q"):
        break
    prompt = input("Enter a fruit (q to quit):")

# 0 to 9  (10 is not included)  0, 1, 2, 3, 4, 5, 6, 7, 8, 9 the end value is not included

#for i in range(0, 100, 10): the third value is increment by 10 0, 10, 20, 30, 40, 50, 60, 70, 80, 90
for i in range(0, 10): 
    print(i)


