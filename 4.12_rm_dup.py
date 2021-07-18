my_list = []
n = int(input("Enter Number of Elements in array:"))
for i in range(n):
    b= int(input())
    my_list.insert(i,b)
my_finallist = [i for j, i in enumerate(my_list) if i not in my_list[:j]] 
print(list(my_finallist))