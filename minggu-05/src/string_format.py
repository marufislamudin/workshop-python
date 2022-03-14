# str.format()
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# angka di dalam kurung dapat merujuk ke posisi objek 
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

# merujuk nilai dengan argumen kata kunci
print('This {food} is {adjective}.'.format(
    food='spam', adjective='absolutely horrible'))

#posisi argumen dan key dapat digabungkan
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

# menggunakan tanda [] untuk mengakses kunci
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d};'
    'Dcab: {0[Dcab]:d}'.format(table))

# meneruskan tabel sebagai kata kunci dengan notasi **
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# contoh baris & kolom
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


