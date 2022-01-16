import socket

sock = socket.socket()  #создание сокета
sock.connect(('localhost', 9090))  #Выберем любой порт от 0 до 65535. Порты от 0 до 1023 требуют определенных привилегий

msg = 'Hello Daniel'  #Вводим сообщение
sock.send(msg.encode())  #Посылаем на сервер

sock.close()  #Закрываем соединение
