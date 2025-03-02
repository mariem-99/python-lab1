ch=input("enter a password: ")
char="!@#$^%&*()-_=+[]{};:.?,§¤¨'/\\|~><°"
is_special=False
is_letter=False
is_digit=False
i=0
while i<len(ch):
    if ("0"<=ch[i]<="9") :
        is_digit=True
    elif ("A"<=ch[i].upper()<="Z"):
        is_letter=True
    else:
        is_special=True
    i+=1

if is_digit and is_letter and is_special:
    print("password accepted")
else:
    print("password not strong enough!")