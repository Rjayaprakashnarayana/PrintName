def arithmetic(a,b,c):
    if(b=='+'):
        print("Result is :"+ str(a+c))
    elif(b=='-'):
        print("Result is :"+ str(a-c))
    elif(b=='*'):
        print("Result is :"+ str(a*c))
    elif(b=='/'):
        print("Result is :"+ str(a/c))

a= int(input())
b= input()
c = int(input())
arithmetic(a,b,c)