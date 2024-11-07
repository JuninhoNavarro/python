# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# Declaração das variáveis n1, n2, n3 e n4 como tipo float
n1: float
n2: float
n3: float
n4: float

# Solicita ao usuário que informe a Nota do 1° Bimestre e converte para float
n1 = float(input('Informe a Nota do 1° Bimestre: '))

# Solicita ao usuário que informe a Nota do 2° Bimestre e converte para float
n2 = float(input('Informe a Nota do 2° Bimestre: '))

# Solicita ao usuário que informe a Nota do 3° Bimestre e converte para float
n3 = float(input('Informe a Nota do 3° Bimestre: '))

# Solicita ao usuário que informe a Nota do 4° Bimestre e converte para float
n4 = float(input('Informe a Nota do 4° Bimestre: '))

# Declara a variável media como tipo float
media: float 

# Calcula a média das quatro notas. A soma das notas é dividida por 4.
media = (n1 + n2 + n3 + n4) / 4

# Exibe o resultado da média do aluno
print(f'A Média do aluno X é {media}.')
