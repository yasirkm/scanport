import sys
from ipaddress import ip_address
from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR

UPPER_PORT = 65536
LOWER_PORT = 0

def port_isopen(ip, port):
    '''
        returns True if port on ip is open
    '''
    with socket(AF_INET, SOCK_STREAM) as s:
        try:
            s.connect((ip, port))
            s.shutdown(SHUT_RDWR)
            s.close()
            return True

        except ConnectionRefusedError:
            return False


def openports(ip):
    '''
        returns a list of open ports of an ip address
    '''
    ports = []

    for port in range(LOWER_PORT, UPPER_PORT+1):
        if port_isopen(ip, port):
            ports.append(port)
    
    return ports