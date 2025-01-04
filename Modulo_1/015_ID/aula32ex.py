"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""
num = input('Digite um número inteiro: ')

try: 
    num_int = int(num)
    if  num_int % 2 == 0:
        print('Seu número é PAR')
    else:
        print('Seu número é ÍMPAR')
except:
    print('Seu número não é inteiro')

"""_
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada.
Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Que horas são sem os minutos? ')
hora_int = int(hora)

if 0 <= hora_int <= 11:
    print ('Bom dia')
elif 12 <= hora_int <=17:
    print('Boa tarde')
elif 18 <= hora_int <= 23:
    print('Boa noite')
else:
    print('Não é um horário válido')
"""
Faça um programa que peça o primeiro nome do usuário. 
Se o nome tiver 4 letras ou menos escreva:
"Seu nome é curto".
Se tiver entre 5 e 6 letras, escreva:
"Seu nome é normal".
Maior que 6, escrevra:
"Seu nome é muito grande".
"""

nome = input('Escreva seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif 5 <= len(nome) <= 6:
    print('Seu nome é normal')
elif len(nome) >= 7:
    print('Seu nome é grande')
else:
    print('Não há nenhum nome :(')