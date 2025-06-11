"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
"""

#         01324
#        -54321
string = 'ABCDE' # 5 caracteres

# lista = list() <- Forma menos comum de se criar listas.

#         0    1     2             3    4
#        -5   -4    -3            -2   -1
lista = [123, True, 'Marcus Lima', 1.2, []]
lista[2] = 'Joãozinho'
print(lista)
print(lista[2]) # Acessando no índice um valor