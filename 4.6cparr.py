def duplicate(a):
    return a
a = []
n = int(input("Enter Number of Elements in an array:"))
for i in range(n):
    b= int(input())
    a.insert(i,b)
print("Original array:")
print(a)
c = duplicate(a)
print("Duplicate array:")
print(c)