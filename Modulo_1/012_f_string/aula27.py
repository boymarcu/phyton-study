"""
Fatiamento de strings
    012345678
    Olá Mundo
   -987654321

Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[-4]) # Acessando o índice
print(variavel[4:]) # os : designa o final, quando não tem nenhum número do índice, ele vai até o final
print(variavel[4:7]) # vai até o índice 7 
print(variavel[0:4])
print(variavel[:4]) # omitindo o início
print(variavel[0:9:1]) # contando de 1 em 1
print(variavel[0:9:2]) # contando de 2 em 2
print(variavel[0:9:-1]) # contando de trás pra frente
print(variavel[::-1]) # forma alternativa

print(len(variavel)) # retorna quantos caracteres possui (não é a mesma coisa que índice)
print(variavel[0:len(variavel):1])