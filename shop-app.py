# thisdict = {
# "brand": "Ford",
#   "model": "Mustand",
# "year": 1964
# }
# print(thisdict["brand"])
all_products = [
    {"name": "cake", "price": "2.80$"},
    {"name": "candy", "price": "3.50$"},
    {"name": "chocolate", "price": "2$"},
    {"name": "lolipop", "price": "1$"},
    {"name": "icecream", "price": "4$"}

]

cart = []

print("Welcome to the Sweet-shop🛍️🍫🍬🍭🧁🍯💞🩷")
while True:

    user_input = input(
        "\n1. Add Product to cart \n2. Show cart \n3. Checkout \n4. Exit\n")

    match user_input:
        case "1":
            while True:
                for product in all_products:
                    print(f"{product['name']}, {product['price']}")
                user_choice = int(input("Which item would you like to add?:"))

                cart.append(all_products[user_choice - 1])
                for i, product in enumerate(cart):
                    print(i, product["name"])

        case "2":
            print(cart)
    print(cart)
