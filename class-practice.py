print("Hello world from Shea's Python project!")
print(2)
print(5 + 3)
print(True)

# SHORTCUTS
# ctrl + s = save
# up arrow key = previous command
# ctrl + - = zoom out

'''
This is a multi-line comment.
Triple quotes can be used around longer comments.
'''

# Variables and concatenation
name = "Shea"
age = 36

print(name, age)
print("My name is " + name + " and I am " + str(age) + " years old.")

"""
Mini Challenge 1:
Write a short story using variables.
"""

place = "Disneyland"
activity = "riding the rollercoaster"
members = 3
store = "Disney store"
bought = "Mickey ears"

print("The last time I went to " + place + ", I had a great time " + activity + " with " + str(members) + " people, and we went to buy " + bought + " at the " + store + ".")

# F-string version
print(f"The last time I went to {place}, I had a great time {activity} with {members} people, and we went to buy {bought} at the {store}.")

# Multi-line f-string
print(f"""
The last time I went to {place}, 
I had a great time {activity} with {members} people, 
and we went to buy {bought} at the {store}.
""")

# TYPE FUNCTIONS
print(type(name))
print(type(members))
print(type(True))

# CASTING
print(20 + int("20"))
print(20 + age)

# INPUT FUNCTION
user_age = int(input("Enter your age: "))
print(f"Hello! You are {user_age} years old.")

# Converting input to int
new_age = int(input("Enter another age: "))
print(user_age + new_age)

"""
Pizza Calculator:
1. Ask how many slices of pizza
2. Ask how many people
3. Divide slices by people
4. Show the result with an f-string
"""

pizza_slices = int(input("How many slices of pizza do you have? "))
people = int(input("How many people are sharing the pizza? "))

slices_per_person = pizza_slices / people

print(f"Each person gets {slices_per_person} slices of pizza.")