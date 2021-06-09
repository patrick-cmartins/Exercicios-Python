i = int(input())
f = int(input())
primos = 0
for a in range(i, f +1):
    if a > 1:
        for b in range(2, a):
            if(a%b)==0:
                break
        else:
            primos += 1
            print(a)
print(f'primos: {primos}')
                
            
