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
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b # Concatenação
print(lista_c)

lista_a.extend(lista_b)
print(lista_a)