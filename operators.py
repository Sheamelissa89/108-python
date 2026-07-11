# operators.py

# Arithmetic operators
number_one = 20
number_two = 6

print("Arithmetic Operators:")
print(f"{number_one} + {number_two} = {number_one + number_two}")
print(f"{number_one} - {number_two} = {number_one - number_two}")
print(f"{number_one} * {number_two} = {number_one * number_two}")
print(f"{number_one} / {number_two} = {number_one / number_two}")
print(f"{number_one} // {number_two} = {number_one // number_two}")
print(f"{number_one} % {number_two} = {number_one % number_two}")
print(f"{number_one} ** 2 = {number_one ** 2}")

# Comparison operators
print("\nComparison Operators:")
print(f"{number_one} > {number_two}: {number_one > number_two}")
print(f"{number_one} < {number_two}: {number_one < number_two}")
print(f"{number_one} == {number_two}: {number_one == number_two}")
print(f"{number_one} != {number_two}: {number_one != number_two}")

# Logical operators
has_money = True
store_is_open = True

print("\nLogical Operators:")
print(f"Can shop: {has_money and store_is_open}")
print(f"At least one condition is true: {has_money or store_is_open}")
print(f"Does not have money: {not has_money}")