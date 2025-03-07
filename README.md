# N1_Atividade_RSA

## Visão Geral

Este projeto implementa um sistema de comunicação segura entre um cliente e um servidor, utilizando o algoritmo de criptografia RSA para garantir a privacidade dos dados trocados. A comunicação ocorre via uma conexão TCP, e os dados trocados são criptografados usando o algoritmo RSA, tanto para a troca de chaves quanto para a criptografia das mensagens enviadas entre cliente e servidor.

### Estrutura do Sistema

- **Cliente:** Conecta-se ao servidor, gera chaves RSA, criptografa uma mensagem e envia-a ao servidor. O cliente recebe uma resposta criptografada do servidor, que é então descriptografada e exibida.
- **Servidor:** Escuta as conexões dos clientes, recebe mensagens criptografadas, descriptografa-as, processa a mensagem e envia uma resposta criptografada de volta ao cliente.

## Requisitos

- Python 3.x
- Bibliotecas `socket` (para comunicação TCP), `random` (para geração de chaves aleatórias) e `math` (para cálculos matemáticos no RSA).

## Instalação

Para rodar o sistema, basta executar os scripts do servidor e do cliente em terminais diferentes.

### Passos para execução:

1. **Servidor:**
   - Execute o script do servidor em um terminal com o seguinte comando:
     ```bash
     python3 servidor.py
     ```

2. **Cliente:**
   - Execute o script do cliente em outro terminal com o comando:
     ```bash
     python3 cliente.py
     ```

## Como Funciona

### Geração das Chaves RSA

O sistema gera chaves RSA tanto para o cliente quanto para o servidor. O processo de geração de chaves é o seguinte:

1. **Geração de Números Primos:** São gerados dois números primos grandes e aleatórios.
2. **Cálculo de `n` e `phi(n)`:** O módulo `n` é calculado como o produto desses dois números primos, e a função totiente de `n` (phi(n)) é calculada.
3. **Geração da Chave Pública e Privada:**
   - A chave pública é composta por um expoente `e` e o módulo `n`.
   - A chave privada é composta pelo expoente `d` e o módulo `n`, onde `d` é o inverso modular de `e` em relação a `phi(n)`.

As chaves são trocadas entre o cliente e o servidor para que ambos possam criptografar e descriptografar as mensagens com segurança.

### Criptografia e Descriptografia com RSA

#### Criptografia:

1. A mensagem é convertida para uma lista de números que representam os valores ASCII de cada caractere.
2. Cada número é criptografado usando a chave pública, com a fórmula \( C = M^e \mod n \), onde `M` é o valor numérico do caractere, `e` é o expoente público e `n` é o módulo.

#### Descriptografia:

1. A mensagem criptografada é recebida e cada número criptografado é decodificado utilizando a chave privada, com a fórmula \( M = C^d \mod n \), onde `C` é o valor criptografado, `d` é o expoente privado e `n` é o módulo.

### Interação Cliente-Servidor

#### Cliente:

1. O cliente se conecta ao servidor e envia sua chave pública.
2. O cliente recebe a chave pública do servidor e gera a chave compartilhada.
3. O cliente criptografa a mensagem de entrada usando a chave pública do servidor e envia a mensagem criptografada.
4. O cliente recebe a resposta criptografada do servidor, descriptografa e exibe o resultado.

#### Servidor:

1. O servidor aguarda uma conexão de cliente e recebe a chave pública do cliente.
2. O servidor gera sua chave privada e pública, e envia sua chave pública ao cliente.
3. O servidor recebe a mensagem criptografada do cliente, descriptografa utilizando sua chave privada e processa a mensagem.
4. O servidor criptografa a resposta utilizando a chave pública do cliente e envia a resposta ao cliente.

## Explicação do Código

### Script do Cliente (`cliente.py`)

1. **Estabelecendo uma Conexão TCP:** O cliente cria um socket e se conecta ao servidor no IP e na porta especificados.
2. **Geração de Chaves (RSA):** O cliente gera uma chave privada e calcula sua chave pública, que envia ao servidor.
3. **Criptografia da Mensagem:** Usando a chave pública do servidor, o cliente criptografa a entrada do usuário e envia a mensagem criptografada ao servidor.
4. **Recebendo a Resposta:** O cliente recebe a resposta criptografada do servidor, descriptografa e imprime o resultado.

### Script do Servidor (`servidor.py`)

1. **Aguardando Conexões:** O servidor escuta as conexões de entrada na porta especificada.
2. **Geração de Chaves (RSA):** Após receber a chave pública do cliente, o servidor gera sua chave privada e calcula sua chave pública, que envia de volta ao cliente.
3. **Descriptografia da Mensagem:** O servidor descriptografa a mensagem recebida do cliente utilizando a chave privada.
4. **Processamento da Mensagem:** O servidor converte a mensagem recebida para maiúsculas e a criptografa novamente com a chave pública do cliente antes de enviar a resposta.

## Tutorial de Execução

1. **Configuração:**
   - Abra a pasta do projeto no Visual Studio Code em ambos os computadores (cliente e servidor).
   - No arquivo `Simple_tcpServer.txt`, ajuste o endereço de IP conforme necessário.
   
2. **No Computador Servidor:**
   - Abra o terminal no VS Code e execute o seguinte comando:
     ```bash
     py .\Simple_tcpServer.txt
     ```

3. **No Computador Cliente:**
   - Abra o terminal no VS Code e execute o seguinte comando:
     ```bash
     py .\Simple_tcpClient.txt
     ```

4. **Interação:**
   - No computador cliente, digite a frase desejada no terminal.
   - O resultado será exibido em ambos os terminais (cliente e servidor).

## Notas

- O algoritmo RSA garante que a comunicação entre o cliente e o servidor seja segura, mesmo em um canal não seguro, pois apenas quem possui a chave privada pode descriptografar a mensagem.
- As chaves públicas são trocadas entre cliente e servidor, enquanto as chaves privadas são mantidas em segredo.
- A criptografia e a descriptografia utilizam a matemática modular para garantir que a comunicação seja segura.
- A implementação assume que tanto o cliente quanto o servidor possuem recursos para gerar números primos grandes para a geração das chaves RSA, garantindo a segurança da comunicação.
