name = input("Type your name: ")
answer = input("You are on the dirt road, it has come to an end and you can go to left or right: ")

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. ")

    if answer == "swim":
        print("You swam acroos the river and were eaten by an alligator. ")
    elif answer == "walk":
        print("You walked for many miles, ran out of watter and you lost the game. ")
    else:
        print("Not a valid option. You lose. ")

elif answer == "right":
    answer = input("You come to a bridge, it looks woobly, do you want to cross it or head back (cross/back)? ").lower()
    if answer == "back":
        print("You go back and lose. ")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()
        if answer == "yes":
            print("You talk the stranger and they give you Gold. You Win! ")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose. ")
        else:
            print("Not a valid option. You lose. ")    

    else:
        print("Not a valid option. You lose. ")    
else:
    print("Not a valid option. You lose. ")

print("Thank you for trying", name)