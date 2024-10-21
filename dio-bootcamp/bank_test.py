import pytest
from bank import Bank  # Supondo que você tenha um arquivo bank.py com sua classe Bank

def test():
    account = Bank(initial_balance=1000)
    account.deposit(deposit_value=500)
    assert  account.historic_account[0] == ("DEPOSIT", 500, account.historic_account[0][2])

    account.withdraw(withdraw_value=300)
    assert  account.historic_account[1] == ("WITHDRAW", 300, account.historic_account[1][2])

    assert account.balance == 1200
    account.extract()
    assert len(account.historic_account) == 2



