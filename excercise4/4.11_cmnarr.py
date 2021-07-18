a = []
n1 = int(input("Enter Number of Elements in 1st array:"))
for i in range(n1):
    b= int(input())
    a.insert(i,b)
c=[]
n2 = int(input("Enter Number of Elements in 2nd array:"))
for i in range(n2):
    b= int(input())
    c.insert(i,b)
a_as_list =set(a)
intersextion = a_as_list.intersection(c)
interaction_as_list = list(intersextion)
print(interaction_as_list)