# Solicita ao usuário a temperatura em Fahrenheit e realiza a conversão para Celsius
fahrenheit = float  # Inicializa a variável 'fahrenheit', mas não é necessário, pois ela será definida logo depois
celsius = float  # Inicializa a variável 'celsius', mas também não é necessário

# Obtém a entrada do usuário, que é a temperatura em Fahrenheit, e converte para o tipo float (número decimal)
fahrenheit = float(input('Informe a temperatura em Fahrenheit: '))  # A função input() captura a entrada e float() converte para número decimal

# A fórmula de conversão de Fahrenheit para Celsius é aplicada
celsius = 5 * ((fahrenheit - 32) / 9)  # A fórmula de conversão é (Fahrenheit - 32) * 5 / 9

# Exibe o valor da temperatura convertida em Celsius
print(f'A temperatura em Celsius é {celsius}')  # Exibe o valor de celsius utilizando f-string para formatação da string
