import socket

SERVER_IP = 'localhost'
SERVER_PORT = 9800
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverAddress = (SERVER_IP, SERVER_PORT)
print('Conectando a {} en el puerto {}'.format(*serverAddress))
sock.connect(serverAddress)

try:
    message = b'Este es un mensaje.'
    print('\n\nEnviando el siguiente texto: {!s}'.format(message))
    sock.sendall(message)

    print('\n\n')

    bytesRecibidos = 0
    bytesEsperados = len(message)

    while bytesRecibidos < bytesEsperados:
        data = sock.recv(BUFFER_SIZE)
        bytesRecibidos += len(data)
        print('Recibiendo: {!s}'.format(data))

finally:
    print('\n\nConexion finalizada con el servidor')
    socket.close()

"""
full_msg = ''

while True:
    msg = s.recv(1024)
    if len(msg) <= 0:
        break
    full_msg += msg.decode('utf-8')
print(full_msg)
"""