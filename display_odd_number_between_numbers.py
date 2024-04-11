a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(" the odd number between ", a,"And", b,"are:")
for i in range(a, b+1):
    if i%2!=0:
        print(i)
