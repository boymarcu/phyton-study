text = 'Python'
i = 0
tamanho_str = len(text)

while i < tamanho_str:
    print(text[i], i)

    i += 1
# While é mais usado com variáveis
## iterando string


## iterando com for in

# a variavel letra você cria

new_text = ''

for letra in text:
    new_text += f'*{letra}'
    print(letra)
print(new_text + '*')