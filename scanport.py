import sys
from ipaddress import ip_address
from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR

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