answer = input("You are on the dirt road, it has come to an end and you can go to left or right")

if answer == "left":
    answer = input("You come to a river, ypu can walk around it or swim across.")

    if answer == "swim":
        print()
    elif answer == "walk":
        print()
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    print()
else:
    print("Not a valid option. You lose.")
