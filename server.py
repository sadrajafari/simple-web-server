from socket import *
import threading

server_port = 80
server_addr = '127.0.0.1'

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind((server_addr, server_port))
server_socket.listen(1)
print('server is ready...')


class CreatingThreads(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        # print(self.name)
        if self.name == '/':
            http_response_status = 'HTTP/1.0 200 OK\n\n'
            f = open('html_docs/index.html')
            http_response_body = f.read()
            f.close()
            http_response = http_response_status + http_response_body
        elif self.name == '/help':
            http_response_status = 'HTTP/1.0 200 OK\n\n'
            f = open('html_docs/help.html')
            http_response_body = f.read()
            f.close()
            http_response = http_response_status + http_response_body
        else:
            http_response = 'HTTP/1.0 404 NOT FOUND\n\n<h1>Not Found (HTTP 404)<h1>'
        connection_socket.send(http_response.encode())
        connection_socket.close()


while True:
    connection_socket, addr = server_socket.accept()

    request = connection_socket.recv(2048).decode()
    headers = request.split('\n')
    method = headers[0].split(' ')[0]
    subdirectory = headers[0].split(' ')[1]
    print('method = {}, path = {}'.format(method, subdirectory))
    CreatingThreads(f'{subdirectory}').start()




