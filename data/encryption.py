from os.path import exists
from os import makedirs,system,remove

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from os import urandom
from base64 import b64decode, b64encode

class Encrypt:
    def __init__(self,username:str,password:str, source:str) -> None:
        '''
        userdata:
            username:the user name of website
            password: password of website
            source: the name of website
            
        '''
        self.username = username
        self.password = password
        self.source = source
        
    def __prepare(self, dir:str = ""):
        '''
        public key, private key AESKey
        '''
        AESKey = urandom(16)
        key = RSA.generate(1024)
        pubkey = key.publickey()

        with open(f"{dir}/aes.txt","wb") as file:
            file.write(b64encode(AESKey))
        with open(f"{dir}/pubkey.pem","wb") as file:
            file.write(b64encode(pubkey.save_pkcs1()))
        with open(f"{dir}/prikey.pem","wb") as file:
            file.write(b64encode(prikey.save_pkcs1()))

        return pubkey, AESKey
        
    def encrypt(self):
        """
        using aes and rsa to encrypt data
        """
        password = bytes(self.password,encoding="utf-8")
        pubkey,aeskey = self.__prepare(self.username)
        rsaencrypt = rsa.encrypt(password,pubkey)
        aes = AES.new(aeskey,AES.MODE_CBC).encrypt(rsaencrypt)
        last = b64encode(aes)
        
        return last

class Decrypt:
    def __init__(self,username:str,data:str|bytes):
        #---------------RSA---------------------
        try:
            data = bytes(data,encoding="utf-8")
        except:
            pass
        with open(f"{username}/prikey.pem","rb") as file:
            read = b64decode(file.read())
        rsakey = rsa.PrivateKey.load_pkcs1(read)
        #---------------AES----------------------
        with open(f"{username}/aes.txt","rb") as file:
            key = b64decode(file.read())
        text = AES.new(key,AES.MODE_CBC)
        aes = text.decrypt(pad(data,))
        return str(rsa.decrypt(aes,rsakey))
        
        
    
thing = Encrypt(username="Justmore5mins",password="HelloWorld",source="www.google.com")
system("cls")
encrypt = thing.encrypt()
print(encrypt)
decrypt = Decrypt("Justmore5mins",encrypt)
print(decrypt)