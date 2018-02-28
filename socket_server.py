"""Simplest socket server

Use `telnet` to get results
"""

import socket


RESPONSE = 'Philippov rules!\n'
N_OF_CONNECTIONS = 10


def serve(host, port):
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(N_OF_CONNECTIONS)

    while True:
        conn, _ = sock.accept()
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.send(bytes(RESPONSE, 'utf-8'))
        finally:
            conn.close()


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8734 

    print(f'Starting at {host}:{port}')
    serve(host, port)
