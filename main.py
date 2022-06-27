import socket
import threading

HOST = '127.0.0.1'
PORT = int(input("Enter the port that you want to comminucate on(ex: 4444) : "))
NAME = input("Enter the name by which you want to comminucate : ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))


def talk(message, sock):
    sock.send((NAME+": "+message).encode())
    # to separate every message with a new line
    sock.send("\n".encode())


def recieve(sock):
    response = sock.recv(4096)
    print(response.decode())


while True:
    message = input()
    thread1 = threading.Thread(target=talk, args=(message, sock,))
    thread2 = threading.Thread(target=recieve, args=(sock,))
    thread1.start()
    thread2.start()

sock.close()
