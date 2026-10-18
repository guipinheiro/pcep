# Implicit declaration
my_str_var = '10'
my_int_var = 10
print(type(my_str_var))
print(type(my_int_var))

# Variables are mutable
print(my_int_var)
my_int_var += 1
print(my_int_var)
my_int_var = "texto" # you can even change its type
print(my_int_var)