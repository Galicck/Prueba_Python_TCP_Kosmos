import socket

# Configuración
HOST = '127.0.0.1'
PUERTO = 5000

# Crear socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PUERTO))

print(f"Conectado al servidor en {HOST}:{PUERTO}")

while True:
    mensaje = input("Escribe un mensaje ('DESCONEXION' para salir): ")

    cliente.sendall(mensaje.encode())

    if mensaje == "DESCONEXION":
        print("Desconectando del servidor...")
        break

    respuesta = cliente.recv(1024).decode()
    print(f"Respuesta del servidor: {respuesta}")

cliente.close()
