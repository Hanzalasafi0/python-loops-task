# Week 1 - Task 2
# Functions, Lists & Basic Data Handling

# Function to add two numbers
def add(a, b):
    return a + b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# List Example
numbers = [10, 20, 30, 40, 50]

print("Numbers in the list:")
for num in numbers:
    print(num)

print("Sum =", add(10, 20))
print("Multiplication =", multiply(5, 4))

# Add new element
numbers.append(60)

print("Updated List:")
print(numbers)

# Find largest number
print("Largest Number:", max(numbers))
