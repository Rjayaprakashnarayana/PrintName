def rev(a,n):
    c=[]
    for i in range(n):
       c.insert(i,a[n-i+1])
    return c
   

a = []
n = int(input("Enter Number of Elements in an array:"))
for i in range(n):
    b= int(input())
    a.insert(i,b)
print("array:")
print(a)
a = rev(a,n)
print("After Reversing an array:")
print(a)