# functions.py

# Function with no parameters
def greet_user():
    print("Welcome to Shea's plant care program!")


# Function with one parameter
def display_plant(plant):
    print(f"Plant: {plant}")


# Function with return value
def calculate_watering_days(days_since_watered):
    return 14 - days_since_watered


# Function using a list
def display_all_plants(plants):
    print("\nMy plant collection:")
    for plant in plants:
        print(plant)


# Calling the functions
greet_user()

favorite_plant = "Haworthia"
display_plant(favorite_plant)

days_since_watered = 6
days_left = calculate_watering_days(days_since_watered)

print(f"\nDays since watered: {days_since_watered}")
print(f"Days left before watering again: {days_left}")

plant_collection = ["Lily", "Petunia", "Haworthia", "Pothos", "Caladium"]
display_all_plants(plant_collection)