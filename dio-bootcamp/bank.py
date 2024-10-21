import time
from datetime import datetime
import pytest
import random

red= "\033[91m"
white= "\033[0m"
green = "\033[92m"
blue = "\033[94m"

'''
criar clientes e fazer verificação
mudar menu para primeiro menu com criar conta e acessar contard
depois que estiver na conta mostrar os menus de acções


'''
def run_test():
    pytest.main(["-s", "bank_test.py"])

def get_current_time():
    return datetime.now().strftime("%H:%M-%d/%m/%Y")

class Bank:
    def __init__(self, initial_balance=0.00):
      self.balance = initial_balance
      self.limit = {
                    "value_limit": 500,
                    "qtd": 3,
                    "transaction": 10
                    }
      self.historic_account = list()
      self.historic_transactions = []
      self.account_default = '0001'
      self.account_user = []


    def historic_transaction_log(self,func):
        self.historic_transactions.append([get_current_time(), func.__name__.upper()])
        print('='*50)
        print(f'~[{get_current_time()}] - FUNC: {func.__name__.upper()} - STATUS: OK')
        print('=' * 50)
        return

    def create_account(self, name=None, cpf=None):
        branch = random.choices(range(0, 10), k=5)
        branch = ''.join(map(str,branch))

        if name is None and cpf is None:
            name = str(input("Name:"))
            cpf = str(input("Cpf:"))

        while len(cpf) != 11 or not cpf.isdigit():
            print("cpf invalid")
            cpf = str(input("Cpf:"))

        cpf_mask = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        branch_mask = f"{branch[:4]}-{branch[4:]}"

        self.account_user.append((name, cpf_mask, branch_mask, self.historic_account) )
        print(self.account_user)


    def withdraw(self, withdraw_value=None):

        try:
            self.historic_transaction_log(self.withdraw)

            if self.limit['transaction'] <= 0 :
                print(f'\n{red}transaction limit exceeded. You can only make up to 10 transactions{white}')
                return

            if withdraw_value is None:
                withdraw_value = float(input("\ninform the withdrawal amount:\nR$:"))

            while withdraw_value < 1:
                print(f"-\n{red}value negative{white}")
                withdraw_value = float(input("\ninform the withdrawal amount:\nR$:"))

            if withdraw_value > self.balance:
                print(f'\n{red}-insufficient balance{white}')
                print(f"💳Balance: R$:{self.balance}")
                return

            if withdraw_value <= self.limit['value_limit'] and self.limit['qtd'] > 0:

                self.limit["qtd"] -= 1
                self.limit['transaction'] -=1
                if self.limit["qtd"] == 3:
                    print(f"\n-its daily value is {green}{self.limit['value_limit']*3}{white} and the withdrawal limit is {green}{self.limit['qtd']}{white} ")

                print(f"\n-withdraw R$:{withdraw_value} loading....")


                if withdraw_value <= self.balance:

                    self.balance -= withdraw_value
                    self.historic_account.append(("WITHDRAW", withdraw_value, get_current_time()))
                    print(f"-withdrawal completed R$:{red}{withdraw_value}{white} remaining R$:{blue}{self.balance}{white}")


                else:

                    print(f"-insufficient balance,your balance R$:{red}{self.balance}.{white}")

            else:
                print(f"-your limit is {green}{self.limit['value_limit']*3}{white} and daily withdrawal limit is {green}{self.limit['qtd']}{white}")


        except ValueError:

            print(f"\n-{red}entry incorrect,please, enter a valid value{white}")

        print("".center(50, ' '))
        time.sleep(0.5)

    def deposit(self, deposit_value=None):

        try:
            self.historic_transaction_log(self.deposit)
            if self.limit['transaction'] <= 0:
                print(f'\n{red}transaction limit exceeded. You can only make up to 10 transactions{white}')
                return
            if deposit_value is None:
                deposit_value =  float(input("\ninform the amount you will deposit: \nR$:"))

            while deposit_value < 1 :
                print(f"\n{red}-value deposit negative{white}")
                deposit_value = float(input("\ninform the amount you will deposit: \nR$:"))

            print(f"\n-deposit  loading....")
            time.sleep(0.5)
            self.balance += deposit_value
            self.historic_account.append(("DEPOSIT", deposit_value, get_current_time()))
            self.limit['transaction'] -= 1

            print(f"-deposit  success of {green}{deposit_value}{white} equal {blue}{self.balance}{white}....")





        except ValueError:

            print(f"\n-{red}entry incorrect,please, enter a valid value{white}")

        print("".center(50, ' '))
        time.sleep(0.5)

    def extract(self):
        self.historic_transaction_log(self.extract)
        print(f"""\n-💳Balance R$:{blue}{self.balance:.2f}{white}\n
here is your transaction history""")

        print("EXTRACT".center(50, '-'))
        if len(self.historic_account) == 0:
            print("-No extract")
        for transaction, value, date in self.historic_account:
            print(f"{transaction:<15} R$ {value:<10}{date:<30}")


        time.sleep(3)
account = Bank(initial_balance=0)

if __name__ == "__main__":
    while True:
        print("option menu".center(50, '-'))
        print("""
        [1] withdraw 💸
        [2] Deposit  💵
        [3] Extract  📄
        [4] Exit     ❌
        [5] TEST     🤖
        [6] create account
        """)
        print("".center(50,'-'))

        try:
            option = int(input("choose your option:\n>>>"))

            if option == 1:
                account.withdraw()
            elif option == 2:
                account.deposit()
            elif option == 3:
                account.extract()
            elif option == 4:
              print(f"\n{red}exit...\033[0m")
              break
            elif option == 5:
                run_test()
            elif option == 6:
                account.create_account()
            else:
                print(f"\n{red}-option invalid{white}")

        except ValueError:
            print(f"\n{red}-entry incorrect,please, enter a valid value{white}")



