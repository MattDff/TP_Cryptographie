from Crypto.Hash import SHA1, MD5

hash1 = SHA1.new(data=b'ENSEA')
hash2 = SHA1.new(data=b'eNSeA')
hash3 = SHA1.new(data=b'ENSEA')
hash4 = SHA1.new(data=b'EN5EA')
hash5 = MD5.new(data=b'ENSEA')
hash6 = MD5.new(data=b'eNSeA')
hash7 = MD5.new(data=b'ENSEA')
hash8 = MD5.new(data=b'EN5EA')

print("SHA1 de ENSEA : ",hash1.hexdigest())
print("SHA1 de eNSEA : ",hash2.hexdigest())
print("SHA1 de eNSeA : ",hash3.hexdigest())
print("SHA1 de EN5EA : ",hash4.hexdigest())
print("MD5 de ENSEA : ",hash5.hexdigest())
print("MD5 de eNSEA : ",hash6.hexdigest())
print("MD5 de eNSeA : ",hash7.hexdigest())
print("MD5 de EN5EA : ",hash8.hexdigest())

with open("textmodified.txt", "r", encoding="utf-8") as f:
    paragraphe = f.read()

data = paragraphe.encode("utf-8")
long_hash = SHA1.new(data=data)
print("SHA1 du paragraphe : ",long_hash.hexdigest())

with open("text.txt", "r", encoding="utf-8") as f:
    paragraphe2 = f.read()

data2 = paragraphe2.encode("utf-8")
long_hash2 = SHA1.new(data=data2)
print("SHA1 du paragraphe : ",long_hash2.hexdigest())