# Assignment 1: Numeric Operations and String Concatenation

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined"

print("\nResults of Numeric Operations:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# string concatenation

concate_result = str(int(num1)) + str(int(num2))
print("\nString Concatenation Result:", concate_result)
