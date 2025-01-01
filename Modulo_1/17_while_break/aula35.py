"""
Repetições
    while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
"""
    código unredable (ou unwritable não sei se ouvi direito)
while False: 
    print('EITA') 

print('Acabou')
"""

contador = 0 

'''
    Nessa forma, o contador vai começar a partir do um pois
while contador < 10:
    contador = contador + 1 # a função de conta começa antes do print
    print(contador) 

print('Acabou')
'''

# Melhor forma a se fazer para começar do zero, porem ele vai até o 9 pois o 0 conta como 10 caracteres
'''
while contador < 10:
    print(contador)
    contador = contador + 1

print('Acabou')
'''

# Assim, o contador vai até o 10, pois quando 10 == 10 ele para de rodar o while
while contador <= 10:
    print(contador)
    contador = contador + 1

print('Acabou')