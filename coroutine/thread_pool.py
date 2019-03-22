from queue import Queue
from threading import Thread
from socket import AF_INET, SOCK_STREAM, socket
from concurrent.futures import ThreadPoolExecutor


def echo_client(sock, client_addr):
    print("Got connection from", client_addr)

    while True:
        msg = socket.recv(65536)
        if not msg:
            break

        socket.sendall(msg)
    print('Client closed connection')
    socket.close()


def echo_server(addr):
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)


def echo_client_user_queue(q):
    sock, client_addr = q.get()
    echo_client(sock, client_addr)


def echo_server_use_queue(addr, nworkers):
    """手动实现进程池"""
    q = Queue()
    for n in range(nworkers):
        t = Thread(target=echo_client_user_queue, args=(q, ))
        t.daemon = True

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        q.put(client_sock, client_addr)


def tcp_client(addr):
    client_sock = socket(AF_INET, SOCK_STREAM)
    client_sock.connect(addr)
    while True:
        data = input('>')
        if not data:
            break
        client_sock.send(data.encode())
        data = client_sock.recv(1024)
        if not data:
            break
        print(data)


def fetch_url(url):
    import requests
    res = requests.get(url)
    return res.content


if __name__ == '__main__':
    addr = ('', 8899)

    # echo_server(('', 8899))
    echo_server_use_queue(addr, 20000)
