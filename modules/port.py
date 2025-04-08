import socket
import sys

def get_available_port(portList):
    for port in portList:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(("", port))
            sock.close()
            return port
        except socket.error:
            print(f"Port {port} is already in use. Trying next port...")
         #   port += 1
    print('All ports are busy right now plese close the terminal completly and then try again')
    sys.exit()