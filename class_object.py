class Shark: #creating Class
    def swim(self):
        print("The shark is swimming.")

    def be_awesome(self):
        print("The shark is being awesome.")


def main():
    sammy = Shark()#creating object
    sammy.swim() #creating signature
    sammy.be_awesome()

if __name__ == "__main__":
    main()