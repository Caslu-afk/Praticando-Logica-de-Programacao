#Conversão de Temperatura
# Descrição: Leia uma temperatura em graus Celsius e converta-a para Fahrenheit. A fórmula de conversão é: F = (C × 9/5) + 32.
# Fórmula de conversão para Kelvin: K = (C + 273,15)

temperatura = float(input("Digite a Temperatura em Graus Celsius: "))
fahrenheit = (temperatura * 9/5) + 32
kelvin = (temperatura + 273.15)

print(f"A temperatura em Fahrenheit é de: {fah:.2f} °F")
print(f"A temperatura em Kelvin é de: {kel:.2f} K")

