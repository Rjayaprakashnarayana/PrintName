def insert_pos(a,ele,pos):
    a.insert(pos,ele)
    return a
a = []
n = int(input("Enter Number of Elements in an array:"))
for i in range(n):
    b= int(input())
    a.insert(i,b)
print("Original array:")
print(a)
elem = int(input("Enter element to be added:"))
pos = int(input("Enter element position:"))
print("array after adding element at required position:")
a= insert_pos(a,elem,pos)
print(a)