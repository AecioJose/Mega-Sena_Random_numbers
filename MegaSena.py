from os import system
from time import sleep
from random import randint
system('cls')


lista = []

qnt_jogos = int(input('\nQuantos jogos você que gerar?  '))
print(F'======== SORTEANDO {qnt_jogos} JOGOS ========')


for jogos in range(0, qnt_jogos):
    lista.append(list())
    for palpite in range(0, 6):
        num_aletório = randint(1, 60)

        for c in range(0, len(lista)):
            if(lista[c] == num_aletório):
                num_aletório = randint(1, 60)

        lista[jogos].append(num_aletório)
    lista[jogos].sort()

for results in range(0, qnt_jogos):
    print(f'Jogo {results+1:>3}: {lista[results]}')
    if(qnt_jogos <= 20):
        sleep(1)
    elif(qnt_jogos >= 21 and qnt_jogos <= 50):
        sleep(0.5)
    else:
        sleep(0.003)

print('======== ««« BOA SORTE! »»» ========\n\n\n\n\n')
print(f'\n\nEsses foram todos os jogos {lista}')
