decimal_value = int(input("Enter decimal value: "))
binary_value = bin(decimal_value)
print("The binary representation is:", binary_value[2:]) # removes the prefix when printing
octal_value = oct(decimal_value)
print("The octal representation is:", octal_value)
hex_value = hex(decimal_value)
print("The hex representation is:", hex_value)
x = 3E4
print("A number created using cientific notation:", x)
print(.1 + .2 == .3)