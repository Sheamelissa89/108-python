# loops.py

# A list of plants
plants = ["Lily", "Petunia", "Haworthia", "Pothos", "Caladium"]

# For loop
print("My plants:")
for plant in plants:
    print(plant)

# For loop with numbers
print("\nCounting plant care days:")
for day in range(1, 6):
    print(f"Day {day}: Check soil and sunlight.")

# While loop
water_count = 0

print("\nWatering reminder:")
while water_count < 3:
    print("Check one plant for water.")
    water_count += 1