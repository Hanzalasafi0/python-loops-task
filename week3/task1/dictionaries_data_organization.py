# Week 3 - Task 1
# Dictionaries & Data Organization

# Create a dictionary
student = {
    "Name": "Hanzala Safi",
    "Age": 20,
    "Course": "Python Development",
    "City": "Patna"
}

# Display dictionary
print("Student Details:")
for key, value in student.items():
    print(f"{key}: {value}")

# Update dictionary
student["Age"] = 21
student["Status"] = "Intern"

print("\nUpdated Student Details:")
for key, value in student.items():
    print(f"{key}: {value}")

# Access a value
print("\nCourse:", student["Course"])
