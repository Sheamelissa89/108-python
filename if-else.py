# Plant Watering Checker

plant = input("Enter the name of your plant: ")
days = int(input("How many days has it been since you watered it? "))

if days >= 14:
    print(f"Your {plant} definitely needs water.")
elif days >= 7:
    print(f"Check the soil before watering your {plant}.")
else:
    print(f"Your {plant} is still healthy and doesn't need water yet.")