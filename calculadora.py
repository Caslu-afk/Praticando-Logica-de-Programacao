#calculadora 

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
operacao = input("Digite a operação desejada: ")

match operacao:
    case "+":
        resultado = n1 + n2
    case "-":
        resultado = n1 - n2
    case "*":
        resultado = n1 * n2
    case "/":
        resultado = n1 / n2
    
print(f"O resultado da sua conta é {resultado}")