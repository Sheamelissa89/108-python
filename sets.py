# Create a set of plants
plants = {"Lily", "Petunia", "Haworthia", "Pothos"}

print("Original set:", plants)
print("Number of plants:", len(plants))

# Add a new plant
plants.add("Caladium")
print("\nAfter adding Caladium:", plants)

# Remove a plant
plants.remove("Petunia")
print("\nAfter removing Petunia:", plants)

# Check if an item exists
print("\nIs Haworthia in the set?", "Haworthia" in plants)

# Loop through the set
print("\nMy plants:")
for plant in plants:
    print(plant)