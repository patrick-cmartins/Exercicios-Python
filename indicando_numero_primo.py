# Crie um programa que receba o número nataual n (n>1)
# e exiba uma mensagem indicando se n é primo.
n = int(input('Número: '))
div = 2
while div < n:
    print(f'{n}%{div} = {n%div}')
    if n % div == 0:
        break
    div += 1
if n%div == 0:
    print('Primo')
else:
    print ('Não e primo')
 


