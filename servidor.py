import socket

# Configuración
HOST = '127.0.0.1'  # localhost
PUERTO = 5000

# Crear socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PUERTO))
servidor.listen()

print(f"Servidor escuchando en {HOST}:{PUERTO}")

while True:
    conexion, direccion = servidor.accept()
    print(f"Conexión establecida con {direccion}")

    while True:
        mensaje = conexion.recv(1024).decode()

        if not mensaje:
            break  # El cliente cerró la conexión

        print(f"Cliente dijo: {mensaje}")

        if mensaje == "DESCONEXION":
            print("Servidor cierra la conexión con el cliente.")
            conexion.close()
            break  # Espera un nuevo cliente

        if mensaje.lower() == "hola servidor":
            respuesta = "HOLA CLIENTE"
        else:
            respuesta = mensaje.upper()
        conexion.sendall(respuesta.encode())
