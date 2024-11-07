# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

# Declaração das variáveis lado, area e dobro como tipo floatt
lado = float
area = float
dobro = float

# Solicita ao usuário que informe o valor do lado do quadrado e converte para float
lado = float(input('Informe o valor do lado do quadrado: '))

# Calcula a área do quadrado. A fórmula para a área de um quadrado é A = lado²
area = lado * lado

# Calcula o dobro da área do quadrado
dobro = 2 * area

# Exibe o resultado da área e o dobro da área, formatando os valores de lado, área e dobro
print(f'A área do quadrado de lado {lado} é de {area} e o dobro dela é {dobro}')
