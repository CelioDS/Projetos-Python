from datetime import datetime
import random
import pytest
import tkinter as tk
from tkinter import messagebox

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
    def __init__(self, root):
        self.user_now = []
        self.account_default = '0001'
        self.historic_account = list()
        self.historic_transactions = []
        self.limit = {
            "value_limit": 500,
            "qtd": 3,
            "transaction": 10
        }
        self.accounts_users = [('Celio',
                                '518.156.328-12',
                                '0001',
                                '1236-5',
                                {"Balance": 1000},
                                [('WITHDRAW', 1000, '17:41-24/12/2024'),('DEPOSIT', 2000, '17:41-24/12/2024')],
                                [('~[19:02-24/12/2024] - FUNC: DEPOSIT_UI - STATUS: OK'),('~[19:02-24/12/2024] - FUNC: WITHDRAW_UI - STATUS: OK')])]
        self.root = root
        self.root.title("Bank APP")
        self.root.geometry("700x600+750+250")
        self.build_main_menu()

    def build_main_menu(self):
        self.clear_frame()

        tk.Label(self.root, text="Bank APP", font=("Arial", 20)).pack(pady=10)

        if self.user_now:
            info_frame = tk.Frame(self.root)
            info_frame.pack(pady=10)

            tk.Label(info_frame, text=f"{self.user_now[0].capitalize()}").grid(row=0, column=0, padx=10, pady=5)
            tk.Label(info_frame, text=f"R$: {self.user_now[4]["Balance"]}").grid(row=0, column=1, padx=10, pady=5)
            tk.Label(info_frame, text=f"Agency: {self.user_now[2]}").grid(row=0, column=2, padx=10, pady=5)
            tk.Label(info_frame, text=f"Account: {self.user_now[3]}").grid(row=0, column=3, padx=10, pady=5)

            tk.Button(self.root, text="Deposit", command=self.deposit_ui, width=20).pack(pady=5)
            tk.Button(self.root, text="Withdraw", command=self.withdraw_ui, width=20).pack(pady=5)
            tk.Button(self.root, text="Extract", command=self.extract_ui, width=20).pack(pady=5)
            tk.Button(self.root, text="Log off", command=self.logoff_account, width=20).pack(pady=5)

        else:
            info_frame = tk.Frame(self.root)
            info_frame.pack(pady=10)



            tk.Button(info_frame, text="Sign Up", command=self.signup_ui, width=20).grid(row=1, column=0, padx=10, pady=5)
            tk.Button(info_frame, text="Sign in", command=self.signin_ui, width=20).grid(row=2, column=0, padx=10, pady=5)

            tk.Label(info_frame, text=f"USER: {len(self.accounts_users)}").grid(row=3, column=0, padx=10, pady=5)
            for users in self.accounts_users:
                tk.Label(info_frame, text=f"{users[0]} : {users[1]}").grid()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def historic_all(self):  # display do historico geral
        for name, cpf, accounts, branch, a, b in self.accounts_users:
            print(f"{name}:{cpf} {branch} {accounts} {a}")

    def return_users(self):  # função de controle se tem usuario on login
        return len(self.user_now) > 0

    def historic_transaction_log(self, func):  # hisotic de login
        self.historic_transactions.append([get_current_time(), func.__name__.upper()])
        self.user_now[6].append(f"~[{get_current_time()}] - FUNC: {func.__name__.upper()} - STATUS: OK")
        return  f'~[{get_current_time()}] - FUNC: {func.__name__.upper()} - STATUS: OK'

    def signup_ui(self):  # criar conta
        self.clear_frame()

        tk.Label(self.root, text="Sign Up", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Name:").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()

        tk.Label(self.root, text="CPF (11 digits):").pack()
        cpf_entry = tk.Entry(self.root)
        cpf_entry.pack()

        def register():
            list_branch = []
            name = name_entry.get().capitalize()
            cpf = cpf_entry.get().replace("-","").replace(".","")

            if len(cpf) != 11 or not cpf.isdigit():
                messagebox.showerror("Error", "CPF must be 11 digits number")
                return
            if len(name) < 3 or name.isdigit():
                messagebox.showerror("Error", "Name invalid")
                return

            branch = "".join(map(str, random.choices(range(0,10), k=5)))
            branch_masked = branch_mask(branch)
            cpf_masked = mask_cpf(cpf)

            for name_list, cpf_list, accounts, branch, *rest in self.accounts_users:
                list_branch.append(branch)

            while branch_masked in list_branch:
                branch = random.choices(range(0, 10), k=5)
                branch = ''.join(map(str, branch))
                branch_masked = branch_mask(branch)

            if any(user[1] == cpf_masked for user in self.accounts_users):
                messagebox.showerror("ERROR", "CPF already registered")
                return

            self.accounts_users.append((name, cpf_masked, '0001', branch_masked, {"Balance": 0}, [],[]))
            messagebox.showinfo("Success","Account created successfully")
            self.build_main_menu()

        tk.Button(self.root, text="Register", command=register, width=20).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.build_main_menu, width=20).pack()

    def signin_ui(self ):  # login
        self.clear_frame()

        tk.Label(self.root, text="Sign In", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="CPF:").pack()
        cpf_entry = tk.Entry(self.root)
        cpf_entry.pack()

        def login():
            cpf = cpf_entry.get().replace("-","").replace(".","")
            cpf_masked = mask_cpf(cpf)

            if len(self.accounts_users) < 1:
                messagebox.showerror("Error", "No registered")

            for user in self.accounts_users:
                if user[1] == cpf_masked:
                    self.user_now = user
                    messagebox.showinfo("Success", f"Welcome, {user[0].capitalize()}!")
                    self.build_main_menu()
                    return

            messagebox.showerror("Error", "User not found")


        tk.Button(self.root, text="Login", command=login, width=20).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.build_main_menu, width=20).pack()

    def logoff_account(self,):  # login
            self.user_now = []
            messagebox.showinfo("Log Out", "Logged out sucessfully")
            self.build_main_menu()

    def withdraw_ui(self):  # função de saque
        self.clear_frame()

        tk.Label(self.root, text="Widthdraw", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Amount").pack()
        amount_entry = tk.Entry(self.root)
        amount_entry.pack()

        def withdraw():
            try:
                amount = float(amount_entry.get())

                if amount <= 0:
                    raise ValueError("Invalid amount.")

                if amount > self.limit["value_limit"] or self.limit["qtd"] <= 0:
                    messagebox.showerror("Error", "Widhdrawal limit exceeded")
                    return

                if self.limit['transaction']  <= 0:
                    messagebox.showerror("Error", "Transaction limit exceeded")
                    return

                if amount > self.user_now[4]["Balance"]:
                    messagebox.showerror("Error", "Insufficient balance")
                    return

                self.user_now[4]["Balance"] -= amount
                self.user_now[5].append(("WITHDRAW", amount, get_current_time()))
                self.historic_account.append(("WITHDRAW", amount, get_current_time()))

                self.limit["qtd"] -= 1
                self.limit['transaction'] -= 1

                text_log = self.historic_transaction_log(self.withdraw_ui)
                tk.Label(self.root, text=text_log, font=("Courier", 10), anchor="w").pack(pady=10)
                messagebox.showinfo("Success", f"width: R$ {amount:.2f}")
                self.build_main_menu()
            except ValueError:
                messagebox.showinfo("Error", "Invalid input")



        tk.Button(self.root, text="Widthdraw", command=withdraw, width=20).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.build_main_menu, width=20).pack()

    def deposit_ui(self):  # função deposit
        self.clear_frame()

        tk.Label(self.root, text="Deposit", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Amount:").pack()
        amount_entry = tk.Entry(self.root)
        amount_entry.pack()

        def deposit():
            try:

                amount = float(amount_entry.get())

                if amount <= 0:
                    raise ValueError("Invalid amount")

                if self.limit['transaction']  <= 0:
                    messagebox.showerror("Error", "Transaction limit exceeded")
                    return

                self.user_now[4]["Balance"] += amount
                self.user_now[5].append(("DEPOSIT", amount, get_current_time()))
                self.limit['transaction'] -= 1

                text_log = self.historic_transaction_log(self.deposit_ui)
                tk.Label(self.root, text=text_log, font=("Courier", 10), anchor="w").pack(pady=10)

                messagebox.showinfo("Success", f"Deposited: R$ {amount:.2f}")
                self.build_main_menu()

            except ValueError:
                messagebox.showerror("Error", "Invalid input")



        tk.Button(self.root, text="Deposit", command=deposit, width=20).pack(pady=10)
        tk.Button(self.root, text='Back', command=self.build_main_menu, width=20).pack()

    def extract_ui(self ):  # display de extract
        self.clear_frame()

        tk.Label(self.root, text="Extract", font=("Arial", 16)).pack(pady=10)

        transactions = self.user_now[5]
        transactions_historic = self.user_now[6]

        if not transactions:
          tk.Label(self.root, text="No transactions").pack()
        else:
            info_frame = tk.Frame(self.root)
            info_frame.pack(pady=10)

            tk.Label(info_frame, text=f"{self.user_now[0].capitalize()}").grid(row=0, column=0, padx=10, pady=5)
            tk.Label(info_frame, text=f"R$: {self.user_now[4]["Balance"]}").grid(row=0, column=1, padx=10, pady=5)

            header = f"{'Transaction':<15}         {'Amount (R$)':<35}         {'Date':>15}"
            tk.Label(self.root, text=header, font=("Courier", 10, "bold"), anchor="center").pack()

            for transaction, amount, date in transactions:
                color = "red" if transaction == "WITHDRAW" else "green"

                row_text = f"{transaction:<15}         R$: {amount:<31}         {date:>15}"
                tk.Label(self.root, text=row_text, font=("Courier", 10), fg=color, anchor="center").pack()



        tk.Button(self.root, text="Back", command=self.build_main_menu, width=20).pack(pady=10)

        self.historic_transaction_log(self.extract_ui)
        tk.Label(self.root, text="LOG", font=("Courier", 10, "bold"), anchor="center").pack()
        if not transactions:
            tk.Label(self.root, text="No transactions historic").pack()
        else:
            for transaction_hit in transactions_historic:
                color = "grey"
                tk.Label(self.root, text=f"{transaction_hit:<15}", font=("Courier", 10), fg=color, anchor="center").pack()

    def __str__(self):
        return f"IO{self.__class__.__name__}"


root = tk.Tk()
account = Bank(root)
root.mainloop()


