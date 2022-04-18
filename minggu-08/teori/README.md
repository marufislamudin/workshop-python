# BAB 10 Mencoba Library Standard Python
Sumber : [tutorial python](https://docs.python.org/3/tutorial/stdlib.html)


## 10.1. Operating System Interface

_**nama file program : `10.1.Operating_System.py`**_

Modul `os` berfungsi untuk berinteraksi dengan sistem operasi.

```python
>>> import os
>>> os.getcwd()      # mengembalikan direktori kerja saat ini
'C:\\Users\\HP'
>>> os.chdir('/server/accesslogs')   #mengubah direktori kerja saat ini 
directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0
```

Untuk mendapatkan lokasi direktori kerja saat ini `os.getcwd()` 
Untuk mengubah direktori kerja (CWD) saat ini, metode `os.chdir()` digunakan. Metode ini mengubah CWD ke jalur yang ditentukan. Hanya membutuhkan satu argumen sebagai jalur direktori baru.
Metode `os.makedirs()` dalam Python digunakan untuk membuat direktori secara rekursif. 


 dir()dan help()fungsi berguna sebagai alat bantu interaktif untuk bekerja dengan modul besar seperti os:

```python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module docstrings>
```

`os.dir()` metode di Python digunakan untuk mendapatkan daftar semua file dan direktori di direktori yang ditentukan.
`os.help()` untuk memanggil sistem bantuan bawaan python yang selanjutnya digunakan untuk menampilkan informasi lebih lanjut dari suatu objek (built-in python) yang menjadi argumennya.


Untuk tugas manajemen file dan direktori harian, modul `shutil`  ini menyediakan antarmuka tingkat tinggi yang lebih mudah digunakan:

```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```

fungsi `copyfile()` untuk menyalin file
fungsi `move()` untuk memindahkan file


## 10.2. File Wildcards

_**nama file program : `10.2.File_Wildcard.py`**_

Modul `glob` untuk membuat daftar urutan file dari hasil pencarian pada direktori atau file dalam satu direktori dengan python yang kita gunakan untuk melakukan pencarian,tapi juga bisa mencari dari isi direktori lainnya.
contoh pencarian file dengan format .py :

```python
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```


## 10.3. Command Line Arguments

_**nama file program : `10.3.command_line.py`**_

Atribut `argv` modul  `sys` 
Atribut `argv` memiliki fungsi untuk membuat 'argumen' diluar script masuk menjadi output.

```python
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
```

modul `argpase` untuk melakukan argument processing. Setiap argumen dapat melakukan trigger dengan aksi yang berbeda, dengan mendifinisikan action argumen pada fungsi `add_argument()`. 



## 10.4. Error Output Redirection and Program Termination

_**nama file program : `10.4.Error_output.py`**_

Modul `sys` ini juga memiliki atribut untuk `stdin` , `stdout` , dan `stderr` . Yang terakhir ini berguna untuk memancarkan peringatan dan pesan kesalahan agar terlihat bahkan ketika stdout telah dialihkan

```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```

Cara paling langsung untuk menghentikan skrip adalah dengan menggunakan `sys.exit()`.


## 10.5. String Pattern Matching

_**nama file program : `10.5.String_pattern_Matching.py`**_


modul `re` Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan dioptimalkan

```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```

dengan perintah string sederhana

```python
>>> 'tea for too'.replace('too', 'two')
'tea for two'
```

fungsi `replace()` diatas mengubah kata 'too' menjadi 'two'


## 10.6. Mathematics

_**nama file program : `10.6.Matematika.py`**_

modul `math` digunakan untuk mengakses fungsi matematika dengan nilai float,jadi nilai yang dicetak adalah float.

```python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```

`math.cos()` untuk mengembalikan kosinus pada sumbu x radian.
`math.log()` untuk mengembalikan nilai logaritma


library `random` untuk menghasilkan angka acak.

```python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4
```


`random.choice` menghasilkan secara acak elemen yang dipilih dari sekuens yang tidak kosong atau non-empty.
`random.sample` mengambil nilai sampel secara acak dengan jumlah yang sudah dideklarasikan.
`random.random`  random() maka nilai random yang dihasilkan akan dalam bentuk float.
`random.randrange` angka batas tertinggi tidak akan dimunculkan. 


Modul `statistics` menghitung properti statistik dasar (rata-rata, median, varians, dll.) dari data numerik:

```python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```

`statistics.mean` untuk menghitung rata-rata
`statistics.median` untuk menghitung nilai tengah data
`statistics.variance` untuk menghitung varians / standar deviasi


## 10.7. Internet Access

_**nama file program : `10.7.Internet_Access.py`**_

Modul untuk mengakses internet dan memproses protokol internet.
Dua yang paling sederhana adalah `urllib.request` untuk mengambil data dari URL dan `smtplib` untuk mengirim email

```python
>>> from urllib.request import urlopen
>>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
...     for line in response:
...         line = line.decode()             # Convert bytes to a str
...         if line.startswith('datetime'):
...             print(line.rstrip())         # Remove trailing newline
...
datetime: 2022-04-18T20:20:10.678681+00:00

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('maruf.udin10@gmail.com', 'maruf.islamudin@students.utdi.ac.id',
... """To: maruf.islamudin@students.utdi.ac.id
... From: maruf.udin10@gmail.com
...
... Beware the Ides of March.
... """)
>>> server.quit()
```


## 10.8. Dates and Times

_**nama file program : `10.8.Dates_Times.py`**_


Modul `datetime` untuk memanipulasi tanggal dan waktu dengan cara yang sederhana dan kompleks.
fokus implementasinya adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi keluaran. Modul ini juga mendukung objek dengan zona waktu sesungguhnya.
fungsi date juga mendukung untuk proses aritmatika operasi tanggal dan waktu.

```python
datetime: 2022-04-18T20:20:10.678681+00:00
>>> # format tanggal yang mudah dibuat
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2022, 4, 19)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'04-19-22. 19 Apr 2022 is a Tuesday on the 19 day of April.'
>>>
>>> # tanggal mendukung operasi aritmatika
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
21081
```


## 10.9. Data Compression

_**nama file program : `10.9.Data_Compress.py`**_

Pengarsipan data umum dan format kompresi secara langsung didukung oleh modul `zlib`, `gzip`, `bz2`, `lzma`, `zipfile` dan `tarfile`.

```python
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```


## 10.10. Performance Measurement

_**nama file program : `10.10.Performance.py`**_

 Python mengembangkan minat yang mendalam untuk mengetahui kinerja relatif dari pendekatan yang berbeda untuk masalah yang sama. 
Misalnya, mungkin tergoda untuk menggunakan fitur pengepakan dan pembongkaran Tuple alih-alih pendekatan tradisional untuk bertukar argumen. Modul timeit dengan cepat menunjukkan keunggulan kinerja sederhana

```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.22210579994134605
>>>
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.16389649990014732
```

Berbeda dengan `timeit` tingkat granularitas yang bagus, modul `profile` dan `pstats` menyediakan alat untuk mengidentifikasi bagian kritis waktu dalam blok kode yang lebih besar.


## 10.11. Quality Control

_**nama file program : `10.11.quality_control.py`**_

Salah satu pendekatan untuk mengembangkan perangkat lunak berkualitas tinggi adalah dengan menulis tes untuk setiap fungsi saat dikembangkan dan menjalankan tes tersebut sesering mungkin selama proses pengembangan.

Modul `doctest()` menyediakan alat untuk memindai modul dan memvalidasi tes yang tertanam dalam dokumen program. Konstruksi pengujian sesederhana memotong dan menempelkan panggilan biasa beserta hasilnya ke dalam docstring.


```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()
```

Modul `unittest` memungkinkan serangkaian pengujian yang lebih komprehensif untuk dipertahankan dalam file terpisah

```python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()
```


## 10.12. Batteries Included

Python memiliki filosofi "termasuk baterai". Ini paling baik dilihat melalui kemampuan canggih dan kuat dari paket-paketnya yang lebih besar. Sebagai contoh:

* Modul `xmlrpc.client` dan `xmlrpc.server` membuat penerapan panggilan prosedur jarak jauh menjadi tugas yang hampir sepele. Terlepas dari nama modul, tidak ada pengetahuan langsung atau penanganan XML yang diperlukan.

* Paket `email` adalah perpustakaan untuk mengelola pesan email, termasuk MIME dan lainnyaDokumen pesan berbasis RFC **2822** . Tidak seperti `smtplib` dan `poplib` yang benar-benar mengirim dan menerima pesan, paket email memiliki perangkat lengkap untuk membangun atau mendekode struktur pesan yang kompleks (termasuk lampiran) dan untuk menerapkan pengkodean internet dan protokol header.

* Paket ini `json` menyediakan dukungan kuat untuk menguraikan format pertukaran data populer ini. Modul ini `csv` mendukung pembacaan dan penulisan file secara langsung dalam format Comma-Separated Value, umumnya didukung oleh database dan spreadsheet. Pemrosesan XML didukung oleh `xml.etree.ElementTree`, `xml.dom` dan `xml.sax`. Bersama-sama, modul dan paket ini sangat menyederhanakan pertukaran data antara aplikasi Python dan alat lainnya.

* Modul `sqlite3` ini adalah pembungkus untuk pustaka database SQLite, menyediakan database persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL yang sedikit tidak standar.

* Internasionalisasi didukung oleh sejumlah modul termasuk `gettext`, `locale`, dan `codecs`.



# BAB 11 Mencoba Library Standard Python
Sumber : [tutorial python](https://docs.python.org/3/tutorial/stdlib.html)