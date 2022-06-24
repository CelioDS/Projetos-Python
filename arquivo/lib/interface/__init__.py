import time
RE  = "\033[1;31m"
G = "\033[0;32m"
Y = "\033[0;33m"
S  = "\033[5;51m" #sem cor
r  = "\033[5;m" #sem cor


Nome_arquivo = 'arquivo1.txt' #altera o nome do arquivo


def menu(lista):
    print(S + "{::^50}".format(" banco de dados ".upper()) + r)
    c=1
    for item in (lista):
        print(f'{c} = {item}')
        c+=1

def cadastrar_pessoa():
    print(S + "{::^50}".format(" BANCO DE DADOS ".upper()) + r)

    # Criando arquivo de texto no modo 'A' e fechando.

    # Adicionando um texto no arquivo modo 'A'
    print(G + "{::^50}".format(" cadastro ".upper()) + r)
    nome = str(input("-Nome:\t")).strip()
    idade = str(input("-Idade:\t"))
    arquivo = open(Nome_arquivo, 'a+', encoding="utf-8")
    arquivo.write(f'{nome:<20}'+"\t\t\t"+idade+" Anos\n")
    print(Y+"Processando..."+r)
    print(G+"Concluido com sucesso " + arquivo.name + " MODO " + arquivo.mode+r)
    arquivo = open(Nome_arquivo, 'r')

    arquivo.close()
    print()

def Mostra_lista():
        print(S + "{::^50}".format(" banco de dados ".upper()) + r)
        # Lendo o arquivo criado:
        print(f"{'Nome':<31} Idade")
        print("-" * 50)
        with open(Nome_arquivo, 'r', encoding="utf-8") as arquivo:
            print(arquivo.read())
        """for linha in arquivo:
            linha = linha.rstrip()
            print(f"{linha:^10}")"""



def verificar(Nome_arquivo):
    try:
        a = open(Nome_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True









