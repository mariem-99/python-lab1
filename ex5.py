x=53
i=0
a=int(input("guess a number between 1 and 100: "))

while (x!=a) and (1<=a<=100):
    a=int(input("guess a number between 1 and 100: "))
    i+=1
    if (a<x):
        print("too low")
    elif (a>x):
        print("too high")
    else:
        print("you win !")
    