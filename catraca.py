import serial
import time
from verifica import verificar_usuario, fechar_conexao, cursor, conn  # Importa a função verificar_usuario e fechar_conexao

# Configura a porta serial (substitua 'COM3' pela porta correta)
ser = serial.Serial('COM3', 9600, timeout=1)

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

# Solicita o nome do usuário
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
fechar_conexao()