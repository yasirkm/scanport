import sys
from ipaddress import ip_address
from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR

UPPER_PORT = 90
LOWER_PORT = 70

def main():
    if len(sys.argv) < 2:
        print("Use: python scanport.py {ip address}")
        sys.exit()
    
    ip = sys.argv[1]

    try:
        ip_address(ip)
    except ValueError:
        print("invalid IP address. Example of valid IP: 192.168.0.1 and 2001:db8::1")
        sys.exit()

    for port in openports(ip):
        print(port)


def port_isopen(ip, port):
    '''
        returns True if port on ip is open
    '''
    with socket(AF_INET, SOCK_STREAM) as s:
        try:
            s.connect((ip, port))
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

if __name__ == "__main__":
    main()