"""
enumerate - enumrea iteráveis (índices)
"""

lista = ['Marcus', 'Rayane', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item) 