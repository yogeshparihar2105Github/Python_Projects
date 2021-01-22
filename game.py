n =18

print("#This game is developed by Yogesh Parihar# \n\n **Rules:\n You have to guess the correct no. to win this game\n you have only 5 chances to do this otherwise you will loss the game\n And the game will be over**\n\nLet's play the game\nBest of LUCK")
num = 0
chances=5
while(chances>0 and num!=n):
    print("\nyou have only",chances, "chances left")
    print("Guess the no.")
    num=int(input())
    if num>n:
        print("this number is greater than the hidden no.")
    elif num==n:
        print("\nYou are correct")
        print("\nYou have won in",5-chances+1,"attempt")
    else:
        print("this number is lesser than the hidden no.")
    chances=chances-1 
  
if (chances==0):
    if(num==n):
        print(" ")
    else:
        print("\nYou have lost the game\nThe hidden no. was 18\n\tGame Over!")
