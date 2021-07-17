def incredecrement(a,b):
    if(a=="++"):
        print("Value before increment"+str(b))
        b+=1
        print("Value after increment"+str(b))
    elif(a=="--"):
        print("Value before decrement"+str(b))
        b-=1
        print("Value after decrement"+str(b))

a= input("Enter increment / decrement operator (++ / --):")
b= int(input("Enter a Value:"))
incredecrement(a,b)
