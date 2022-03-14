# membulatkan pi dengan 3 angka dibelakang koma
import math
print(f'The value of pi is approximately {math.pi:.3f}.')

# membuat kolom berbaris
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

# mengkonversi nilai sebelum diformat
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')
