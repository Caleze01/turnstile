import serial
import time
import pyodbc

# Configura a porta serial (substitua 'COM3' pela porta correta)
ser = serial.Serial('COM3', 9600, timeout=1)

# Configura a conexão com o banco de dados MS SQL
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-SUHMG7B;'
    'DATABASE=PythonSQL;'
)
print("Conexão estabelecida com sucesso!")

cursor = conn.cursor()

def registrar_evento(evento, usuario):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO eventos_catraca (id_evento, UsuarioID, timestamp) VALUES (?, ?, ?)", (evento, usuario, timestamp))
    conn.commit() 

def abrir_catraca(usuario):
    ser.write(b'ABRIR')  # Envia comando para abrir a catraca
    time.sleep(1)  # Aguarda um segundo
    resposta = ser.readline().decode('utf-8').strip()
    registrar_evento('ABRIR', usuario)
    return resposta

def fechar_catraca(usuario):
    ser.write(b'FECHAR')  # Envia comando para fechar a catraca
    time.sleep(1)  # Aguarda um segundo
    resposta = ser.readline().decode('utf-8').strip()
    registrar_evento('FECHAR', usuario)
    return resposta

def verificar_usuario(usuario):
    cursor.execute("SELECT COUNT(*) FROM Usuarios WHERE Nome = ?", (usuario,))
    result = cursor.fetchone()
    return result[0] > 0

 #Solicita o nome do usuário
usuario = input("Digite seu nome de usuário: ")

if verificar_usuario(usuario):
    print("Usuário verificado. Abrindo catraca...")
    resposta = abrir_catraca(usuario)
    print(f"Resposta da catraca: {resposta}")

    print("Fechando catraca...")
    resposta = fechar_catraca(usuario)
    print(f"Resposta da catraca: {resposta}")
else:
    print("Usuário não encontrado. Acesso negado.")

 # Fecha a conexão serial e a conexão com o banco de dados
ser.close()
conn.close()