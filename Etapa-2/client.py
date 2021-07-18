import socket

# target_host = ip do servidor
target_host = '192.168.0.112'
target_port = 12000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
num = 1
while True:
    num = input('Digite um numero: ')
    if(num.isdigit()):
        client.send(num.encode())
        response = client.recv(1024)
        decoded_response = response.decode()
        if(decoded_response != 'kill'):
            print("A soma dos números primos de 0 até " + num + " é " + decoded_response + '\n')
        else:
            break
    else:
        print('Digite um número valido!\n')
print('[*] Conexão finalizada!')