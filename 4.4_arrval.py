def search(c,a):
    return c in a
a = []
n = int(input("Enter Number of Elements in an array:"))
for i in range(n):
    b= int(input())
    a.insert(i,b)
print(a)
c = int(input("Enter a number to be searched:"))
d = search(c,a)
print(d)