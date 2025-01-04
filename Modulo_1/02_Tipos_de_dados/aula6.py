# Conversão de tipos, coerção
# type convertion, typecasting, coercion.
# É o ato de converter um tipo em outro tipos imuáveis e primitivos:
# str, int, float, bool

print('1', type('1')) # = str
print(int('1'), type(int('1')))  # = int

print (int('1') + 1) # Vai transformar a str em int devido a classe int() 

print(float('1.2') + 1) # Vai transformar a str em float devido a classe float()
print(float('1') + 1) # Vai transformar a str em float devido a classe float() 

print(bool(' ')) # Vai transformar a str em boolean devido a classe bool()

print(str(11) + 'b') # Transforma o int em str devido a calsse str()