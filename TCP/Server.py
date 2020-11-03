import socket

IP_ADDR = socket.gethostname()
IP_PORT = 9800
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverAddress = (IP_ADDR, IP_PORT)
print('\nInciando servidor en {}, puerto {}'.format(*serverAddress))
sock.bind(serverAddress)
sock.listen(1)

while True:
    print('\nEsperando conexion remota')
    connection, clientAddress = sock.accept()

    try:
        print('\nConexion establecida desde', clientAddress)
        while True:
            data = connection.recv(BUFFER_SIZE)
            print('\nRecibido: {!r}'.format(data))

            if str(data.decode()) == str('print suma'):
                print('\nSe ha hecho una suma')

            """if data:
                print('\nEnviando data devuelta al cliente')
                connection.sendall(data)
            else:
                print('\nTransmision finalizada desde el cliente ', clientAddress)
                break"""

    except KeyboardInterrupt:
        sock.close()
        break

    finally:
        connection.close()