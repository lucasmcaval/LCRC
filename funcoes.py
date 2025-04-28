from random import *

def rolar_dados(numero):
    lista = []
    for i in range(numero):
        n = randint(1, 6)
        lista.append(n)
    return lista