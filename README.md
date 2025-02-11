# Gerenciador de Senhas Seguro em Python

Bem-vindo ao **Gerenciador de Senhas Seguro**, um sistema desenvolvido em Python que permite armazenar suas senhas de forma criptografada e acessá-las usando uma chave mestra. Esse gerenciador mantém suas senhas seguras, armazenando-as juntamente com os domínios e as datas associadas, garantindo que suas credenciais sejam sempre protegidas.

## Objetivo

Este projeto tem como objetivo fornecer uma maneira simples e eficiente de gerenciar senhas, mantendo a segurança das informações através de criptografia. Com ele, você poderá:

- Armazenar senhas criptografadas de diferentes serviços e sites.
- Associar cada senha ao seu respectivo domínio (site ou serviço).
- Registrar a data de criação ou modificação das senhas.
- Acessar suas senhas de maneira segura utilizando uma **chave mestra**.

## Funcionalidades

- **Armazenamento Criptografado**: As senhas são criptografadas utilizando um algoritmo seguro (como AES ou similar).
- **Chave Mestra**: Você define uma chave mestra única, que é usada para acessar todas as senhas armazenadas.
- **Domínios e Datas**: Cada senha é associada ao seu respectivo domínio (ex: "google.com") e a data de criação ou modificação.
- **Busca de Senhas**: Permite buscar por senhas associadas a um domínio específico.
- **Facilidade de Uso**: Interface simples para que você possa adicionar, modificar e acessar suas senhas de maneira eficiente.

## Como Usar

1. **Clonar o Repositório**:
   - Para começar, clone este repositório em sua máquina local:
     ```bash
     git clone https://github.com/seu-usuario/gerenciador-de-senhas.git
     cd gerenciador-de-senhas
     ```

2. **Instalar Dependências**:
   - Instale as bibliotecas necessárias (por exemplo, `cryptography` para criptografia):
     ```bash
     pip install -r requirements.txt
     ```

3. **Configuração Inicial**:
   - Ao executar o programa pela primeira vez, você será solicitado a criar uma **chave mestra**. Essa chave será usada para criptografar e descriptografar as senhas.
   
4. **Adicionar uma Senha**:
   - Para adicionar uma nova senha, execute o script:
     ```bash
     python gerenciador.py adicionar
     ```
     Você será solicitado a fornecer:
     - O domínio ou serviço (ex: "google.com").
     - A senha para esse serviço.
     - A data de criação ou modificação da senha.

5. **Acessar Senhas**:
   - Para acessar suas senhas, execute:
     ```bash
     python gerenciador.py acessar
     ```
     Insira sua chave mestra e o programa exibirá as senhas descriptografadas, associadas aos respectivos domínios.

6. **Buscar por Senhas**:
   - Para buscar uma senha associada a um domínio específico, execute:
     ```bash
     python gerenciador.py buscar --dominio google.com
     ```

## Estrutura do Projeto

- **`gerenciador.py`**: Script principal para gerenciar senhas.
- **`crypt.py`**: Arquivo responsável pela criptografia e descriptografia das senhas.
- **`requirements.txt`**: Dependências do projeto.
- **`senhas.db`**: Arquivo onde as senhas criptografadas são armazenadas.

## Exemplo de Uso

1. Criação da chave mestra:
   ```bash
   python gerenciador.py configurar
