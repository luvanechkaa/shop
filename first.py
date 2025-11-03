import os

todo_list = []
should_continue = True


def show_todos():
    for item in todo_list:
        print(item)


def add():

    is_adding = True
    while is_adding:
        os.system("cls")
        show_todos()
        user_input = input("Enter a to-do, say 'x' to quit: ")

        if user_input == "x":
            is_adding = False
        else:
            todo_list.append(user_input)


def delete():
    is_deleting = True
    while is_deleting:
        show_todos()
        user_input_1 = int(input("Enter the index of number: "))
        todo_list.pop(user_input_1 - 1)


def edit():
    is_editing = True
    while is_editing:
        show_todos()
        user_input_1 = int(input("Enter the index of number: "))
        user_input_2 = input("Enter the new value: ")
        todo_list[user_input_1 - 1] = user_input_2


while should_continue:
    action = input("Choose your action: 1. Add / 2. Delete / 3. Edit: ")
    if action == '1':
        add()
    elif action == '2':
        delete()
    elif action == "3":
        edit()


print("To do: ")
