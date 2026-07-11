"""
Mini Challenge: Multiplication Table

1. Ask the user to enter a number.
2. Store it in a variable called num.
3. Use a for loop with range(1, 11).
4. Multiply num by each number from 1 to 10.
"""

num = int(input("Enter a number: "))

print(f"\nMultiplication table for {num}:\n")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")