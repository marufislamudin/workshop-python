# open()mengembalikan objek file
f = open('workfile', 'w')

# menggunakan with
with open('workfile') as f:
    read_data = f.read()
# memeriksa apakah file telah ditutup secara otomatis
f.closed

# Setelah objek file ditutup, upaya untuk menggunakan objek file secara otomatis akan gagal
f.close()
f.read()
