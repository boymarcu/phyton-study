"""
Cuidado com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
nome = 'Marcus'

# nome[1] = 'D' # TypeError - não pode ser feito isso
noutra_variavel = nome
nome = 'Luiz' # apontando para outra variável

print(nome)
print(noutra_variavel)

lista_a = ['Marcus', 'Maria', 1, True, 1.2] # Valore Imutáveis
lista_b = lista_a.copy() # retorna uma nova lista com os mesmos valores

lista_a[0] = 'Luiz'

print(lista_a)
print(lista_b)