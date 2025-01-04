""" Calculadora com while """

while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro: ')
    operador = input('Digite o operador (+ - / *): ')

    num_val = None

    try: 
        num1 = int(num1)
        num2 = int(num2)
        num_val = True

    except: 
        num_val = None

    if num_val is None:
        print('Um ou ambos números não são válidos')
        continue

    op_val = '+-/*'

    if operador not in op_val:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador == '+':
        print(num1 + num2)

    elif operador == '-':
        print(num1 - num2)

    elif operador == '/':
        print(num1 / num2)

    elif operador == '*':
        print(num1 * num2)

    else:
        print('Você nunca deveria chegar aqui...')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        print('Você saiu da Calculadora!')
        break