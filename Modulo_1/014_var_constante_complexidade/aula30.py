"""
Constante = "Variáveis" que não vão mudar

Muitas condições no mesmo if = ruim
    < - Contagem de complexidade (ruim) (Afastado da margem)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 90 # local em que o carro está na estrada

# Usamos letras maiúsculas para definir constantes 
RADAR_1 = 60 # velocidade máxima do radar
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_passou_radar_1 and vel_carro_pass_radar_1:
    print('Carro multado em radar 1')


""" 
FORMA RUIM

if velocidade > RADAR_1:
    print('Você ultrapassou o limite de velocidade')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
        local_carro<= (LOCAL_1 + RADAR_RANGE) and \
            velocidade > RADAR_1:
    print('Carro multado no radar 1') # dá para utilizar a barra inversa para "pular" a linha
"""