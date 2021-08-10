from threading import Thread
from time import sleep
def carro1(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        print(f"Carro {piloto}:", trajeto)
        trajeto += velocidade
        sleep(0.5)


t1 = Thread(target=carro1, args=[10, "A"])
t2 = Thread(target=carro1, args=[20, "B"])

t1.start()
t2.start()