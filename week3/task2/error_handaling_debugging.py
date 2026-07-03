# Week 3 - Task 2
# Error Handling & Debugging Basics

print("=== Error Handling Example ===")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numbers only.")

except Exception as e:
    print("Unexpected Error:", e)

finally:
    print("Program executed successfully.")
