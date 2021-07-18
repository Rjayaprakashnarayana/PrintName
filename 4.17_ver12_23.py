def verify_12_23(a,n):
    b = 12 in a
    c= 23 in a
    return b and c

arr = [] 
n = int(input("Enter Number of Elements in array:"))
for i in range(n):
    b= int(input())
    arr.insert(i,b) 
d = verify_12_23(arr ,n)
print("Array Contains 12 and 23:")
print(d)
