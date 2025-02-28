from socket import *
import random

# Função para realizar o teste de primalidade de Miller-Rabin
def miller_rabin(n, k=5):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def gerar_numero_primo(bits):
    while True:
        numero = random.getrandbits(bits) | 1
        if miller_rabin(numero):
            return numero

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def inverso_modular(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Função para criptografar e descriptografar com RSA
def rsa_criptografar(mensagem, chave_publica):
    e, n = chave_publica
    return [pow(ord(c), e, n) for c in mensagem]

def rsa_descriptografar(mensagem_cripto, chave_privada):
    d, n = chave_privada
    return ''.join(chr(pow(c, d, n)) for c in mensagem_cripto)

# Função principal do cliente
def cliente():
    serverName = "10.1.70.9"  # Endereço IP do servidor
    serverPort = 1300  # Porta do servidor
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    # Recebendo a chave pública do servidor
    e = int(clientSocket.recv(1024).decode("utf-8"))
    n = int(clientSocket.recv(1024).decode("utf-8"))
    chave_publica = (e, n)

    # Entrando com a mensagem
    mensagem = input("Digite a mensagem para enviar: ")

    # Criptografando a mensagem
    mensagem_cripto = rsa_criptografar(mensagem, chave_publica)
    clientSocket.send(bytes(",".join(map(str, mensagem_cripto)), "utf-8"))

    # Recebendo a resposta do servidor
    resposta_cripto = clientSocket.recv(1024)
    resposta_cripto = [int(i) for i in resposta_cripto.decode("utf-8").split(",")]

    # Descriptografando a resposta
    chave_privada = (d, n)  # A chave privada 'd' e 'n' são a chave do servidor ou calculadas pelo cliente
    resposta_desencriptada = rsa_descriptografar(resposta_cripto, chave_privada)

    print("Resposta do servidor (decriptografada):", resposta_desencriptada)

    clientSocket.close()

# Executando o cliente
cliente()
