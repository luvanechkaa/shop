import os
# thisdict = {
# "brand": "Ford",
#   "model": "Mustand",
# "year": 1964
# }
# print(thisdict["brand"])
all_products = [
    {"name": "cake", "price": 2.80},
    {"name": "candy", "price": 3.50},
    {"name": "chocolate", "price": 2},
    {"name": "lolipop", "price": 1},
    {"name": "icecream", "price": 4}

]

cart = []
true_password = "admin"
print("Welcome to the Sweet-shop🛍️🍫🍬🍭🧁🍯💞🩷")
user_login = input(
    "Are you a costumer or administrator? 😊 Press 'C' for Costumer🛍️, and 'A' for administrator🧁: ")
if user_login == "A":
    password = input("Please enter the password: ")
    if password == true_password:
        while True:
            admin_input = input(
                "Welcome, administrator! Choose your action:\n1.Show list of products\n2.Add item \n3.Delete item \n4.Edit an existing item\n5.Exit:")

            os.system("cls")
            match admin_input:
                case "1":
                    os.system("cls")
                    print("The list of products is:")
                    for product in all_products:
                        print(product['name'])
                case "2":
                    admin_item = input("Enter the new item: ")
                    admin_price = int(input("Enter the price: "))
                    all_products.append(
                        {"name": admin_item, "price": admin_price})
                    print("Your new list of products:")
                    for product in all_products:
                        print(f"{product['name']}:{product['price']}")
                case "3":
                    print("This is your current list:")
                    for product in all_products:
                        print(f"{product['name']}:{product['price']}")
                    admin_choice_to_delete = int(
                        input("Please choose the index of item you would like to delete: "))
                    del all_products[admin_choice_to_delete - 1]
                    print("Your new list: ")
                    for product in all_products:
                        print(f"{product['name']}:{product['price']}")
                case "4":
                    print("This is your current list:")
                    for product in all_products:
                        print(f"{product['name']}:{product['price']}")
                    admin_choice_to_edit = int(
                        input("Please choose the index of item you would like to edit: "))
                    new_name = input("Enter the name of new item: ")
                    new_price = int(input("Enter the new price: "))
                    all_products[admin_choice_to_edit - 1]['name'] = new_name
                    all_products[admin_choice_to_edit - 1]['price'] = new_price
                    print("Your new list of products:")
                    for product in all_products:
                        print(f"{product['name']}:{product['price']}")
                case "5":
                    break
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

elif user_login == "C":
    while True:

        user_input = input(
            "\n1. Add Product to cart \n2. Show cart \n3. Checkout \n4. Exit\n")
        os.system("cls")

        match user_input:
            case "1":
                os.system("cls")
                isAdding = True
                while isAdding:
                    for product in all_products:
                        print(f"{product['name']}, {product['price']}")
                    user_choice = input(
                        "Which item would you like to add? To go back press X:")

                    if user_choice == "X":
                        break
                    elif user_choice == "x":
                        break
                    else:
                        user_choice = int(user_choice)

                    os.system("cls")

                    cart.append(all_products[user_choice - 1])
                    for i, product in enumerate(cart):
                        print(i + 1, product["name"])

            case "2":
                os.system("cls")
                for product in cart:
                    print(product["name"])

            case "3":
                os.system("cls")
                summe = 0
                for product in cart:
                    summe = product["price"] + summe
                print(summe)

            case "4":
                break
            case _:
                print("Invalid input")
