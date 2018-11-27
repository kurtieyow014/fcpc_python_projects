#number1

print("number 1")
for n in range(8):
    print(2**n,end='\t')
print()

#number2

print("number 2")
for n in range (1,13):
    if n % 4 == 0:
        print("S", end='\t')
    else:
        print(n, end='\t')
print()

#number3

print("number 3")
for n in range(1, 9):
    if n % 8 == 1:
        print(n, end='\t')
    else:
        print("E",end='\t')
print()
