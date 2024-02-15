import socket
import json
from datetime import datetime

address = "localhost"
port = 8008
s = None


while True:
    name = input('Ваше имя: ')
    user_input = input('Введите сообщение: ')
    print('-'*20)

    data = {
        'action': 'msg',
        'time': str(datetime.now()),
        'to': 'server',
        'from': name,
        'encoding': 'utf-8',
        'message': user_input
    }

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address, port))

    s.send(json.dumps(data).encode('utf-8'))

    # прием
    data = b''
    while True:
        a = s.recv(4)
        print(a)
        data += a
        if not a:
            break
    print(json.loads(data))
    s.close()
