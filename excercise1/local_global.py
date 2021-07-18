a =1 #global variable
def local():
    a=3 #local variable
    print(a)#prints local variable


if __name__ == "__main__":
    print(a)#prints global variable
    local()
    print(a)#prints global variable