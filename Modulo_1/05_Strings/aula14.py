a = 'A'
b = 'B'
c = 1.1

# Formatação - Método FORMAT

formato = 'a={nome1} b={nome2} c={nome3:.2f}'.format(nome1=a, nome2=b, nome3=c)
        # índice                            # Parâmetro nomeado

print(formato)