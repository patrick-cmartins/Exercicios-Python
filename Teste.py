valor = float(input('Valor do item: '))
qtd = int(input('Quantidade: '))
total = valor * qtd
desconto = total * 0.10
total_final = total - desconto
print(f'Total com desconto: R${total_final:.2f}')
 
