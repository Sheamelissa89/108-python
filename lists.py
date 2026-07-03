# Create a list of favorite foods
foods = ["pizza", "tacos", "spaghetti", "salad"]
print("Original list:", foods)
print("List length:", len(foods))

# Access items by index
print("First food:", foods[0])
print("Third food:", foods[2])

# Replace a value
foods[1] = "sushi"
print("After replacing tacos with sushi:", foods)
print("List length:", len(foods))

# Remove an item by value
foods.remove("salad")
print("After removing salad:", foods)
print("List length:", len(foods))

# Remove an item by index
foods.pop(0)
print("After removing the first item:", foods)
print("List length:", len(foods))