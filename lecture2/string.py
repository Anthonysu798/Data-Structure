from collections import Counter


def toUpperString(message):
    count = 0
    # If two uppercase in the string return the string in full caps if not just return default string
    for ch in message: 
        if ch.isupper():
            count += 1
            if count >=2:
                return message.upper()
    return message

print(toUpperString("Hello World")); # type: ignore

def remove_duplicates(fruits):
    return list(set(fruits))

    # result = []

    # for fruit in fruits:
    #     if fruit not in result:
    #         result.append(fruit)
    # return result

#array can hold duplicate
#set cannot be duplicate

print(remove_duplicates(['Apple', 'Orange', 'Apple', 'Banana', 'Orange']))


def is_common(first, second):
    for i in first:
        if i in second:
            return True
    return False

print(is_common([1,2,3,4,5], [5,6,7,8]))

def second_smallest(numbers):
    return sorted(numbers)[1]


print(second_smallest([1, 5, 2, 3, 4]))


def split_list(lst, n):
    pass

print(split_list([1,2,3,4,5,6,7,8], 2))

def iterate_lists(fruits, freqs):
    
    for fruit, freq in zip(fruits, freqs):
        print("{}: {}".format(fruit, freq))

print(iterate_lists(['Apple', 'Banana', 'Orange'], [3,2,1])) # {'Apple' : 3, 'Banana' 2}

# Print how many times Apple has appear in the arrary
def get_frequencies(fruits):
    freqs = {}

    for fruit in fruits:
        if fruit in freqs.keys():
            freqs[fruit] += 1 # freqs['Apple'] =2
        else:
            freqs[fruit] = 1 # freqs['Apple'] =1
    return freqs

# return dict(Counter(fruits))




print(get_frequencies(['Apple', 'Orange', 'Banana', 'Apple', 'Orange', 'Apple']))
# {Apple: 3, Orange, Banana: 1}

