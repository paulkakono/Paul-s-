
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")



while True:
    try:
        age = int(input("Enter your age:"))
        break           # leave the loop if conversion worked
    except ValueError:
        print("Please Enter a whole number:")
print("Age recorded:, age")




try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success:", result)

