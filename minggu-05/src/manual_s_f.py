# tabel diformat manual
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # penggunaan 'end' pada baris sebelumnya
    print(repr(x*x*x).rjust(4))

#fungsi str.zfill()  mengisi string numerik di sebelah kiri dengan nol.
'12'.zfill(5)
'-3.14'.zfill(7)
'3.14159265359'.zfill(5)