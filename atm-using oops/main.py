class Atm:   #in class the functions build are called methods and if not in class then it is called functions.
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    def menu(self):
        value = input("Do you want to proceed(y/n):")
        if value.lower()=="y":
            self.pin = input("Please write your pin: ")

            val="0"
            while val!="4":
                val= input("""
                What do you want to do?
                    1.Deposit
                    2.Withdraw
                    3.Check Balance
                    4.Exit
        """)
            
                if val=="1":
                    self.deposit()
                elif val=="2":
                    self.withdraw()
                elif val=="3":
                    self.check_balance()
                else:
                    print("Bye.")
                    exit(1)
        else:
            print("Bye.")
            exit(1)
    def create(self):
        self.pin = input("Enter your pin: ")
        print("Pin set successful!!")
    def deposit(self):
        pin = input("Please first enter your pin: ")
        if pin==self.pin:
            amt = input("Enter the amount to be deposited: ")
            self.balance=self.balance+float(amt)
            print("Successfully deposited..")
        else:
            print("Incorrect pin!!!")
    def withdraw(self):
        pin = input("Please first enter your pin: ")
        if pin==self.pin:
            amt = input("Enter the amount to be withdrawed: ")
            if self.balance>float(amt):
                self.balance=self.balance-float(amt)
                print("Withdrawal of cash is successful..")
            else:
                print("Insufficient balance")
            
        else:
            print("Incorrect pin!!!")
    def check_balance(self):
        pin = input("Please first enter your pin: ")
        if pin==self.pin:
            print(f"Total balance is {self.balance}")
        else:
            print("Incorrect pin!!!")
a = Atm()

print(a.check_balance())