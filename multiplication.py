def multiply_numbers(num1, num2):
    """Function to multiply two numbers."""
    return num1 * num2

# Input two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Call the function to multiply the numbers
result = multiply_numbers(num1, num2)

# Display the result
print("The product of", num1, "and", num2, "is:", result)
