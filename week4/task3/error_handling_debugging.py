# Week 4 - Task 3
# Error Handling and Debugging

print("=== Error Handling Demo ===")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter only numbers.")

except Exception as e:
    print("Unexpected Error:", e)

finally:
    print("Program finished.")

print("\n=== List Example ===")

numbers = [10, 20, 30]

try:
    index = int(input("Enter list index (0-2): "))
    print("Value:", numbers[index])

except IndexError:
    print("Error: Index out of range.")

except ValueError:
    print("Error: Enter a valid integer.")

print("\nDebugging completed successfully.")
