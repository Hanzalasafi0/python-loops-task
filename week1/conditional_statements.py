# Conditional Statements & Loops in Python

num = int(input("Enter a number: "))

# Check Even or Odd
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

# Print numbers from 1 to 10
print("\nNumbers from 1 to 10:")
for i in range(1, 11):
    print(i)

# While loop example
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1

print("Done!")
