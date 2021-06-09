n = 3.14159
raio = float(input())**2
area = n * raio
from decimal import Decimal
c = round(Decimal(area),4)
print(f'A={(c)}')
