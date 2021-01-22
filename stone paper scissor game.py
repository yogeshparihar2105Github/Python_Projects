import random
print("\n\t\t\tThis is stone-paper-scissor Game\n\t\t\tDo you want to play with me\n\t\t\tYou have only 10 chances jiske jayda point honge wo jeet jayega\n\n")
i=0
j=0
chances=10
while chances>0:
    lst = ["stone","paper","scissor"]
    computer_turn = random.choice(lst)  

    ust ={"s":"stone","p":"paper","sc":"scissor"}
    user_turn = input("\nEnter your move\nPress s for stone\nPress sc for scissor\nPress p for paper\nYour move : ") 
    if user_turn=="s" or user_turn=="sc" or user_turn=="p":

        if computer_turn=="stone" and user_turn=="sc":
            print("\ncomputer entered", computer_turn)
            j=j+1
            print("YOU LOSS")
        elif computer_turn=="stone" and user_turn=="p":
            print("\ncomputer entered", computer_turn)
            i=i+1
            print("YOU WIN")
        elif computer_turn=="stone" and user_turn=="s":
            print("\ncomputer entered", computer_turn)
            print("DRAW")

        elif computer_turn=="scissor" and user_turn=="sc":
            print("\ncomputer entered", computer_turn)
            print("DRAW")
        elif computer_turn=="scissor" and user_turn=="p":
            print("\ncomputer entered", computer_turn)
            j=j+1
            print("YOU LOSS")
        elif computer_turn=="scissor" and user_turn=="s":
            print("\ncomputer entered", computer_turn)
            i=i+1
            print("YOU WIN")

        elif computer_turn=="paper" and user_turn=="sc":
            print("\ncomputer entered", computer_turn)
            i=i+1
            print("YOU WIN")
        elif computer_turn=="paper" and user_turn=="p":
            print("\ncomputer entered", computer_turn)
            print("DRAW")
        elif computer_turn=="paper" and user_turn=="s":
            print("\ncomputer entered", computer_turn)
            j=j+1
            print("YOU LOSS")
        chances=chances-1
    else:
        print("\n\t\t\t\t-----ERROR-----\nPlease enter only the char which are given above otherwise you won't be able to play with me")

print("\nyour point", i)
print("\ncomputer point", j)
print("\ndraw time", 10-i-j)
if i>j:
    print("\n\t\t\tCongratulations!!!You won the game")
elif i==j:
    print("\n\t\t\tThe Game Draw")
else:
    print("\n\t\t\tYou loss the game")
