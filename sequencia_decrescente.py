# 3, Crie um programa que solicite ao
# usuario um numero natural e exiba a
# sequencia decrescente do numero dado
# até um.

n = int(input())
for i in range(n, 0, -1):
    print(i, end=' ')
