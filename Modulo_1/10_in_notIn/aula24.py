'''
# Operadores in e not in
# String são iteráveis (pode navegar item por item)
    0 1 2 3 4 5
    O t á v i o
    -6-5-4-3-2-1
'''
nome = 'Otávio'
print(nome[2]) # Para acessar o índice
print(nome[-4])

print('á' in nome) # Checar se 'á' está entre as letras do nome
print('z' in nome) # Checar se 'z' está entre as letras do nome

print('vio' in nome) # Checar se 'vio' está entre as letras do nome

print('á' not in nome) # Checar se 'á' não está entre as letras do nome
print('z' not in nome) # Checar se 'z' não está entre as letras do nome

print('vio' not in nome) # Checar se 'vio' não está entre as letras do nome

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')