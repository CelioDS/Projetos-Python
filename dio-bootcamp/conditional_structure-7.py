import sys
import time

red= "\033[91m"
white= "\033[0m"
green = "\033[92m"
blue = "\033[94m"

class Bank:
    def __init__(self, initial_balance=0): #initial value
      self.balance = initial_balance

    def sake(self):

        try:
            sake_value = float(input("\ninform the withdrawal amount\nR$:"))
            print(f"Sake R$:{sake_value} loading....")
            time.sleep(2)

            if sake_value <= self.balance:
                self.balance -= sake_value
                print(f"{red}withdrawal completed R$:{sake_value} remaining R$:{self.balance}{white}")
                print('_'*25)
            else:
                print(f"{red}insufficient balance,your balance R$:{self.balance}.{white}")
                print('_'*25)
        except ValueError:
            print(f"{red} entry incorrect,please, enter a valid value{white}")
            print('_'*25)

    def deposit(self):
        try:
            deposit_value =  float(input("\ninform the amount you will deposit: \nR$:"))
            print(f"deposit  loading....")
            time.sleep(2)
            self.balance += deposit_value
            print(f"{blue}deposit  success {self.balance}{white}....")
            print('_'*25)
        except ValueError:
            print(f"{red} entry incorrect,please, enter a valid value{white}")
            print('_'*25)

    def extract(self):
        print(f"{blue}Your balance is R$:{self.balance}{white}")
        print('_')

account = Bank(initial_balance=1000)


while True:
    print("\n ===== option menu ====="*1)
    print("1. Sake")
    print("2. deposit")
    print("3. extract")
    print("4. exit")

    try:
        option = int(input("choose your option:\n>>>"))

        if option == 1:
            account.sake()
        elif option == 2:
            account.deposit()
        elif option == 3:
            account.extract()
        elif option == 4:
          print(f"{red}exit...\033[0m")
          break
        else:
            sys.exit("option invalid")

    except ValueError:
        print(f"{red} entry incorrect,please, enter a valid value{white}")
        print('_'*25)


