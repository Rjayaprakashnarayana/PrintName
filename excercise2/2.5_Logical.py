a= int(input("enter a value:"))
b= int(input("enter a value:"))
if(a not in [1,3,4]):#used not keyword
    print("a out of range")
elif(a==1 and b==2):#used and keyword
    print("Expected values")
elif(a==10 or b==12):#used or keyword
    print("One or both conditions satisfied")
