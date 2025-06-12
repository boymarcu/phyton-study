"""
Introdução ao desempacotamento + tuples (tuplas)
"""

nomes = ['Marcus', 'Luiz', 'Rayane']
nome1, nome2, nome3 = nomes
print(nome1, nome2, nome3)


'''
forma alternativa:

nome1, nome2, nome3 = ['Marcus', 'Luiz', 'Rayane']
print(nome1, nome2, nome3)
'''


# Caso queira pegar apenas 1 dos valores dentro da lista se faz da seguinte forma:

nome1, *_ = ['Marcus', 'Luiz', 'Rayane']
print(nome1)
