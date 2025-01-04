"""
Iterando strings com while
"""
#       012345678910

nome = 'Marcus Lima' # Iteráveis
#      1110987654321

tamanho_nome = len(nome) # Tamanho do nome
print(nome) # Lê o nome
print(tamanho_nome) # Diz quantas letras possuem

print(nome[4]) # Acessa o índice 4 (u)

# Utilizar while para em cada indíce possuir um * entre cada letra

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)