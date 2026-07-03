# Functions, Lists & Basic Data Handling

# Function to add two numbers
def add(a, b):
    return a + b

# Function to find maximum number
def find_max(numbers):
    return max(numbers)

# List example
numbers = [10, 20, 30, 40, 50]

print("Numbers in the list:")
for num in numbers:
    print(num)

print("Sum of 5 and 10 =", add(5, 10))
print("Maximum number =", find_max(numbers))

# Adding a new element
numbers.append(60)

print("Updated List:")
print(numbers)
