def evodd(a,n):
    even=0
    odd=0
    for i in range(n):
        if(a[i]%2==0):
            even+=1
        elif(a[i]%2==1):
            odd+=1
    return even,odd

arr = [] 
n = int(input("Enter Number of Elements in array:"))
for i in range(n):
    b= int(input())
    arr.insert(i,b) 
even,odd = evodd(arr, n)
print("No fo even elements in array:"+str(even))
print("No fo odd elements in array:"+str(odd))