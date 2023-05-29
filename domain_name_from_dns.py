import socket


def get_domain(ip):
    hostname = socket.gethostbyaddr(ip)[0]
    print(hostname)


get_domain("8.8.8.8")
