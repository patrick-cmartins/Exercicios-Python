total = 0
vic_coin = True

while vic_coin:
    doacao = float(input())
    total += doacao
    
    if doacao == -1:
        total += 1
        vic_coin = False
print(f'VC$ {total:.2f}')
print(f'R$ {total*2.5:.2f}')

