# input() <- Função

'''nome = input('Qual o seu nome? ')   # Dica: deixar esse espaço no final pois o usuário vai escrever.
                                    # Após preenchido, o interpretador vai guardar a entrada na variável "nome" 
'''
'''
    # Por padrão, toda função INPUT vai retornar uma str então,
    # fazemos a conversão de str para int:
numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

print(f'A soma dos números é: {numero_1 + numero_2}')
'''
'''
    # O mais correto a se fazer é realizar uma checagem se o valor do usuário é um int antes de chegar na soma

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')

    int_num_1 = int(numero_1)
    int_num_2 = int(numero_2)

print(f'A soma dos números é: {int_num_1 + int_num_2}')

'''