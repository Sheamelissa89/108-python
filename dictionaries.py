# Create a dictionary about a plant
plant = {
    "name": "Haworthia",
    "type": "Succulent",
    "location": "Balcony",
    "watering": "Every 2 weeks"
}

print("Original dictionary:", plant)
print("Dictionary length:", len(plant))

# Access values using keys
print("Plant name:", plant["name"])
print("Location:", plant["location"])

# Add a new key
plant["status"] = "Blooming"
print("After adding status:", plant)
print("Dictionary length:", len(plant))

# Update an existing value
plant["location"] = "Kitchen Window"
print("After updating location:", plant)
print("Dictionary length:", len(plant))

# Remove a key
plant.pop("status")
print("After removing status:", plant)
print("Dictionary length:", len(plant))

# Loop through the dictionary
print("\nPlant Information:")
for key, value in plant.items():
    print(f"{key}: {value}")