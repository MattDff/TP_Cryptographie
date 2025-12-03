import base64
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256

#  Question 5.8 
password = "123PetitsChats"
key_length = 32
iterations = 600000

salt = "JR53k2vFWO11bPrXZLcCYEE01fxSQhTy/8oWaco0bIs="
decode_salt = base64.b64decode(salt)

key = PBKDF2(password, decode_salt,dkLen=key_length,count=iterations,hmac_hash_module=SHA256)

print(key.hex())

# Question 5.12
mnemonic = input("Enter mnemonic phrase : ")
mnemonic = "".join([c for c in mnemonic if c.isalpha()])

# seed = PBKDF2(, ,dkLen=64,count=2048,hmac_hash_module=SHA256)