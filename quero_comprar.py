# Crie um programa que peça ao usuário
# preços de produtos comprados até que
# ele decida encerrar a compra.
# O programa, ao final, deve exibir o
# total gasto.

total = 0
quero_comprar = True

while quero_comprar:
    preco = float(input('Preço: '))
    total += preco
    opcao = input('Continuar comprando (s/n)? ')
    if opcao != 's':
        quero_comprar = False
print(f'Total da compra R$ {total:.2f}')
