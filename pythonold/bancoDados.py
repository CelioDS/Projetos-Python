import time

R = "\033[1;31m"
Re = "\033[5;51m" #sem cor
G = "\033[0;32m"
r = "\033[0;m"
cadastro = dict()
bancos = list()
contador = 0


#adiciona produtos
def adicionar():
    global contador
    while True:
        print(Re+"{:^50}".format(f" cadastra produtos {contador} ").upper())
        cadastro["Codigo"] = contador
        cadastro['Produto'] = str(input(r+f"-Nome do produto:{'':<4}->")).strip()
        cadastro["Preço"] = float(input(f"-Valor do produto:{'':<3}->"))
        cadastro["Ano"] = int(input(f"-Ano de fabricação:{'':<2}->"))
        bancos.append(cadastro.copy())
        cadastro.clear()
        contador+=1
        print(r+G + "Processando....." + r)
        time.sleep(0.2)
        print(G + "Produto cadastrado com sucesso".upper() + r)
        print(bancos)
        continuar = str(input("Continuar [N/S]->")).upper().strip()
        while continuar not in "NS":
            continuar = str(input("Continuar [N/S]->")).upper().strip()
        if continuar == 'N':
            break

#consultar produtos
def menu():
    while True:
        print(Re+"{:^50}".format(" Menu ").upper())
        print(r+"1: CADASTRAR PRODUTO ".title())
        print("2: consultar produto ".title())
        print("3: excluir produto ".title())
        print("4: sair ".title())
        opcao = int(input("Digite a opção: "))
        if opcao == 1:
            adicionar()
        elif opcao == 2:
            while True:
                print(Re+"{:^50}".format(" modo de consulta ").upper())
                print(r+"1: Consultar por codigo ".title())
                print("2: consultar por produto ".title())
                print("3: consultar por ano".title())
                print("4: sair ".title())
                consulta = int(input("Digite a opcçao:"))
                print("_" * 50)
                if consulta == 1:
                    op = int(input("Digite o Codigo ".title()))
                    for produtos in bancos:
                        if op == produtos['Codigo']:
                            for k, n in produtos.items():
                                if k == 'Preço':
                                    print(f"{k:<7} = R${n:<10}")
                                else:
                                    print(f"{k:<7} = {n:<10}")
                if consulta ==2:
                    op = str(input("Nome do produto".title()))
                    for produtos in bancos:
                        if op == produtos['Produto']:
                            for k, n in produtos.items():
                                if k == 'Preço':
                                    print(f"{k:<7} = R${n:<10}")
                                else:
                                    print(f"{k:<7} = {n:<10}")
                if consulta ==3:
                    op = int(input("Ano do produto".title()))
                    for produtos in bancos:
                        if op == produtos['Ano']:
                            for k, n in produtos.items():
                                if k == 'Preço':
                                    print(f"{k:<7} = R${n:<10}")
                                else:
                                    print(f"{k:<7} = {n:<10}")
                if consulta ==4:
                    break
        # excluir produtos
        elif opcao == 3:
            while True:
                print(Re+"{:^50}".format(" modo de exclusao ").upper())
                print(r+"1: Excluir por codigo ".title())
                print("2: Excluir por produto ".title())
                print("3: Excluir por ano".title())
                print("4: sair ".title())
                consulta = int(input("Digite a opcçao:"))
                if consulta == 1:
                    op = int(input("Digite o Codigo ".title()))
                    for produtos in bancos:
                        if op == produtos['Codigo']:
                            for k, n in produtos.items():
                                if k == 'Preço':
                                    print(G+"Processando....."+r)
                                    time.sleep(1)
                                    print(R+"Produto excluido com sucesso"+r)
                                    bancos.remove(produtos)
                elif consulta == 2:
                    op = str(input("Nome do produto".title()))
                    for produtos in bancos:
                        if op == produtos['Produto']:
                            for k, n in produtos.items():
                                if k == 'Preço':
                                    print(G + "Processando....." + r)
                                    time.sleep(1)
                                    print(R + "Produto excluido com sucesso" + r)
                                    bancos.remove(produtos)
                elif consulta == 3:
                    op = int(input("Ano do produto".title()))
                    for produtos in bancos:
                        if op == produtos['Ano']:
                            for k, n in produtos.items():
                                print(G + "Processando....." + r)
                                time.sleep(1)
                                print(R + "Produto excluido com sucesso" + r)
                                bancos.remove(produtos)
                elif consulta == 4:
                    break
                else:
                    print(R+"Produto nao encontrado!!! Verificar produtos"+r)

        else:
            break
        print(bancos)
while True:

    if contador == 0:
        adicionar()
    menu()





