def remele(c,a):
    a.pop(c)
    return a
a = []
n = int(input("Enter Number of Elements in an array:"))
for i in range(n):
    b= int(input())
    a.insert(i,b)
print(a)
c = int(input("Enter a number to be removed:"))
for i in range(n):
    if(a[i]==c):
        f=i
        break
d = remele(f,a)
print("Array After removing element:")
print(d)