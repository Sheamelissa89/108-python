"""
Mini Challenge: Password Checker

1. Ask the user to enter a password
2. Check if it's correct (password: "secret123")
3. If it's wrong, print "Wrong! Try again." and ask again
4. When they enter the correct password, print "Access granted!"
"""

password = input("Enter the password: ")

while password != "secret123":
    print("Wrong! Try again.")
    password = input("Enter the password: ")

print("Access granted!")