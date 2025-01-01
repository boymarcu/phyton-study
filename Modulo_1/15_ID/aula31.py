"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
v1 = 'a'
v2 = 'a'
print(id(v1)) # vendo a identidade de um elemento na memória
print(id(v2))

''''''
condicao = False
passou_no_if = None

# forma ruim de código
if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    passou_no_if = None
    print('Não faça algo')

print(passou_no_if, passou_no_if is None) # mesma coisa que usar ==
print(passou_no_if, passou_no_if is not None) # mesma coisa que usar ==