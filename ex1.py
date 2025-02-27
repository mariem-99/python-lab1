a=int( input ("enter a="))
def fact(a):
    if a==0 or a==1:
        return 1
    else:
        return a * fact(a-1)
    
print(f"the factoral is {a} is {fact(a)}")