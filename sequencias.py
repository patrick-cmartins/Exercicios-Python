# 1, Crie um programa que solicite ao
# usuario um número natural e exiba a
# sequência crescente de um até o
# numero dado.

n = int(input('Numero: '))
for i in range(1, n+1):
    print(i, end=' ')
