from os.path import exists
from os import makedirs,system,remove
from err import *

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from base64 import b85encode,b85decode

class Encrypt:
    def __init__(self,username:str,password:str,source:str) -> None:
        '''
        userdata:
            username:the user name of website
            password: password of website
            source: the name of website
            
        '''
        self.username = username
        self.password = password
        
    def generate(self):
        '''
        it  has encrypt mode
        '''
        key = RSA.generate(2048)
        pubkey = key.publickey()
        aeskey = get_random_bytes(16)
        
        #rsa encrypt aes key
        atrsa = PKCS1_OAEP.new(pubkey)
        encaeskey = atrsa.encrypt(aeskey)
        
        #AES to encrypt data
        ataes = AES.new(aeskey,AES.MODE_EAX)
        encrypted, tag = ataes.encrypt_and_digest(bytes(self.password,encoding="utf-8"))
        #saving files
        #rsa keys
        with open(f"{self.username}/pubkey.pem","wb") as file:
            file.write(key.publickey().export_key(passphrase=self.username,pkcs=8,protection="scryptAndAES128-CBC"))
        with open(f"{self.username}/prikey.pem","wb") as file:
            file.write(key.export_key(passphrase=self.username,pkcs=8,protection="scryptAndAES128-CBC"))
        
        #let something readable
        self.prikey = key
        self.aes = ataes
        self.pubkey = key.publickey()
        with open(f"{self.username}/encryption.bin","wb") as file:
            file.write(encaeskey)
            file.write(ataes.nonce)
            file.write(tag)
            file.write(aeskey)
        return encrypted
    
    def encrypt(self):
        with open(f"{self.username}/encryption.bin","rb") as file:
            aeskey = file.read(-1)
            aes = AES.new(aeskey,AES.MODE_EAX)
            encrypted,tag = aes.encrypt_and_digest(bytes(self.password,encoding="utf-8"))
        return encrypted
        
class Decrypt:
    def decrypt(username:str, encryption_file:str,encrypted:str):
        prikey = RSA.import_key(open(f"{username}/prikey.pem").read(),passphrase=username)
        with open(encryption_file,"rb") as file:
            encaeskey = file.read(prikey.size_in_bytes())
            nonce = file.read(16)
            tag = file.read(16)
        
        #rsa decrypt aes key
        rsa = PKCS1_OAEP.new(prikey)
        aeskey = rsa.decrypt(encaeskey)
        
        #aes decrypt data
        aes = AES.new(aeskey,AES.MODE_EAX,nonce)
        data = aes.decrypt_and_verify(encrypted,tag)
        
        return data.decode()
system("cls")    
encrypt = Encrypt(username="Justmore5mins",password="HelloWorld",source="www.google.com")
encrypted = encrypt.encrypt()
print(encrypted)
print(Decrypt.decrypt("Justmore5mins","Justmore5mins/encryption.bin",encrypted))