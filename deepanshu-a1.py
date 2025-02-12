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
