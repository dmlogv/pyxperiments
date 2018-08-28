"""Socket client to receive message from the `socket_random_server.py`"""
import socket
import time


class SocketClient:
    def __init__(self, host, port):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._sock.connect((host, port))

    def __del__(self):
        self._sock.close()

    def receive_forever(self):
        """Receive data from server"""
        
        # Send empty data to initiate receiving
        self._sock.sendall(bytes('', 'utf-8'))

        while True:
            received = str(self._sock.recv(256), 'utf-8')

            if not received:
                exit(0)

            yield received


if __name__ == '__main__':
    host, port = 'localhost', 9999
    print(f'Connect to {host}:{port}...')

    for data in SocketClient(host, port).receive_forever():
        print(data)
        time.sleep(0.1)
