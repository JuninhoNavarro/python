#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu 
# trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do 
# estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você 
# faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso
#  a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima 
# os dados do programa com as mensagens adequadas.

# Inicializa as variáveis como tipo float, mas a inicialização não é necessária aqui, pois os valores serão atribuídos mais tarde
peso = float  # Variável para armazenar o peso do peixe em quilos
peso_excedido = float  # Variável para armazenar a quantidade de quilos excedentes
multa = float  # Variável para armazenar o valor da multa a ser paga

# Solicita ao usuário o peso do peixe e converte a entrada para float (número decimal)
peso = float(input('Informe o peso do peixe: '))  # O valor informado pelo usuário é convertido para float e armazenado em 'peso'

# Calcula o peso excedente, que é a diferença entre o peso informado e o limite de 50 quilos
peso_excedido = peso - 50  # Se o peso for maior que 50, 'peso_excedido' será a diferença entre o peso e 50

# Se o peso for menor ou igual a 50 quilos, não há multa
if peso <= 50:
    print('Não excedeu o peso')  # Exibe uma mensagem informando que o peso não excedeu o limite

# Se o peso for maior que 50 quilos, calcula o excesso e a multa
elif peso > 50:
    multa = peso_excedido * 4  # A multa é calculada multiplicando o excesso de peso por R$ 4,00 por quilo
    # Exibe a quantidade de quilos excedentes e o valor da multa
    print(f'Excedeu {peso_excedido} quilos, a multa é de R$ {multa:.2f}')  # O valor da multa é exibido com 2 casas decimais

# Caso o valor de peso seja inválido (o que não ocorre com a lógica atual), um erro seria exibido
else:
    print('Erro')  # Essa linha nunca será executada, pois todas as condições estão cobertas acima
