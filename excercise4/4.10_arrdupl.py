def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

a = []
n = int(input("Enter Number of Elements in an array:"))
for i in range(n):
    b= int(input())
    a.insert(i,b)
print("array:")
print(a)
print("Thr duplicate values in array are:")
print (Repeat(a))