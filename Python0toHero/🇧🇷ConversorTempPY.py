# 1- o programa deve solicitar ao usuário que insira uma temperatura em graus Celsius.
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
# 2- o programa deve converter a temperatura de Celsius para Fahrenheit usando a fórmula: F = (C * 1.8) + 32.
temperatura_fahrenheit = (temperatura_celsius * 1.8) + 32
# 3- o programa deve exibir a temperatura convertida em Fahrenheit. 
print(f"A temperatura convertida é: {temperatura_fahrenheit:.2f}°F")
