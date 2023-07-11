def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos : Para você o voto é NEGADO.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos : Para você o voto é OPICIONAL.'
    else :
        return f'Com {idade} anos : Para você o voto é OBRIGATÓRIO.'
nasc = int(input("Em que ano você nasceu? "))  
print(voto(nasc))
       
