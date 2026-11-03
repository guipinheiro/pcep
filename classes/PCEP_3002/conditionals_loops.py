print("While...")
x = 10

while x > 0: # it can execute 0 times depending on the condition
    print(x)
    x -= 1

print("For with range(10)")
for y in range(10): # Range is not inclusive with its upper boundary. Thus, it will not print 10
    print(y)
    
print("For with range(2, 10)")
for y in range(2, 10):
    print(y)

print("For with range(0, 10, 2)")
for y in range(0, 10, 2):
    print(y)

