import math

print('--- Motor de IA: Calculadora Vetorial ---')

# Pegando as coordenadas do texto do usuário (Vetor 1)
print("Vetor da Pergunta (ex: 2 e 3):")
x1 = float(input("Coordenada X1: "))
y1 = float(input("Coordenada Y1: "))

# Pegando as coordenadas do Banco de Dados (Vetor 2)
print("\nVetor do Banco de Dados (ex: 5 e 7):")
x2 = float(input("Coordenada X2: "))
y2 = float(input("Coordenada Y2: "))

# O coração do RAG: Calculando a Distância Euclidiana
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f'\nA Distância Euclidiana entre os vetores é: {distancia:.2f}')