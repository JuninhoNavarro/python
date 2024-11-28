# Solicita ao usuário o valor recebido por hora de trabalho
valor_hora = float  # A variável é inicializada, mas não é necessário, pois ela será definida depois
valor_hora = float(input('informe o valor recebido por hora: '))  # Converte a entrada do usuário para um número decimal (float) e armazena em valor_hora

# Solicita ao usuário o número de horas trabalhadas no mês
numero_hora = float  # A variável é inicializada, mas também será definida posteriormente
numero_hora = float(input('informe o numero de horas trabalhadas no mês: '))  # Converte a entrada do usuário para float e armazena em numero_hora

# Calcula o salário mensal multiplicando o valor da hora pelo número de horas trabalhadas
salario = float  # A variável é inicializada, mas não é necessário, pois ela será definida logo abaixo
salario = valor_hora * numero_hora  # Calcula o salário mensal e armazena o resultado em salario

# Exibe o valor do salário calculado, utilizando a formatação de string para incluir o valor de salario na mensagem
print(f'seu salario é {salario}')  # Exibe o salário calculado para o usuário
