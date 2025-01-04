nome = 'Marcus Lima'
altura = 1.73333
peso = 95
imc = peso / (altura*altura)


# Formatação de strings 
# F STRING
# :.2 duas casas decimais -> delimita as casas decimais

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é {imc:.2f}'

print(linha_1)
print(linha_2)