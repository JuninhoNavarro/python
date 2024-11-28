# O algoritmo calcula o peso ideal de uma pessoa com base na sua altura e sexo

# Solicita ao usuário para informar o sexo. O valor inserido deve ser 'M' (masculino) ou 'F' (feminino).
# O valor é armazenado na variável 'sexo', que será uma string.
sexo = str(input('Informe o sexo (M ou F): '))  # A função input() captura a entrada do usuário e converte para string.

# Solicita ao usuário para informar sua altura. A altura é convertida para um número decimal (float).
altura = float(input('Informe a sua altura: '))  # Converte a entrada para float para realizar cálculos.

# Inicializa a variável peso_ideal como um tipo float. Essa variável vai armazenar o resultado do cálculo do peso ideal.
peso_ideal = float  # A inicialização aqui não é necessária, já que o valor será atribuído mais tarde.

# Condicional para verificar o sexo informado
# Se o sexo for 'm' (masculino), o programa aplica a fórmula para calcular o peso ideal de homens.
if sexo == "m":
    # Calcula o peso ideal para homens com a fórmula: (72.7 * altura) - 58
    peso_ideal = (72.7 * altura) - 58
    # Exibe o peso ideal calculado para o usuário
    print(f'Seu peso ideal é {peso_ideal:.2f}')  # Formata o resultado para exibir 2 casas decimais.
else:
    # Caso contrário, o sexo é feminino, e a fórmula para mulheres é aplicada.
    # Calcula o peso ideal para mulheres com a fórmula: (62.1 * altura) - 44.7
    peso_ideal = (62.1 * altura) - 44.7
    # Exibe o peso ideal calculado para o usuário
    print(f'Seu peso ideal é {peso_ideal:.2f}')  # Formata o resultado para exibir 2 casas decimais.
