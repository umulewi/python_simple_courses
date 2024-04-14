def subtract_numbers(num1, num2):
    """Function to subtract two numbers."""
    return num1 - num2

# Input two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Call the function to subtract the numbers
result = subtract_numbers(num1, num2)

# Display the result
print("The difference of", num1, "and", num2, "is:", result)
