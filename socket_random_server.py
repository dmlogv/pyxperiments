"""Socket server that push random data"""
import random
import socketserver
import string
import time


BLOCK_SIZE = 4
INTERVAL = 0.1


class RandomDataHandler(socketserver.BaseRequestHandler):
    """Send some random data to socket"""
    def handle(self):
        while True:
            self.request.sendall(self.random_data(BLOCK_SIZE))
            time.sleep(INTERVAL)

    def random_data(self, size):
        """Concatenate some chars and encode to binary"""
        block = [
            random.choice(string.ascii_uppercase)
            for _ in range(size)
            ]
        data = bytes(''.join(block), 'utf-8')
        return data


if __name__ == '__main__':
    host, port = 'localhost', 9999

    with socketserver.TCPServer((host, port), RandomDataHandler) as server:
        server.serve_forever()
