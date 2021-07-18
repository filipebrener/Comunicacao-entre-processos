import socket

# bind_ip = ip do servidor
bind_ip = '192.168.0.112'
bind_port = 12000

def isprim(num):
    for i in range(2,num):
        if(num%i == 0):
            return False
    return True

def prime_sum(num):
    sum = 0
    for i in range(2,int(num)):
        if isprim(i) == True:
            sum += i
    return str(sum)
 

def recv_connection():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip,bind_port))
    server.listen(1)
    print('[*] Escutando pelo ip:%s port:%s' %(bind_ip,bind_port))
    client, addr = server.accept()
    print('[*] Conexão aceita de: %s:%d\n' %(addr[0],addr[1]))
    return client

def handle_client(client_socket):
    num = 1
    while num != 0:
        num_encoded = client_socket.recv(1024)
        num = int(num_encoded.decode())
        if(num != 0):
            num_sum = prime_sum(num)
            client_socket.send(num_sum.encode())
            print("[*] Recebido %d\n[*] Respondido: %s\n" %(num,num_sum))

    client_socket.send('kill'.encode())
    print("[*] Finalizando conexão!")
    client_socket.close()

if(__name__ == '__main__'):
    client = recv_connection()
    handle_client(client)
    print('[*] Fechando server!')