print(int(3.6))
print(int(float("3.6")))
try:
    print(int(float("H")))
except ValueError:
    print("valor inválido")
finally:
    print('Try except is over')
    
print(float(True))
print(str(True))

print('--- Bool')
print(bool(' '))
print(bool(''))
print(bool(0))
print(bool(1))