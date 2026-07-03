# Create a dictionary about a student
student = {
    "name": "Shea",
    "course": "Python",
    "grade": 95
}
print("Original dictionary:", student)
print("Dictionary length:", len(student))

# Access values using keys
print("Student name:", student["name"])
print("Course:", student["course"])

# Add a new key
student["status"] = "active"
print("After adding status:", student)
print("Dictionary length:", len(student))

# Update an existing value
student["grade"] = 100
print("After updating grade:", student)
print("Dictionary length:", len(student))

# Remove a key
student.pop("status")
print("After removing status:", student)
print("Dictionary length:", len(student))