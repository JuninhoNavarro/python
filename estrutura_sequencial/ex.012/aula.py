#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
#  ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta 
# é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta 
# a serem compradas e o preço total.

# Solicita ao usuário a quantidade de metros quadrados da área a ser pintada
metros = float(input('Informe o tamanho em metros quadrados da área a ser pintada: '))  # O valor inserido é convertido para float

# Calcula a quantidade de litros de tinta necessária para cobrir a área
litros = metros / 3  # A cobertura é de 1 litro para cada 3 metros quadrados

# Calcula a quantidade de latas de tinta necessárias, considerando que cada lata tem 18 litros
latas = int(litros / 18)  # Dividimos os litros por 18 e usamos int() para arredondar para baixo

# Se a divisão dos litros por 18 não for exata (resto diferente de 0), significa que há sobra de tinta necessária
if litros % 18 != 0:
    latas += 1  # Se houver sobra, precisamos de mais uma lata

# Exibe a quantidade de latas a serem compradas e o valor total da compra
print(f'Você deverá comprar {latas} latas, e o valor total é R$ {latas * 80}')  # O preço de cada lata é R$ 80,00
