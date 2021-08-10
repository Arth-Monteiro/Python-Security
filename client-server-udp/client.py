from socket import socket, AF_INET, SOCK_DGRAM, error
from sys import exit

def main():
    try:
        s = socket(AF_INET, SOCK_DGRAM)
    except error as e:
        print(e)
        exit()  
    
    else:
        print("Cliente socket criado com sucesso.")
        
    host = 'localhost'
    port = 5432
    message = '\nClient: Hello Server'

    try:
        print("Cliente: " + message)
        s.sendto(message.encode(), (host, port))

        dados, _ = s.recvfrom(4096)
        dados = dados.decode()
        print("Cliente: " + dados)
    except Exception as e:
        print(e)
        exit()
    finally:
        print("Cliente: Fechando a conexão")
        s.close()


if __name__ == '__main__':
    main()
