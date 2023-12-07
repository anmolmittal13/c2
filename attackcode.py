import ipaddress
import socket
import sys

BASE_PORT = 3040
WEEK4_IP = '10.0.2.5'

def is_ip_valid(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        print(f"{ip} is not a valid IP address.")
        return False

def _connect(port = BASE_PORT, host = WEEK4_IP):
    try:
        sock.connect((host, port))
    except Exception as e:
        return False
    return True

def find_port():
    port = BASE_PORT
    host = WEEK4_IP
    if(is_ip_valid(host)): 
        while port < 6130:
            print(f"Trying to connect to port {port}.")
            valid = _connect(port, host)
            if valid:
                print(f"Connected to port {port}.")
                break
            port += 1
        return None

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    find_port()
