# Variaveis
numero1 = 5
numero2 = 10
numero3 = 34
numero4 = 7
frase = "uma frase simples qualquer."
palavra = "papagaio"

# Media Aritmetica
media = (numero1 + numero2 + numero3 + numero4) / 4

# Quadrado do Terceiro Numero
quadrado_numero3 = numero3 ** 2

# Dobro do Quarto numero
dobro_numero4 = 2 * numero4

# Quantidade de Letra na Palavra
quantidade_letras_palavra = len(palavra)

# Quantidade de Espacos na Frase
quantidade_espacos_frase = frase.count(" ")

# Verifica se o Primeiro Numero eh Maior que o Segundo
primeiro_maior_segundo = numero1 > numero2

# Encontra o Maior Numero Entre os Quatro
maior_numero = max(numero1, numero2, numero3, numero4)

# Imprime os Resultados
print(f"media aritmetica: {media:.2f}")
print(f"Quadrado do terceiro numero: {quadrado_numero3}")
print(f"Dobro do quarto numero: {dobro_numero4}")
print(f"Quantidade de letras na palavra: {quantidade_letras_palavra}")
print(f"Quantidade de espacos em branco na frase: {quantidade_espacos_frase}")
print(f"O primeiro numero eh maior que o segundo? {primeiro_maior_segundo}")
print(f"O maior numero eh: {maior_numero}")