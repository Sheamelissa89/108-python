# -------------------------------
# MINI CHALLENGE: STUDENT REPORT CARD
# -------------------------------

# 1. Create a dictionary called "report_card"
report_card = {
    "name": "Shea",
    "subject": "Python Programming",
    "grades": (95, 92, 98)
}

# 2. Print the student's name and subject
print("Student Name:", report_card["name"])
print("Subject:", report_card["subject"])

# 3. Calculate the average of the 3 grades
average = sum(report_card["grades"]) / len(report_card["grades"])

# 4. Add a new key called "average"
report_card["average"] = average

print("Average Grade:", average)

# 5. Print a message based on the average
if average >= 90:
    print("Excellent!")
elif average >= 70:
    print("Good job!")
else:
    print("Needs improvement!")

# 6. Remove the "subject" key
report_card.pop("subject")

# Print the updated dictionary
print("Updated Report Card:")
print(report_card)