num = int(input("Enter a number: "))
i = 1
print("Odd numbers below", num, "are:")
while i < num:
    if i % 2 != 0:
        print(i)
    i += 1
