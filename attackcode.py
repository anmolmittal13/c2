import socket
import sys

BASE_PORT = 3040
WEEK4_IP = '10.0.2.5'

def shell():
    print("Starting terminal. To exit terminal type 'q'.")
    while True:
        cmd = input("$: ")
        if(cmd == "q"):
            sock.close()
            break
        else:
            sock.send(cmd.encode('utf-8'))
        result = s.recv(4096)
        print(result.decode())

def is_ip_valid(ip):
    if ip.count('.') != 3:
        print(f"{ip} is not a valid IP address.")
        return False
    segments = ip.split('.')
    for segment in segments:
        try:
            num = int(segment)
            if not (0 <= num <= 255):
                print(f"{ip} is not a valid IP address.")
                return False
        except ValueError:
            print(f"{ip} is not a valid IP address.")
            return False
    return True

def _connect(port = BASE_PORT, host = WEEK4_IP):
    try:
        sock.connect((host, port))
    except Exception as e:
        return False
    return True

def find_port():
    port = BASE_PORT
    host = WEEK4_IP
    if is_ip_valid(host):
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
    shell()
