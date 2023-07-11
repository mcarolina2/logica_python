from random import randint
from time import sleep


def sorteio(lista):
    print('Sorteando 5 Valores da lista: ', end='')
    for cont in range(0,5):
        v = randint(1,10)
        lista.append(v)
        print(f'{v} ', end='', flush=True )
        sleep(0.2)
        print('Pronto!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da {lista} ,  temos  {soma}')
números = list()
sorteio(números)  
somapar(números)
