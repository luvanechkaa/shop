def add():
    result = user_input_1 + user_input_2
    print(result)


def substract():
    result = user_input_1 - user_input_2
    print(result)


def multiply():
    result = user_input_1 * user_input_2
    print(result)


def divide():
    result = user_input_1 / user_input_2
    print(result)


while True:
    chosen_action = input(
        "Welcome to calculator :) Choose your action: 1.Add 2. Subtract 3. Multiply 4.Divide: ")

    user_input_1 = int(input("Enter the first number:"))
    user_input_2 = int(input("Enter the second number:"))

    if chosen_action == "+":
        print(user_input_1 + user_input_2)
        print(result)

    elif chosen_action == "-":
        result = user_input_1 - user_input_2
        print(result)

    elif chosen_action == "*":
        result = user_input_1 * user_input_2
        print(result)
    elif chosen_action == "/":
        result = user_input_1 / user_input_2
        print(result)

    user_input_1 = result
    print(result)
