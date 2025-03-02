while True:
    choice=input("enter operator (+, -, *, /) or 'q' to quit : ")
    if choice=="q":
        exit()

    
    a=float(input("enter the first number:"))
    b=float(input("enter the second number: "))

    match choice:#like switch in c 
        case "+":
            print( a + b )
        case "-":
            print(a - b)
        case "*":
            print(a * b)
        case "/":
            if b!=0:#make sure that we can do this operation 
                print(a / b)
            else:
                print("error")
        case _:
            print("invalid operator")
        
        

    