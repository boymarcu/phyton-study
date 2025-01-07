"""
(pode te entregar uma coisa por vez)
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu interador
"""
numeros = range (0, 100, 8)

for numero in numeros:
    print(numero)
    

        # __iter__()
text = iter('Marcus') # iterável

iterador = iter(text) # iterador

print(next(text)) #.__next__()
print(next(text))
print(next(text))
print(next(text))

# o for faz isso por de baixo dos panos
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

for letra in text:
    print(letra)