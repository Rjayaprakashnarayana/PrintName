a = []
x=0 #flag for not found
n = int(input("Enter Number of Elements in an array:"))
for i in range(n):
    b= int(input())
    a.insert(i,b)
print(a)
c = int(input("Enter a number to be found its index in array:"))
for i in range(n):
    if(a[i]==c):
        x=1
        print("Index Is found at"+str(i))
        break
if (x==0):
    print("Element Found")