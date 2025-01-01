'''
# Operadores lógicos
    and (e)     or (ou)     not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.
# São considerados falsy (já vimos)
    0       0.0     ''      False
# Também existe o tipo None que é usado para representar um não valor.
'''

# Avaliação de curto cirtuito -> AND

entrada = input('[E]ntrar [S]air')
senha = input('Senha: ')

senha_permitida ='123456'

if entrada == 'E' and senha == senha_permitida:
    print('Entrar')
else:
    print('Sair')
