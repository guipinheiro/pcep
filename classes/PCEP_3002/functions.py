def funcao(*args, **kwargs):
    for arg in args:
        print("Positional arg:", arg)
    print("Args:", args)
        
    for key, value in kwargs.items():
        print("Key:'", key, "' for value'", value, "'")
    print("Kwargs:", kwargs)
funcao(1, 2, a="k1", b="k2")

# def funcao2(a='', b): # it can't have position parameters after keyword args

# Same function using keyword args and regular args

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
    
adding(1,2,3)
adding(b = 2, c = 3, a = 1)

# Function the default value

def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
    
introduction('John')
introduction('John', 'Doe')

def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    
    print("Happy New Year!")
happy_new_year(False)
happy_new_year()

# None return
print(introduction('Guilherme'))

# Lists passed to a functions
def list_func(my_list):
    print('the items of my list')
    for items in my_list:
        print(items)
    return my_list
        
my_list = [1,3,5,'a']
print(list_func(my_list))

# Variable from the outside being used inside a function

def my_function():
    print("Do I know that variable?", var)

var = 1
my_function()
print(var)

def my_function2():
    var = 2
    print("Do I know that variable?", var)

var = 1
my_function2()
print(var)

# Using global to access a variable

def my_function2():
    global var
    var = 2
    print("Do I know that variable?", var)

var = 1
my_function2()
print(var)

# Recursion - a function calling itself

def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    return fib(n-1) + fib(n - 2)


for n in range(1, 10):
    print(n, "->", fib(n))
