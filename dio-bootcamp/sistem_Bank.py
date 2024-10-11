import sys
import time

red= "\033[91m"
white= "\033[0m"
green = "\033[92m"
blue = "\033[94m"

class Bank:
    def __init__(self, initial_balance=0.00): #initial value
      self.balance = initial_balance
      self.limit = {
                    "value_limit": 500,
                    "qtd": 3
                    }
      self.historic_account = [
          ('deposit', initial_balance)
      ]

    def sake(self):

        try:

            sake_value = float(input("\ninform the withdrawal amount\nR$:"))

            while sake_value < 1:
                print(f"-{red}value negative{white}")
                sake_value = float(input("\ninform the withdrawal amount\nR$:"))

            if sake_value <= self.limit['value_limit'] and self.limit['qtd'] > 0:

                self.limit["qtd"] -= 1
                print(f"\n-its daily value is {green}{self.limit['value_limit']}{white} and the withdrawal limit is {green}{self.limit['qtd']}{white} ")

                print(f"-Sake R$:{sake_value} loading....")
                time.sleep(2)

                if sake_value <= self.balance:

                    self.balance -= sake_value
                    self.historic_account.append(("sake", sake_value))
                    print(f"-withdrawal completed R$:{red}{sake_value}{white} remaining R$:{blue}{self.balance}{white}")
                    print("".center(50,'*'))

                else:

                    print(f"-insufficient balance,your balance R$:{red}{self.balance}.{white}")
                    print("".center(50,'*'))
            else:

                print(f"-Seu valor limite {green}{self.limit['value_limit']}{white} e o limite de saque diario {green}{self.limit['qtd']}{white}")


        except ValueError:

            print(f"-{red} entry incorrect,please, enter a valid value{white}")
            print("".center(50,'*'))

    def deposit(self):

        try:
            deposit_value =  float(input("\ninform the amount you will deposit: \nR$:"))

            while deposit_value < 1 :
                print("-value deposit negative")
                deposit_value = float(input("\ninform the amount you will deposit: \nR$:"))

            print(f"\n-deposit  loading....")
            time.sleep(2)
            self.balance += deposit_value
            self.historic_account.append(("deposit", deposit_value))
            print(f"-deposit  success of {green}{deposit_value}{white} equal {blue}{self.balance}{white}....")
            print("".center(50,'*'))

        except ValueError:

            print(f"-{red} entry incorrect,please, enter a valid value{white}")
            print("".center(50,'*'))

    def extract(self):

        print(f"\n-Your balance is R$:{blue}{self.balance:.2f}{white}\n")

        for transaction, value in self.historic_account:
            print(transaction, value)

        print("".center(50,'*'))

account = Bank(initial_balance=3000)


while True:
    print("option menu".center(50, '='))
    print("""
    [1] Sake
    [2] deposit
    [3] extract
    [4] exit
    """)
    print("".center(50,'='))
    
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
            print(f"{red}option invalid{white}")

    except ValueError:
        print(f"{red} entry incorrect,please, enter a valid value{white}")
        print("".center(50, '*'))


