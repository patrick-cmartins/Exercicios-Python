# Crie um programa que receba o numero
# n >= 0 e exiba o valor da raiz quadrada
# de n. Enquanto n for um número negativo,
# repita a solicitação de entrada.
from math import sqrt
while True:
    n = float(input('Numero: '))
    if n >= 0: break
    
print(f'Raiz quadrada de {n} é {sqrt(n):.2f}')
