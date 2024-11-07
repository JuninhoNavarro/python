# Faça um Programa que peça dois números e imprima a soma.

# Declaração das variáveis n1 e n2 como tipo float
n1: float
n2: float

# Solicita ao usuário que informe o primeiro número e o converte para float
n1 = float(input("Informe um número: "))

# Solicita ao usuário que informe o segundo número e o converte para float
n2 = float(input("Informe outro número: "))

# Declaração da variável soma como tipo float
soma: float

# Realiza a soma dos dois números informados e armazena o resultado na variável soma
soma = n1 + n2

# Exibe o resultado da soma na tela
print(f'A soma dos números é: {soma}')
