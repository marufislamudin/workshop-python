# BAB 7 INPUT OUTPUT
Sumber : [tutorial python](https://docs.python.org/3/tutorial/inputoutput.html)

Terdapat beberapa cara untuk menampilkan output dari suatu program. Data dapat dicetak dalam bentuk yang dapat dibaca manusia, atau ditulis ke file untuk digunakan di masa mendatang.


## 7.1 Format Output

_**nama file program : `fancier.py`**_

selain 2 cara untuk menulis nilai yang telah dibahas bab-bab sebelumnya ( *pernyataan ekspresi* dan fungsi `print()` ). Cara ke 3 ini akan menggunakan metode `write()` objek file. File keluaran standar dapat dirujuk sebagai `sys.stdout`.

Beberapa cara memformat output :
* menggunakan formatted string literals. dimulai dstring dengan `f` di dalamnya dapat dituliskan ekspresi Python di dalam tanda kurung kurawa `{}`. berisi karakter yang dapat merujuk ke variabel / nilai.

```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```

format menampilkan string mulai *f* kemudian memanggil nilai variabel dengan nama variabel yang berada pada dalam kurung kurawa *{}*.

* metode `str.format()`
Pada metode ini menggunakan kurung urawa `{}` untuk menandai di mana variabel akan diganti dan dapat memberikan arahan pemformatan terperinci. pernyataan disertai juga informasi yang akan diformat.

```python
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
```

* Melakukan semua penanganan string sendiri dengan menggunakan operasi pengirisan string dan penggabungan.  Tipe string memiliki beberapa metode yang melakukan operasi yang berguna untuk mengisi string ke lebar kolom tertentu.


**Fungsi `repr()` dan `str()` untuk mengkonversi nilai apapun menjadi string**
Fungsi `str()` untuk mengembalikan representasi nilai yang dapat dibaca.
Fungsi `repr()` untuk menghasilkan representasi yang dapat dibaca oleh interpreter. 
Untuk objek yang tidak memiliki representasi khusus untuk dapat dibaca manusia, `str()` akan mengembalikan nilai yang sama dengan `repr()`.

contoh :

```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # repr() menambahkan tanda kutip string garis miring terbalik 
>>> hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # argumen repr() dapat berupa objek python apapun
>>> repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```

Modul **string** berisi *Template* kelas yang menawarkan cara lain untuk mengganti nilai menjadi string, menggunakan placeholder seperti $xdan menggantinya dengan nilai dari kamus.

### 7.1.1. Formatted String Literals

_**nama file program : `Formatted_String_Literals.py`**_

Formatted String Literals (f-string) memungkinkan untuk memasukkan nilai ekspresi Python di dalam string dengan mengawali string dengan `f` atau `F` dan menulis ekspresi sebagai `{expression}`.

Penentu format opsional dapat mengikuti ekspresi memungkinkan kontrol yang lebih besar atas bagaimana nilai diformat.
Contoh membulatkan pi ke dalam tiga angka setelah koma :

```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```

Nilai pi yang beraada dalam library math ditampilkan dengan format 3 angka di belakan g koma. Maka nilai yang ditampilkan adalah 3.142.

Membuat kolom berbaris

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```

penulisan perintah pernyataan untuk ditampilkan antar kolom dipisahkan dengan tanda `:`. Perintah for akan mendefinisikan nilai pada table, pernyataan di depan tanda `:` sebagai **name** dan pernyataan di belakang tanda `:` sebagai **phone**. 

Menkonversi nilai sebelum diformat
`!a` berlaku sebagai `ascii()`
`!s` berlaku sebagai `str()`
`!r` berlaku sebagai `repr()`

contoh :

```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```
karena fungsi repr() yang tertulis `!r` menghasilkan representasi yang dapat dibaca oleh interpreter maka akan tetap menampilkan **'eels'**


### 7.1.2 The String format() Method

_**nama file program : `string_format.py`**_

Penggunaan dasar `str.format()`

```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

Tanda kurung dan karakter di dalamnya (disebut bidang format) diganti dengan objek yang diteruskan ke metode `str.format()`.
Angka dalam kurung dapat digunakan untuk merujuk ke posisi objek yang dilewatkan ke dalam metode `str.format()`.

```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

pada posisi objek diatas, `format('spam', 'eggs')` *spam* menempati posisi 0; *eggs* menempati posisi 1. 
Maka pada saat pemanggilan ke dua `print('{1} and {0}'` yang ditampilkan awal nilai pada posisi 1 yaitu *eggs*, kemudian nilai pada posisi ke-0 yaitu *spam*.


Jika argumen kata kunci digunakan dalam metode `str.format()`, nilainya dirujuk dengan menggunakan nama argumen.

```python
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
...
This spam is absolutely horrible.
```

perintah ini mendeklarasikan kata kunci
`format(food='spam', adjective='absolutely horrible')`
maka jika memanggil dengan key *food* akan menampilkan **spam**
jika memanggil dengan key *adjective* akan menampilkan **adjective**

Argumen posisi dan kata kunci dapat digabungkan secara sewenang-wenang:

```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
The story of Bill, Manfred, and Georg.
```

deklarasi format di atas
`format('Bill', 'Manfred', other='Georg')`
posisi 0 => Bill
posisi 1 => Manfred
key other => Georg


jika memiliki format string yang panjang dan tidak dipisahkan, dapat dengan  mereferensikan variabel yang akan diformat berdasarkan nama alih-alih berdasarkan posisi.
Dapat dilakukan hanya dengan melewatkan *dict* dan menggunakan tanda kurung siku `[]` untuk mengakses kunci.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
...
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

Meneruskan tabel sebagai argumen kata kunci dengan notasi `**`.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

contoh, baris berikut menghasilkan kumpulan kolom yang tersusun rapi yang memberikan bilangan bulat dan kuadrat serta kubusnya :

```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

### 7.1.3. Manual String Formatting

_**nama file program : `manual_s_f.py`**_

Tabel kotak dan kubus yang sama dengan program diatas, diformat secara manual:

```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note 
...		# penggunaan 'end' pada baris sebelumnya
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

Metode `str.rjust()` objek string membenarkan string di bidang dengan lebar tertentu dengan mengisinya dengan spasi di sebelah kiri.
Metode serupa :
* `str.ljust()`
* `str.center()` 

Metode ini tidak menulis apa pun, hanya mengembalikan string baru. Jika string input terlalu panjang, tidak akan memotongnya, dan mengembalikannya sama persis.
Kelemahan metode ini akan mengacaukan tata letak kolom.
Jika akan memotong string dapa menggunakan operasi irisan `x.ljust(n)[:n]` untuk memperpendek string.


Metode `str.zfill()` untuk mengisi string numerik di sebelah kiri dengan nol

```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```

### 7.1.4. Old string formatting

_**nama file program : `old_s_f.py`**_

Operator **%** (modulo) juga dapat digunakan untuk pemformatan string. Operasi ini biasa disebut dengan interpolasi string. Sebagai contoh: `'string' % values%stringvalues`

```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```


## 7.2. Reading and Writing Files

_**nama file program : `read_writing.py`**_

Fungsi `open()` untuk mengembalikan objek file.
argumen yang sering digunakan yaitu `open(filename, mode)`

```python
>>> f = open('workfile', 'w')
```

Argumen pertama adalah string yang berisi nama file. 
Argumen kedua adalah string lain yang berisi beberapa karakter yang menjelaskan cara file akan digunakan.

* `r` hanya akan membaca file
* `w` hanya menulis (file yang ada dengan nama yang sama akan dihapus)
* `a` membuka file untuk ditambahkan; setiap data yang ditulis ke file secara otomatis ditambahkan ke akhir.
* `r+` membuka file untuk membaca dan menulis
* `b` membuka file dalam mode biner, data dibaca dan ditulis dalam bentuk objek byte


Praktik menggunakan `with` keyword objek file
dengan metode ini  file dapat ditutup dengan benar setelah rangkaiannya selesai.
Menggunakan `with` juga jauh lebih pendek daripada menulis yang setara `try- finally` blok:

```python
>>> with open('workfile') as f:
...     read_data = f.read()

>>> # memeriksa apakah file telah ditutup secara otomatis
>>> f.closed
True
```

Jika tidak menggunakan `with` keyword, maka harus memanggil `f.close()` untuk menutup file dan segera menutup data/file yang sedang di proses. 

**Peringatan**
```
 Memanggil f.write()tanpa menggunakan with keyword atau panggilan f.close() dapat mengakibatkan argumen f.write()tidak sepenuhnya ditulis ke disk, bahkan jika program berhasil keluar.
```

Setelah objek file ditutup, baik dengan pernyataan `with` atau dengan memanggil `f.close()`, upaya untuk menggunakan objek file secara otomatis akan gagal.

```python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

### 7.2.1. Methods of File Objects

_**nama file program : `file_objects.py`**_

Untuk membaca konten file dengan memanggil fungsi `f.read(size)`, maka akan membaca sejumlah data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner). 
*Size* adalah argumen numerik opsional. 
Ketika ukuran dihilangkan atau negatif, seluruh isi file akan dibaca dan dikembalikan.

Jika akhir file telah tercapai, `f.read()` akan mengembalikan string kosong **( '')**.

```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```

`f.readline()` membaca satu baris dari file.
karakter baris baru ( \n) ditinggalkan di akhir string dan hanya dihilangkan pada baris terakhir file jika file tidak diakhiri dengan baris baru. 
Jika `f.readline()` mengembalikan string kosong, akhir file telah tercapai, sedangkan baris kosong diwakili oleh **'\n'**, string yang hanya berisi satu baris baru.

```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```

Untuk membaca baris dari file, dapat dengan cara mengulang objek file.

```python
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
```


Menggunakan `list(f)` atau `f.readlines()` untuk  membaca semua baris file dalam daftar.
`f.write(string)` akan menulis isi string ke file, mengembalikan jumlah karakter yang ditulis.

```python
>>> f.write('This is a test\n')
15
```

Mengkonversi menjadi string (dalam mode teks) atau objek byte (dalam mode biner) sebelum ditampilkan

```python
>>> value = ('the answer', 42)
>>> s = str(value)  # ubah tuple menjadi string
>>> f.write(s)
18
```

`f.tell()` akan mengembalikan bilangan bulat yang memberikan posisi objek file saat ini dalam file yang direpresentasikan sebagai jumlah byte dari awal file saat dalam mode biner dan angka buram saat dalam mode teks.

Untuk mengubah posisi objek dapat menggunakan `fseek()`
* Posisi dihitung dari penambahan offset ke titik referensi
* Titik referensi dipilih menggunakan pernyataan *where*
* Nilai 0 mengukur dari awal file
* 1 menggunakan posisi file saat ini
* 2 menggunakan akhir file sebagai titik referensi

perintah menggunakan file awal sebagai titik referensi adalah `f.seek(offset, whence)`

```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```

### 7.2.2. Saving structured data with json

_**nama file program : `struktur_data_json.py`**_

String dapat dengan mudah ditulis dan dibaca dari sebuah file.
Angka membutuhkan sedikit lebih banyak usaha, karena metode *read()* hanya mengembalikan string, yang harus diteruskan ke fungsi seperti int(), yang mengambil seperti string '123' dan mengembalikan nilai numeriknya 123.

Python memungkinkan untuk menggunakan format pertukaran data populer yang disebut JSON (JavaScript Object Notation). 
Modul standar yang dipanggil `json` dapat mengambil hierarki data Python, dan mengubahnya menjadi representasi string. Proses ini disebut serialisasi.
Merekonstruksi data dari representasi string disebut deserializing. 
Antara serialisasi dan deserializing, string yang mewakili objek mungkin telah disimpan dalam file atau data, atau dikirim melalui koneksi jaringan ke beberapa mesin yang jauh.

misal objek x, untuk melihat representasi string JSON dengan sebaris kode sederhana:

```python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```

Varian lain dari fungsi `dumps()`, yang disebut `dump()`, hanya membuat serial objek ke file teks. 
Jadi jika objek `f` file teks dibuka untuk ditulis, dapat dengan perintah

```python
json.dump(x, f)
```

jika `f` adalah objek file teks yang telah dibuka untuk dibaca, Untuk memecahkan kode objek dengan perintah

```python
x = json.load(f)
```

Teknik serialisasi sederhana ini dapat menangani daftar dan kamus, tetapi membuat serialisasi instance kelas arbitrer di JSON membutuhkan sedikit usaha ekstra.