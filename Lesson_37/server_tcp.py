import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 8888)
sock.bind(server_address)
sock.listen(10)

print("The server is listening on 127.0.0.1:8888 ...")


while True:
    # Синхронная обработка.
    conn, addr = sock.accept()  # Блокировка до тех пор, пока нет клиента.
    print('Connected by', addr)

    while True:
        print("Receiving message...")
        data = conn.recv(4)
        text_data = data.decode('utf-8')
        print("Received data:", text_data)

        # ...... Логика приложения.

        if not data:
            conn.send('Bye'.encode('utf-8'))
            conn.close()
            break

        conn.sendall(b'GOT')
