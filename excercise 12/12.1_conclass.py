class A:
    def __init__(self,x=2,y=3):
        if (x==2 and y==3):
            print("Constructor with no arguments")
        elif ((x!=2 and y==3) or (x==2 and y!=3)):
            print("Constructor with one arguments")
        else:
            print("Constructor with two arguments")

if __name__ == "__main__":
    A()
    A(5)
    A(6,7)