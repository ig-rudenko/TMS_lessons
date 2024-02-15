import datetime
import socket
import time

import select

print('Для выключения сервера нажмите Ctrl+C.')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8008))
sock.listen(5)
sock.setblocking(False)  # НЕ блокирующий сокет!

inputs = [sock]  # сокеты, которые будем читать
outputs = []  # сокеты, в которые надо писать

messages = {}  # здесь будем хранить сообщения для сокетов

print('\nОжидание подключения localhost:8008...')
while True:
    # вызов `select.select` который проверяет сокеты в
    # списках: `inputs`, `outputs` и по готовности, хотя бы
    # одного - возвращает списки: `reads`, `send`, `excepts`
    readable, writable, exceptional = select.select(inputs, outputs, inputs, 0.1)

    if not readable and not writable and not exceptional:
        print(f"{datetime.datetime.now().time()} Обработка другой задачи")
        time.sleep(1)

    # Далее проверяются эти списки, и принимаются
    # решения в зависимости от назначения списка

    # список READS - сокеты, готовые к чтению
    for conn in readable:
        if conn == sock:
            # если это серверный сокет, то пришел новый клиент, принимаем подключение
            new_conn, client_addr = conn.accept()
            print('Успешное подключение!')

            new_conn.setblocking(False)  # устанавливаем неблокирующий сокет
            inputs.append(new_conn)      # поместим новый сокет в очередь на прослушивание
            outputs.append(new_conn)     # на запись

            messages[new_conn] = []  # инициализируем список сообщений

        else:
            # если это НЕ серверный сокет, то клиент хочет что-то сказать
            data = conn.recv(1)
            if data:
                print(conn, data)
                # если сокет прочитался и есть сообщение
                # то кладем сообщение в словарь, где
                # ключом будет сокет клиента
                messages[conn].append(data)

    # список SEND - сокеты, готовые принять сообщение
    for conn in writable:

        if conn in readable:
            # Пропускаем сокеты, которые еще читаются или нет данных для записи
            continue

        # выбираем из словаря сообщения для данного сокета
        msg = messages.get(conn, [])
        if len(msg):
            # если есть сообщения - то переводим
            # его в верхний регистр и отсылаем
            temp = msg.pop(0).decode('utf-8').upper()

            conn.send(temp.encode())
        else:
            # если нет сообщений - удаляем из очереди
            # сокетов, готовых принять сообщение
            inputs.remove(conn)
            outputs.remove(conn)
            conn.close()

    # список EXCEPTS - сокеты, в которых произошла ошибка
    for conn in exceptional:
        print('Клиент отвалился...')
        # удаляем сокет с ошибкой из всех очередей
        inputs.remove(conn)
        if conn in outputs:
            outputs.remove(conn)
        # закрываем сокет как положено, тем
        # самым очищаем используемые ресурсы
        conn.close()
        # удаляем сообщения для данного сокета
        del messages[conn]
