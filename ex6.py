import random #bringing the random from the library 
choice=input("enter rock, paper, or scissors (or 'q' to exit): ")
if choice=="q":
    exit() #exiting without completing the game 
choices=['rock', 'paper', 'scissors']
#computer choose randomly 
computer=random.choice(choices)
print(f"the computer chose {computer}")

if (computer=="rock") and (choice=="paper"):
    print("you win!")
elif (computer=="scissors") and (choice=="rock"):
    print("you win!")
elif (computer=="paper") and (choice=="scissors"):
    print("you win! ")
elif(computer==choice):
    print("it's a tie!")
else:
    print (" what a loser")


