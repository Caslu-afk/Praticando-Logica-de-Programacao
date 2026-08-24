# Algoritmo que leia a largura e altura de uma parede, calcule e mostre a area ser pintada
# Mostre a quantidade de tinta necessaria para fazer o serviço 
# Cada litro de tinta, pinta uma area de 2m quadrados 


# ENTRADA DE DADOS
largura = float(input("Digite a Largura: "))
altura = float(input("Digite a Altura: "))

# PROCESSAMENTO DE DADOS
def parede(largura, altura): # Função para definir o valor da área
    area = largura * altura
    return area

area = parede(largura, altura)


def pintar(area): # função para definir a quantidade de tinta com base no resultado da área
    pintura = area / 2
    return pintura

tinta = pintar(area)

# SAÍDA DOS RESULTADOS   
print(f"A parede possui uma área total de {area:.2f} m².")
print(f"Para pintar uma parede com essas medidas, serão necessários aproximadamente {tinta:.2f} litros de tinta.")

