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
    CRUD - Create, Read, Update, Delete
"""
#        0   1   2   3
lista = [10, 20, 30, 40]

lista.append(50) # adiciona ao final da lista o número
lista.append(60) # só add ao final da lista
lista.pop() # remove o último item da lista
lista.append(70)

lista.pop(3) # removendo os elementos indicando no índice

lista[2] = 300 # Update
del lista[2] # Delete


# numero = lista[2] <- Podemos atribuir os valores da lista para uma variável
print(lista)
print(lista[2])