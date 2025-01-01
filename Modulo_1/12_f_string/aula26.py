'''
Formatação básica de strings

s - string
d - int
f - float
.<numero de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
ex.: 0>-100,.1f
Conversion flags - !r !s !a - __repr__  __str__ __ask__
'''

variavel = 'ABC'
print(f'{variavel}')

        # 10 caracteres à esquerda
print(f'{variavel: >10}')

        # 10 caracteres à direita
print(f'{variavel: <10}.')

        # 10 caracteres no centro
print(f'{variavel:.^10}.')


print(f'{1000.9239182956812:,.1f}')
print(f'{1000.9239182956812:0=+10,.1f}')


print(f'O hexadecimal de 1500 é {1500:08x}')


print(f'{variavel!r}')