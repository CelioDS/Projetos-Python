import tkinter as tk
import pandas as pd
import sqlite3
# ctrl + / comenta tudo que estiver selecionado ctrl * / tira #

#criar banco e tabela
# conexao = sqlite3.connect('Banco_Cliente.db')
# c = conexao.cursor()
# c.execute('''CREATE TABLE clientes(
#             Nome text,
#             Sobrenome text,
#             Email text,
#             Telefone text
#             )
# ''')
# conexao.commit()
# conexao.close()

def cadastrar_cliente():
    conexao = sqlite3.connect('Banco_Cliente.db')
    c = conexao.cursor()
    c.execute('INSERT INTO clientes VALUES (:nome, :sobrenome, :email, :telefone)',#variavel teporaria com :
              {
               'nome':entry_nome.get(),
               'sobrenome':entry_sobrenome.get(),
               'email':entry_email.get(),
               'telefone':entry_telefone.get()
              }
              )
    conexao.commit()
    conexao.close()
    entry_nome.delete(0,'end') #limpa interfece
    entry_sobrenome.delete(0, 'end')  # limpa interfece
    entry_telefone.delete(0, 'end')  # limpa interfece
    entry_email.delete(0, 'end')  # limpa interfece

def exporta_clientes():
    conexao = sqlite3.connect('Banco_Cliente.db')
    c = conexao.cursor()
    c.execute("SELECT *, oid FROM clientes") #seleciona tudo na banco junto com ID
    clientes_cadastrados = c.fetchall()  #pega todos os dados e coloca na variavel
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['nome', 'sobrenome', 'telefone', 'email','id_banco'])
    clientes_cadastrados.to_excel('Banco_Clientes.xlsx')
    conexao.commit() #confirma
    conexao.close()


janela = tk.Tk()
janela.title("Ferramenta de cadastro de cliente")
janela.geometry("320x400+0+500") #primeiro tamanho largura e altura, depois posicao onde aparece

#labels
label_nome = tk.Label(janela, text='nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='email')
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)

#entrys

entry_nome = tk.Entry(janela, text='nome')
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, text='sobrenome')
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, text='email')
entry_email.grid(row=2, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, text='telefone')
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

# botaoes
botao_cadastrar = tk.Button(janela, text='Cadastrar Cliente', command = cadastrar_cliente)
botao_cadastrar.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

botao_exportar = tk.Button(janela, text='exportar base de clientes', command = exporta_clientes)
botao_exportar.grid(row=5, column=0, padx=10, pady=10,  columnspan=2, ipadx=80)



janela.mainloop()
