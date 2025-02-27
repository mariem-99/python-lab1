def ch():
    s=input("enter a string")
    return s

def  lsub(s):
    ch1=""
    ch2=""
    i=0
    while i<len(s):
        if not(s[i] in ch2):
            ch2+=s[i]
        if len(ch2) > len(ch1):
            ch1=ch2
        i+=1
    return ch1

#principal 
s=ch()
print(f"the longest unique substring:{lsub(s)}")

            
        
        



