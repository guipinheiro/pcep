a_list = [1, 3, 5]
a_tuple = (2, 4, 6)
a_dict  = {'a': 8, 'b': 9}

# Lists

# Lists are mutable

a_list.pop()
print(a_list)
a_list.append(5)
print(a_list)

print('is 5 in list:', 5 in a_list)

# Tuples are not mutable

print(a_tuple[1])
# a_tuple[1] = 5 # this code will generate an error
# print(a_tuple)

# Ordering a list
print('Ordering a list')
numbers = [5, 1, 3, -2, 1]

changes = 1
while changes != 0:
    changes = 0
    for i in range(1, len(numbers)):
        if (numbers[i - 1] > numbers[i]):
            changes += 1
            numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
        print(str(numbers))
        
# Remove an item from a list

print('Removing items')

list_a = [1,3,5]
del list_a[2]
print(list_a)
list_a.pop() # default pop value is -1, but you can select any index
print(list_a)
list_a.pop(0)
print(list_a)

# Using negative index
print('Using negative index')

list_b = [1, 2, 3, 4]
print(list_b[-2]) # Access the value 3

# Adding items to a list using insert(location, value)
print('adding values to a list')

list_c = [1,3,4]
list_c.insert(1, 2)
print(list_c)

# sorting using sort
print('sorting using sort')

lst = ["D", "F", "A", "Z"]
lst.sort()

print(lst)

# The name of a list is the name of a memory location where the list is stored.

print('Assign a list to another')

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

# You can create a copy of a list by slicing it
print('Slicing to create a copy')
list_2 = list_1[:]
list_1[0] = 3
print(list_2)
print(list_1)

# You can slice using negative numbers
print('Slicing with negative')
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-3:-1]
print(new_list)

# Deleting more than one item using slicing
print('deleting using slice')
list_to_del = [1, 2, 3, 4, 5]
del list_to_del[1:3]
print(list_to_del)

# List comprehension
print('List comprehension')
row = [i for i in range(8)]
print(row)

squares = [x ** 2 for x in range(10)]
print(squares)
odds = [x for x in squares if x % 2 != 0 ]
print(odds)

# Two dimensional array
print('Two dimensional array')
board = []

board = [[(j, i) for i in range(8)] for j in range(8)]
    
print(board)
print(board[0][1])

