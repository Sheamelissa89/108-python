from catalog import catalog  # Imports the catalog list from catalog.py


# GLOBAL VARIABLE
cart = []


# HELPER FUNCTIONS
def header(text):
    print("------------------")
    print(text)
    print("------------------")


def menu():
    print("Menu")
    print("1. View Catalog")
    print("2. Search Product")
    print("3. View Cart")
    print("Q. Quit")


# CATALOG AND CART FUNCTIONS
def print_catalog():
    header("Our Catalog")

    for prod in catalog:
        print(
            f'| {prod["id"]} | '
            f'{prod["title"].ljust(15)} | '
            f'${prod["price"]:.2f} |'
        )

    answer = input("Type ID to add (N to close): ")

    if answer.lower() == "n":
        return

    add_product_to_cart(answer)


def add_product_to_cart(prod_id):
    found = False

    for prod in catalog:
        if str(prod["id"]) == str(prod_id):
            found = True
            cart.append(prod)
            print(f'{prod["title"]} added to your cart.')
            break

    if not found:
        print("** ERROR: Invalid ID **")


def search_product():
    text = input("Search product: ").lower()
    found = False

    for prod in catalog:
        if text in prod["title"].lower():
            found = True

            print(
                f'Found: ID {prod["id"]} | '
                f'{prod["title"].ljust(15)} | '
                f'${prod["price"]:.2f} |'
            )

            choice = input(
                "Do you want to add this item to your cart? (y/n): "
            )

            if choice.lower() == "y":
                add_product_to_cart(prod["id"])

            break

    if not found:
        print("Sorry, this item does not exist.")


def view_cart():
    header("Your Cart")

    if not cart:
        print("Your cart is empty.")
        return

    for prod in cart:
        print(
            f'| {prod["id"]} | '
            f'{prod["title"].ljust(15)} | '
            f'${prod["price"]:.2f} |'
        )


# MAIN PROGRAM LOOP
option = ""

while option.lower() != "q":
    header("Welcome to Store XY")
    menu()

    option = input("Choose an option: ")

    if option == "1":
        print_catalog()

    elif option == "2":
        search_product()

    elif option == "3":
        view_cart()

    elif option.lower() == "q":
        print("Goodbye!")

    else:
        print("** ERROR: Invalid option **")