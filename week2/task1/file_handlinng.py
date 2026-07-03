# Week 2 - Task 1
# File Handling in Python

# Step 1: Write data to a file
with open("student_data.txt", "w") as file:
    file.write("Name: Hanzala Safi\n")
    file.write("Course: Python Internship\n")
    file.write("Week: 2 Task: 1\n")

print("Data written successfully.")

# Step 2: Read data from the file
with open("student_data.txt", "r") as file:
    data = file.read()

print("\nReading Data from File:")
print(data)

# Step 3: Append new data
with open("student_data.txt", "a") as file:
    file.write("Status: Completed\n")

print("\nNew data added successfully.")

# Step 4: Read updated file
with open("student_data.txt", "r") as file:
    updated_data = file.read()

print("\nUpdated File Content:")
print(updated_data)
