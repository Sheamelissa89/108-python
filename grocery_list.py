# -------------------------------
# MINI CHALLENGE: THE GROCERY LIST
# -------------------------------

# 1. Create a list called "groceries" with at least 5 items.
groceries = ["bread", "apples", "cheese", "chicken", "rice"]

# 2. Print the first and last item using indexing.
print("First item:", groceries[0])
print("Last item:", groceries[-1])

# 3. Use slicing to print just the first 3 items.
print("First 3 items:", groceries[:3])

# 4. Add "eggs" to the end of the list using append().
groceries.append("eggs")

# 5. Insert "milk" at the very beginning of the list.
groceries.insert(0, "milk")

# 6. Remove one item using remove().
groceries.remove("cheese")

# 7. Check if "bread" is in the list.
if "bread" in groceries:
    print("Bread is in the grocery list.")
else:
    print("Bread is NOT in the grocery list.")

# 8. Print how many items are in the final list.
print("Total number of items:", len(groceries))

# Print the completed grocery list.
print("Final Grocery List:", groceries)