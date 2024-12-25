from datetime import datetime
import time
import random
import pytest


red = "\033[91m"
white = "\033[0m"
green = "\033[92m"
blue = "\033[94m"



#criar class padrao POO

def run_test():
    pytest.main(["-s", "bank_test.py"])


def get_current_time():  # pega a hora
    return datetime.now().strftime("%H:%M-%d/%m/%Y")


def mask_cpf(cpf):  # mascara de cpf
    mask = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return mask


def branch_mask(branch):  # mascara de agencia mudar e colocar conta
    mask = f"{branch[:4]}-{branch[4:]}"
    return mask


class Bank:  #
    def __init__(self):
        self.historic_transactions = []
        self.historic_account = list()
        self.account_default = '0001'
        self.accounts_users = []
        self.user_now = []
        self.limit = {
            "value_limit": 500,
            "qtd": 3,
            "transaction": 10
        }

    def historic_all(self):  # display do historico geral
        for name, cpf, accounts, branch, a, b in self.accounts_users:
            print(f"{name}:{cpf} {branch} {accounts} {a}")

    def return_users(self):  # função de controle se tem usuario on login
        return len(self.user_now) > 0

    def historic_transaction_log(self, func):  # hisotic de login
        self.historic_transactions.append([get_current_time(), func.__name__.upper()])
        print('=' * 50)
        print(f'~[{get_current_time()}] - FUNC: {func.__name__.upper()} - STATUS: OK')
        print('=' * 50)
        return

    def create_account(self, name=None, cpf=None):  # criar conta
        cpf_equal = 0
        list_branch = []
        branch = random.choices(range(0, 10), k=5)
        branch = ''.join(map(str, branch))

        if name is None and cpf is None:
            name = str(input("Name:"))
            cpf = str(input("Cpf:"))

        while len(cpf) != 11 or not cpf.isdigit():
            print("cpf invalid")
            cpf = str(input("Cpf:"))

        cpf_default = mask_cpf(cpf)
        branch_default = branch_mask(branch)

        for name_list, cpf_list, accounts, branch, *rest in self.accounts_users:
            list_branch.append(branch)

            if cpf_list == cpf_default:
                cpf_equal += 1

        while branch_default in list_branch:
            branch = random.choices(range(0, 10), k=5)
            branch = ''.join(map(str, branch))
            branch_default = branch_mask(branch)

        if cpf_equal == 0:
            self.accounts_users.append((name, cpf_default, self.account_default, branch_default, {'Balance': 0}, []))
        else:
            print(f"The CPF {cpf_default} is already registered. Please try registering a different CPF.")

    def login_account(self, cpf=None):  # login

        if len(self.accounts_users) >= 1:
            cpf = str(input("enter your CPF"))
        else:
            print('user not registered')


        if cpf is not None:
            cpf_default = mask_cpf(cpf)
            for account_user in self.accounts_users:

                if account_user[1] == cpf_default:
                    print(f"user: {account_user[0]}")
                    self.user_now = account_user
                    break
                else:
                    print('user not registered')
        else:
            self.user_now = []

    def logoff_account(self,):  # login
            self.user_now = []


    def withdraw(self, withdraw_value=None):  # função de saque

        try:
            self.historic_transaction_log(self.withdraw)

            if self.limit['transaction'] <= 0:
                print(f'\n{red}transaction limit exceeded. You can only make up to 10 transactions{white}')
                return

            if withdraw_value is None:
                withdraw_value = float(input("\ninform the withdrawal amount:\nR$:"))

            while withdraw_value < 1:
                print(f"-\n{red}value negative{white}")
                withdraw_value = float(input("\ninform the withdrawal amount:\nR$:"))

            if withdraw_value <= self.limit['value_limit'] and self.limit['qtd'] > 0:

                self.limit["qtd"] -= 1
                self.limit['transaction'] -= 1

                if self.limit["qtd"] == 3:
                    print(
                        f"\n-its daily value is {green}{self.limit['value_limit'] * 3}{white} and the withdrawal limit is {green}{self.limit['qtd']}{white} ")

                print(f"\n-withdraw R$:{withdraw_value} loading....")

                if withdraw_value <= self.user_now[4]["Balance"]:

                    for user in self.accounts_users:
                        if self.user_now == user:
                            self.user_now[4]["Balance"] -= withdraw_value
                            self.user_now[5].append(("WITHDRAW", withdraw_value, get_current_time()))

                    self.historic_account.append(("WITHDRAW", withdraw_value, get_current_time()))
                    print(
                        f"-withdrawal completed R$:{red}{withdraw_value}{white} remaining R$:{blue}{self.user_now[4]}{white}")

                else:

                    print(f"-insufficient balance,your balance R$:{red}{self.user_now[4]}.{white}")

            else:
                print(
                    f"-your limit is {green}{self.limit['value_limit'] * 3}{white} and daily withdrawal limit is {green}{self.limit['qtd']}{white}")

        except ValueError:

            print(f"\n-{red}entry incorrect,please, enter a valid value{white}")

        print("".center(53, ' '))
        time.sleep(0.5)

    def deposit(self, deposit_value=None):  # função deposit

        try:
            self.historic_transaction_log(self.deposit)
            if self.limit['transaction'] <= 0:
                print(f'\n{red}transaction limit exceeded. You can only make up to 10 transactions{white}')
                return
            if deposit_value is None:
                deposit_value = float(input("\ninform the amount you will deposit: \nR$:"))

            while deposit_value < 1:
                print(f"\n{red}-value deposit negative{white}")
                deposit_value = float(input("\ninform the amount you will deposit: \nR$:"))

            print(f"\n-deposit  loading....")
            time.sleep(0.5)

            for user in self.accounts_users:
                if self.user_now == user:
                    self.user_now[4]["Balance"] += deposit_value
                    self.user_now[5].append(("DEPOSIT", deposit_value, get_current_time()))

            self.limit['transaction'] -= 1

            print(f"-deposit  success of {green}{deposit_value}{white} equal {blue}{self.user_now[4]["Balance"]}{white}....")

        except ValueError:

            print(f"\n-{red}entry incorrect,please, enter a valid value{white}")

        print("".center(53, ' '))
        time.sleep(0.5)

    def extract(self):  # display de extract
        self.historic_transaction_log(self.extract)

        print(f"""\n-💳Balance R$:{blue}{self.user_now[4]["Balance"]:.2f}{white}\n
here is your transaction history""")

        print("EXTRACT".center(53, '-'))
        if len(self.historic_account) == 0:
            print("-No extract") 
        for user in self.accounts_users:
            if self.user_now == user:
                for transaction, value, date in self.user_now[5]:
                    if transaction == "WITHDRAW":
                        value_display = f"{red}{value:.2f}{white}"
                    else:
                        value_display = f"{green}{value:.2f}{white}"
                    print(f"{transaction:<15} R$:{value_display:<25} {date:<30}")

        time.sleep(0.5)

    def __str__(self):
        return f"IO{self.__class__.__name__}"


account = Bank()

if __name__ == "__main__":

    while True:
        user_now = account.return_users()

        print("option menu".center(53, '-'))

        if user_now:
            print('''
[1] withdraw 💸
[2] Deposit  💵
[3] Extract  📄
[4] Exit     ❌''')
        else:
            print("""
[1] Sign Up       📝
[2] Sign In       🔑
[3] Bot Test      🤖
[4] historic all  🤖 """)

        print("".center(53, '-'))
        try:
            option = int(input("choose your option:\n>>>"))

            if user_now:
                if option == 1:
                    account.withdraw()
                elif option == 2:
                    account.deposit()
                elif option == 3:
                    account.extract()
                elif option == 4:
                    account.logoff_account()
                else:
                    print(f"\n{red}-option invalid{white}")
            else:
                if option == 1:
                    account.create_account()

                elif option == 2:
                    account.login_account()
                elif option == 3:
                    run_test()
                elif option == 4:
                    account.historic_all()
                else:
                    print(f"\n{red}-option invalid{white}")
        except ValueError:
            print(f"\n{red}-entry incorrect,please, enter a valid value{white}")
