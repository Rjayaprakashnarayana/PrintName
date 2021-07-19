class A:
    def __init__(self):
        print("Default Constructor")
    def __init__(self,x):
        print("Constructor with one argument")
    def __init__(self,x,y):
        print("Constructor with two argument")

if __name__ == "__main__":
    A()
    A(5)
    A(6,7)