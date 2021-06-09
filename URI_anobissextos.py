ano_ini = int(input())
ano_fim = int(input())
bissextos = 0

for a in range(ano_ini, ano_fim+1,):
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        bissextos += 1
        print(a)
        
print(f'bissextos: {bissextos}')
    
