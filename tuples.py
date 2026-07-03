# Create a tuple of plants
plants = ("Lily", "Petunia", "Haworthia", "Pothos")

print("Plant tuple:", plants)
print("Number of plants:", len(plants))

# Access items by index
print("First plant:", plants[0])
print("Third plant:", plants[2])

# Loop through the tuple
print("\nMy plants:")
for plant in plants:
    print(plant)

# Demonstrate that tuples are immutable
print("\nTuples cannot be changed after they are created.")