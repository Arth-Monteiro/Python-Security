from hashlib import new

path = "./comparador-hash/"
arquivo1 = path + "arquivo1.txt"
arquivo2 = path + "arquivo2.txt"

hash1 = new("ripemd160")
hash1.update(open(arquivo1, "rb").read())

hash2 = new("ripemd160")
hash2.update(open(arquivo2, "rb").read())

if hash1.digest() == hash2.digest():
    print("Arquivos iguais")
else:
    print("Arquivos diferntes:")
    print("Hash 1:", hash1.hexdigest())
    print("Hash 2:", hash2.hexdigest())
