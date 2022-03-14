f = open('workfile', 'w')

f.read()
f.read()

# f.readline()membaca satu baris dari file
f.readline()
f.readline()
f.readline()

# membaca baris dari file
for line in f:
    print(line, end='')
    
# membaca semua baris file dalam daftar
f.write('This is a test\n')

# konversi jenis objek
value = ('the answer', 42)
s = str(value) #ubah tuple menjadi string
f.write(s)


#engubah posisi objek file
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)
f.read(1)
f.seek(-3, 2)
f.read(1)
