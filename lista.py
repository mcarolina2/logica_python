total= [[] , []]
valor = 0
for v in range(0,8):
    valor = int(input(f'Digite o {v}-. Número: '))
    if valor % 2 == 0:
       total[0].append(valor)
    else:
        total[1].append(valor)
print('--' * 20)
print(f'Todo Os Números são {total}')
print('--' * 20)
print(f'Os Valores Pares São {total[0]}')
print('--' * 20)
print(f'Os Valores Impares São {total[1]}')