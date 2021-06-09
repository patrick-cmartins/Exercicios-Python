n = int(input())
c = 0
if n <= 10:
    while c <= 9:
        c += 1
        print(f'{n} x {c} = {n*c}')
