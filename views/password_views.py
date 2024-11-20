import string, secrets #Conjunto de texto
import hashlib #Criptografador
import base64 #Base 64 é um método para codificação de dados para transferência na Internet
from pathlib import Path #Manipulador de diretorios
from cryptography.fernet import Fernet, InvalidToken

class FernetHasher: #FernetHasher é o metodo random string para gerar uma chave aleatoria
    RANDOM_STRING_CHARS = string.ascii_lowercase + string.ascii_uppercase #RANDOM_STRING_CHARS é a variavel geradora de senha, 'string.' para chamar o import string
    BASE_DIR =Path(__file__).resolve().parent.parent #Raiz do projeto ate o arquivo
    KEY_DIR = BASE_DIR / 'keys' #Pasta onde vai ser armazenada a chave
    
    def __init__(self, key): #Função para dividir usuarios
        if not isinstance(key, bytes):
            key = key.encode()
    
        self.fernet = Fernet(key)
    
    @classmethod #Metodo de clase
    def _get_random_string(cls, length=25): #CLS pois é uma variavel de clase
        string = '' #Armazena o texto
        for i in range(length): #Repetir o codigo
            string += secrets.choice(cls.RANDOM_STRING_CHARS) #String vai ser = a string ja armazenada + a nova

        return string #Return devolve o valor quando chamado

    @classmethod
    def create_key(cls, archive=False): #Função de criar a chave
        value = cls._get_random_string() #Armazena dentro da variavel value a string aleatoria
        hasher = hashlib.sha256(value.encode('utf-8')).digest() # Transforma a string armazenada em bits
        key = base64.b64encode(hasher) #Transforma o hasher em base 64
        if archive: #Se definir a variavel como verdadeira
            return key, cls.archive_key(key) # Return
        return key, None

    @classmethod
    def archive_key(cls, key): #Salva a chave dentro de um arquivo sem sobescrever
        file = 'key.key'
        while Path(cls.KEY_DIR / file).exists():
            file = f'key_{cls._get_random_string(length=5)}.key'

        with open(cls.KEY_DIR / file, 'wb') as arq: #with é um gerenciador de contexto
            arq.write(key) #O valor a guardar dentro do arquivo

        return cls.KEY_DIR / file #Caminho do arquivo

    def encrypt (self, value): #Função de criptografar os dados
        if not isinstance(value, bytes):
            value = value.encode()
        return self.fernet.encrypt(value)

    def decrypt(self, value): #Função de descriptografar a senha
        if not isinstance(value, bytes):
            value = value.encode()
        
        try:
            return self.fernet.decrypt(value).decode()
        except InvalidToken as e: #Tratamento da mensagem para o usuario em caso de erro
            return 'Token inválido'