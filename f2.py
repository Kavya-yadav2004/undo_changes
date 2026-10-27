number = int(input("Enter a nonnegative integer: "))
factorial = 1

for value in range(2, number + 1):
    factorial *= value

print(factorial)