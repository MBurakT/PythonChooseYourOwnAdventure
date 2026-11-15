def play():
    name = input("Type your name: ")

    print(f"Welcome {name} to this adventure!\n")

    answer = input(
        "You are on a dirt road, it has come to an end you can go left or right. Which way would you like to go?").lower()

    if answer == "left":
        answer = input(
            "You come to river, you can walk around it or swim across? Type walk to walk and swim to swim across: ").lower()
        if answer == "swim":
            print("You swam across and were eaten by an alligator")
        elif answer == "walk":
            print("You walked for many miles, ran out of water and you lost the game")
        else:
            print("Not a valid option. You lose")
    elif answer == "right":
        answer = input(
            "You came to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)").lower()
        if answer == "back":
            print("You go back and win.")
        elif answer == "cross":
            print(
                "You cross the bridge and meet a stranger and you lose")
        else:
            print("Not a valid option. You lose")
    else:
        print("Not a valid option. You lose")

    input("Enter any key to quit.")


play()
