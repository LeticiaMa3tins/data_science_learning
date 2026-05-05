# 1. Importação da biblioteca nativa 'math' para utilizar a função de cálculo fatorial
import math

# 2. Captura do dado com conversão explícita para o tipo inteiro (int)
numero_digitado = int(input("Digite um número inteiro (preferencialmente entre 1 e 10): "))

# 3. Utilização da biblioteca nativa para abstrair o cálculo
resultado_fatorial = math.factorial(numero_digitado)

# 4. Saída formatada exibindo o resultado
print(f"O cálculo fatorial de {numero_digitado} resulta em: {resultado_fatorial}")