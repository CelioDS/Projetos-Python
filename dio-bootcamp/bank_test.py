import pytest
from bank import Bank  # Supondo que o arquivo com a classe Bank seja bank.py
from unittest.mock import patch


def test_bank_operations():
    # Criando uma instância da classe Bank
    account = Bank()

    # Simulando a criação de uma conta
    with patch("builtins.input", side_effect=["celio", "50816832803"]):
        account.create_account("celio", '50816832803')



    # Simulando o login na conta criada
    with patch("builtins.input", return_value="50816832803"):
        account.login_account('50816832803')

    assert account.user_now[1] == '508.168.328-03', "Login falhou"

    # Simulando um depósito de 1500
    with patch("builtins.input", return_value="1500"):
        account.deposit(deposit_value=1500)

    assert account.user_now[4]["Balance"] == 1500, "Saldo incorreto após depósito"

    # Simulando um saque de 750
    with patch("builtins.input", return_value="750"):
        account.withdraw(withdraw_value=750)





    # Simulando o logoff da conta
    account.logoff_account()
    assert account.user_now == [], "Usuário deveria ter deslogado"


if __name__ == "__main__":
    pytest.main()
