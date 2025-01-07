"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.

- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade
para o usuário digitar apenas uma letra.

- Quando o usuário digitar uma letra, você vai conferir se a letra 
digitada está na palavra secreta.

- Se a letra digitada estiver na palavra secreta, exiba a letra.
- Se a letra digitada não estiver nma palavra secreta, exiba *.

Faça a contagem de tentativas do seu usuário
"""

palavra = 'caixa'
acertos = ''
tentativas = 0

while True:

    entrada = input ('Digite uma letra: ')
    tentativas += 1

    if len(entrada) > 1:
        print('Digite apenas uma letra.')
        continue

    if entrada in palavra:
        acertos += entrada
        
    palavra_formada = ''
    for letra in palavra:
        if letra in acertos:
                palavra_formada += letra
        else:
                palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra:
            print('VOCÊ GANHOU!! PARABÉNS!')
            print('A palavra era', palavra)
            print('Tentativas:', tentativas)
