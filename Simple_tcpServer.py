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

# Função principal do servidor
def servidor():
    serverPort = 1300
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", serverPort))
    serverSocket.listen(5)

    print("TCP Server\n")
    connectionSocket, addr = serverSocket.accept()

    # Gerando chaves do servidor
    bits = 64
    p = gerar_numero_primo(bits)
    q = gerar_numero_primo(bits)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    while mdc(e, phi_n) != 1:
        e = random.randrange(2, phi_n)
    d = inverso_modular(e, phi_n)
    chave_publica = (e, n)
    chave_privada = (d, n)

    # Enviando chave pública para o cliente
    connectionSocket.send(bytes(str(chave_publica[0]), "utf-8"))
    connectionSocket.send(bytes(str(chave_publica[1]), "utf-8"))

    # Recebendo mensagem criptografada do cliente
    mensagem_cripto = connectionSocket.recv(1024)
    mensagem_cripto = [int(i) for i in mensagem_cripto.decode("utf-8").split(",")]

    # Descriptografando a mensagem
    mensagem_desencriptada = rsa_descriptografar(mensagem_cripto, chave_privada)
    print("Mensagem recebida (decriptografada):", mensagem_desencriptada)

    # Processamento (exemplo: transformar a mensagem em maiúsculas)
    mensagem_processada = mensagem_desencriptada.upper()

    # Criptografando a resposta
    resposta_cripto = rsa_criptografar(mensagem_processada, chave_publica)
    connectionSocket.send(bytes(",".join(map(str, resposta_cripto)), "utf-8"))
    
    connectionSocket.close()

# Executando o servidor
servidor()
