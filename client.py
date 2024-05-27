import socket

def send_line_to_server(line, host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(line.encode('utf-8'))
        response = client_socket.recv(1024)
        return response.decode('utf-8')

if __name__ == '__main__':
    host = 'localhost'
    port = 12345
    while True:
        line = input('Enter a sequence of integers (or "exit" to quit): ')
        if line.lower() == 'exit':
            break
        response = send_line_to_server(line, host, port)
        print(f'Server response: {response}')
