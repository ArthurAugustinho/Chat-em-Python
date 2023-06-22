import socket 

def cliente():
    cliente_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    endereco_servidor = ('10.24.0.137', 5000)

    try:
        cliente_soket.connect(endereco_servidor)

        while True:

            mensagem = input("Digite uma mensagem (exit para sair): ")

            if mensagem == 'exit':
                break

            cliente_soket.send(mensagem.encode())
    finally:
        cliente_soket.close()

cliente()