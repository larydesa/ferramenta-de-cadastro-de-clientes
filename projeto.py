import tkinter as tk
import sqlite3
import pandas as pd

conexao = sqlite3.connect("banco_clientes.db")
c = conexao.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS clientes (
                nome text, 
                sobrenome text, 
                email text, 
                telefone text
            )""")

conexao.commit()
conexao.close()

def cadastrar_clientes():
    conexao = sqlite3.connect("banco_clientes.db")
    c = conexao.cursor()
    c.execute("INSERT INTO clientes VALUES (:nome, :sobrenome, :email, :telefone)",
        {
            'nome': entry_nome.get(),
            'sobrenome': entry_sobrenome.get(),
            'email': entry_email.get(),
            'telefone': entry_telefone.get()
        }
    )

    entry_nome.delete(0, 'end')
    entry_sobrenome.delete(0, 'end')
    entry_email.delete(0, 'end')
    entry_telefone.delete(0, 'end')

    conexao.commit()
    conexao.close()

def exporta_clientes():
    conexao = sqlite3.connect("banco_clientes.db")
    c = conexao.cursor()
    c.execute("SELECT *, oid FROM clientes")
    clientes_dataframe = c.fetchall()
    clientes_dataframe = pd.DataFrame(clientes_dataframe, columns=['nome', 'sobrenome', 'email', 'telefone', 'id_banco'])
    clientes_dataframe.to_excel('clientes.xlsx', index=False)

    print("Dados exportados com sucesso para clientes.xlsx!")
    print(clientes_dataframe)

    conexao.commit()
    conexao.close()

jshell = tk.Tk()
jshell.title("Ferramenta de cadastro de cliente")

label_nome = tk.Label(jshell, text = "Nome", width = 30)
label_nome.grid(row = 0, column = 0, padx = 50, pady = 50)

label_sobrenome = tk.Label(jshell, text = "Sobrenome", width = 30)
label_sobrenome.grid(row = 1, column = 0, padx = 50, pady = 50)

label_email = tk.Label(jshell, text = "Email", width = 30)
label_email.grid(row = 2, column = 0, padx = 50, pady = 50)

label_telefone = tk.Label(jshell, text = "Telefone", width = 30)
label_telefone.grid(row = 3, column = 0, padx = 50, pady = 50)

entry_nome = tk.Entry(jshell, width = 30)
entry_nome.grid(row = 0, column = 1, padx = 50, pady = 50)

entry_sobrenome = tk.Entry(jshell, width = 30)
entry_sobrenome.grid(row = 1, column = 1, padx = 50, pady = 50)

entry_email = tk.Entry(jshell, width = 30)
entry_email.grid(row = 2, column = 1, padx = 50, pady = 50)

entry_telefone = tk.Entry(jshell, width = 30)
entry_telefone.grid(row = 3, column = 1, padx = 50, pady = 50)

botao_cadastrar = tk.Button(jshell, text = "Cadastrar", command = cadastrar_clientes)
botao_cadastrar.grid(row = 4, column = 0, padx = 50, pady = 50, columnspan = 2, ipadx = 80)

botao_exportar = tk.Button(jshell, text = "Exportar Base de Dados", command = exporta_clientes)
botao_exportar.grid(row = 5, column = 0, padx = 50, pady = 50, columnspan = 2, ipadx = 80)

jshell.mainloop()