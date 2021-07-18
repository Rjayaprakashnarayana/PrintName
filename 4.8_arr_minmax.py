def minmax(a,n):
    min =9999
    max=0
    for i in range(n):
        if(a[i]<min):
            min = a[i]
        if(a[i]>max):
            max = a[i]
    return min, max

a = []
n = int(input("Enter Number of Elements in an array:"))
for i in range(n):
    b= int(input())
    a.insert(i,b)
print("array:")
print(a)
min1,max1= minmax(a,n) 
print("min value:"+str(min1))
print("max value:"+str(max1))