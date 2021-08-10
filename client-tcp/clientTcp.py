from socket import socket, AF_INET, SOCK_STREAM, error
from sys import exit

def main():
    try:
        s = socket(AF_INET, SOCK_STREAM, 0)
    except error as e:
        print(e)
        exit()  
    
    else:
        print("Socket criado com sucesso.")
        
    host_alvo = input("Host/Ip a conectar: ")
    port_alvo = input("Porta a conectar: ")

    try:
        s.connect((host_alvo, int(port_alvo)))
        print("Cliente TCP conectado com sucesso.")
        s.shutdown(2)
    except Exception as e:
        print(e)
        exit()


if __name__ == '__main__':
    main()
