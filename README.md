# N1_Atividade_RSA

## Visão Geral

Este projeto implementa um sistema de comunicação simples entre um cliente e um servidor, utilizando o algoritmo RSA para criptografia e troca de chaves. A comunicação ocorre via uma conexão TCP, e os dados trocados são criptografados usando o algoritmo RSA para garantir a segurança da informação.

O sistema é composto por duas partes:

- **Cliente:** Conecta-se ao servidor, gera chaves RSA, envia uma mensagem criptografada e recebe a resposta criptografada do servidor.
- **Servidor:** Escuta por conexões dos clientes, recebe a mensagem criptografada, descriptografa, processa a mensagem, criptografa a resposta e envia-a de volta ao cliente.

## Requisitos

- Python 3.x
- Biblioteca `socket` (para comunicação TCP)
- Biblioteca `random` (para geração de chaves aleatórias)
- Biblioteca `math` (para cálculos matemáticos no algoritmo RSA)

## Instalação

Para rodar o sistema, basta executar os scripts do servidor e do cliente em terminais diferentes.

1. **Servidor:**
   - Execute o script do servidor em um terminal com o seguinte comando:

   ```bash
   python3 servidor.py
