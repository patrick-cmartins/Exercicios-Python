vlr_tl = int(input())
parc = int(input())
pagamento = 0

while vlr_tl >= 0:
    for i in range(vlr_tl, 0, -parc):
        pagamento = pagamento + 1
        print(f'pagamento: {pagamento}')
        print(f'antes = {i}')
        if i-parc <= 0:
            print(f'depois = 0')
            print('-'*5)
        else:
            print(f'depois = {i-parc}')
            print('-'*5)
    break
    
          
