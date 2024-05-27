import socket


def process_line(line):
    numbers = list(map(int, line.split()))
    return max(numbers), min(numbers)


def start_server(host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f'Server started and listening on {host}:{port}')

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f'Connected by {addr}')
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    line = data.decode('utf-8').strip()
                    max_num, min_num = process_line(line)
                    response = f'Max: {max_num}, Min: {min_num}'
                    conn.sendall(response.encode('utf-8'))


if __name__ == '__main__':
    start_server()
