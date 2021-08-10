from hashlib import md5

resultado = md5(b"Python Security")

print(resultado.hexdigest())