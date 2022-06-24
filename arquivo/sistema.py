from lib.interface import *

global Nome_arquivo

if verificar(Nome_arquivo):
    print(f"Arquivo existe {Nome_arquivo}  ")
else:
    print('Arquivo nao encontrado')


while True:

    menu(['Cadastrar nova Pessoa','Ver Pessoas Cadastro','Sair',])

    try:
        opcao = int(input('Digite sua opçao\t>>>'))
        print()
    except (ValueError, TypeError, KeyboardInterrupt):
        print(RE + "{::^20}".format(" valor incorreto".upper()) + r)
    else:
        if opcao == 1:
            cadastrar_pessoa()
        elif opcao == 2:
            Mostra_lista()
        elif opcao == 3:
            print(RE+"Saindo...."+r)
            time.sleep(1)
            print(G + "Ate mais...." + r)
            time.sleep(1)
            break
        else:
            print(RE + "{::^20}".format(" valor incorreto".upper()) + r)
        time.sleep(1)


