num1 = input('Digite um valor: ')
num2 = input('Digite outro valor: ')

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 == num2:
    print('Os valores são iguais')
else:
    print(f'{num1} é menor que {num2}')