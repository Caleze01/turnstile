import pyodbc

# Conecta Banco de dados 
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-SUHMG7B;'
    'DATABASE=PythonSQL;'
)
print("Conexão estabelecida com sucesso!")

cursor = conn.cursor()

# Função para verificar nome do usuário
def verificar_usuario(usuario):
    cursor.execute("SELECT COUNT(*) FROM Usuarios WHERE Nome = ?", (usuario,))
    result = cursor.fetchone()
    return result[0] > 0

# Fecha a conexão com o banco de dados
def fechar_conexao():
    conn.close()

usuario = input("Digite seu nome de usuário: ")

if verificar_usuario(usuario):
    print("Usuário verificado. Abrindo catraca...")
    

    print("Fechando catraca...")
    
    print("Usuário não encontrado. Acesso negado.")
else:
    print("Usuário não encontrado. Acesso negado.")
