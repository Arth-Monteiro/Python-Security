from socket import socket, AF_INET, SOCK_DGRAM, error
from sys import exit

def main():
    try:
        s = socket(AF_INET, SOCK_DGRAM)
    except error as e:
        print(e)
        exit()  
    
    else:
        print("Socket criado com sucesso.")
        
    host = 'localhost'
    port = 5432
    message = '\nServer: Hello Client'

    try:
        s.bind((host, port))
        while True:
            dados, end = s.recvfrom(4096)
            
            if dados:
                print("Servidor enviando mensagem...")
                s.sendto(dados + (message.encode()), end)
                break

    except Exception as e:
        print(e)
        exit()

    finally:
        print("Fechando conexão.")
        s.close()


if __name__ == '__main__':
    main()
