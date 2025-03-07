import pyodbc

dados_conexao = (
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-SUHMG7B;'
    'DATABASE=PythonSQL;'
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão estabelecida com sucesso!")

cursor = conexao.cursor()

# Solicita os dados do usuário
nome = input("Digite o nome: ")
idade = input("Digite a idade: ")
genero = input("Digite o gênero: ")
telefone = input("Digite o telefone: ")
email = input("Digite o email: ")
plano = input("Digite o plano: ")

New_user = """INSERT INTO Usuarios (Nome, Idade, Genero, Telefone, Email, Plano)
VALUES(?, ?, ?, ?, ?, ?)"""

cursor.execute(New_user, nome, idade, genero, telefone, email, plano)
conexao.commit()

print("Usuário cadastrado com sucesso!")

conexao.close()