'''
# Operadores lógicos
    and (e)     or (ou)     not (não)
# and - Todas as condições precisam ser verdadeiras.
# or  - Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.
# São considerados falsy (já vimos)
    0       0.0     ''      False
# Também existe o tipo None que é usado para representar um não valor.
'''
# Avaliação de curto cirtuito -> OR

entrada = input('[E]ntrar [S]air')
senha = input('Senha: ')

senha_permitida ='123456'
    # envolvendo a condição de entrada em parenteses para que seja avaliada primeira
if (entrada == 'E'or entrada == 'e') and senha == senha_permitida:
    print('Entrar')
else:
    print('Sair')