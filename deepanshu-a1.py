# Main program for Arnold's Amazing Eats Ordering System starts here
#this while loop will keep running until the user confirms the order
  
while True:
    print(" Welcome to Arnold's Amazing Eats Ordering System! ")
    print("=" * 50)
    print("We offer delicious meals delivered to your doorstep.")
    print("Please follow the prompts to place your order.")
    print("-" * 50)

    # Collecting user information

    # Collecting user's name
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # Collecting user's full delivery address
    address = input("Enter your full delivery address: ")
    city = input("Enter your city: ")
    province = input("Enter your province: ")
    postal_code = input("Enter your postal code: ")

    # Collecting user's phone number and delivery instructions
    phone_number = input("Enter your phone number: ")
    delivery_instructions = input("Any special delivery instructions? ")
    print(" ")
    print("Thank you for providing your information.")
    print("=" * 50)

    # Displaying the menu
    print("Here is our menu for today:")
    print("-" * 50)

#storing menu as dictionary key-value pairs
    menu = {
        "1": {"name": "Spaghetti Carbonara", "price": 12.99},
        "2": {"name": "Grilled Chicken Wings", "price": 14.99}
    }
  

    print("\nMenu:")
#displaying items from menu dictionary using for loop
    for key, item in menu.items():
        print(f"{key}) {item['name']} - ${item['price']:.2f}")

# Taking user selection and loop until user selects 1 or 2
    meal_choice = input("Select a meal (1 or 2): ")
    while meal_choice not in menu:
        meal_choice = input("Invalid choice! Please select 1 or 2: ")

# Taking user input for quantity
    quantity = int(input("Enter quantity: "))

    # Order confirmation and loop until user confirms
    print("\nOrder Summary:")
    print(f"Meal: {menu[meal_choice]['name']}")
    print(f"Quantity: {quantity}")

    confirm = input("Confirm Order? (y/n): ").strip().lower()
    while confirm not in ["y", "n"]:
        confirm = input("Invalid input. Please enter 'y' or 'n': ").strip().lower()

    if confirm == "y":
        break

    else:
        print("\nLet's start over!\n")
