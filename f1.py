numbers = [3, 8, 11, 14, 20]

for number in numbers:
    if number % 2 == 0:
        print(number)


try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:
    print("Please enter a whole number.")