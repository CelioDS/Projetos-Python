import random
R = "\033[1;31m"
G = "\033[0;32m"
r = "\033[0;m"

lista = ['Arroz']
aleatorio = random.randint(0,len(lista))
palavra =list()
certa = list()
for l in lista[aleatorio]:
    certa.append(l.upper())
    palavra.append('-')

print(certa)
print(palavra)
tentativa =  0

while True:
    chute = str(input(f"Chute a {tentativa}° letra :>>>\t").upper())
    if chute not in certa:
        print(R + "Voce errou a letra!!!" + r)
    else:
        print(G + "letra certa" + r)
    for posicao, letra in enumerate(certa):
        if chute == letra:
            palavra[posicao] = chute
    for n in palavra:
        print(f'{n:<2}', end='')
    print('\n')
    if certa == palavra:
        print(G+'PARABENS VOCE GANHOU!!!'+r)
        break
    elif tentativa >= len(certa)+2:
        print(R+"Voce perdeu!!!"+r)
        break

    tentativa += 1





