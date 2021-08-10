from random import SystemRandom
from string import ascii_letters, digits

tam = 16
chars = ascii_letters + digits + "!@#$%&*"

rnd = SystemRandom()

print("".join(rnd.choice(chars) for _ in range(tam)))