frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

print(frase.count('Python'))

i = 0

apareceu_mais = 0
letra_maisX = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        continue

    letra_apareceu = frase.count(letra_atual)

    if apareceu_mais < letra_apareceu:
        apareceu_mais = letra_apareceu
        letra_maisX = letra_atual

    i += 1

print('A letra que apareceu mais vezes foi' f'{letra_maisX} que apareceu' f'{apareceu_mais}x')