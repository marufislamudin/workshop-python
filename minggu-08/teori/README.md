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




# BAB 11 Mencoba Library Standard Python Bagian 2
Sumber : [tutorial python](https://docs.python.org/3/tutorial/stdlib2.html)

Pada Bagian ii mencoba modul yang lebih canggih, yanng mendukung pemrograman profesional.

## 11.1. Output Formatting

_**nama file program : `11.1.Output_Formating.py`**_

Modul `reprlib` menyediakan versi yang `repr()` disesuaikan untuk tampilan singkat wadah besar atau bersarang dalam

```python
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```

Modul pprintini menawarkan kontrol yang lebih canggih atas pencetakan objek bawaan dan objek yang ditentukan pengguna dengan cara yang dapat dibaca oleh penerjemah. Ketika hasilnya lebih panjang dari satu baris, "printer cantik" menambahkan jeda baris dan lekukan untuk mengungkapkan struktur data dengan lebih jelas:

```python
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
...     'yellow'], 'blue']]]
...
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
```


Modul textwrapmemformat paragraf teks agar sesuai dengan lebar layar yang diberikan:

```python
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
...
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```

Modul ini localemengakses database format data spesifik budaya. Atribut pengelompokan fungsi format lokal menyediakan cara langsung untuk memformat angka dengan pemisah grup:

```python
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv()
>>> x = 1234567.8
>>> locale.format("%d", x, grouping=True)
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
...                      conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
```

## 11.2. Templating

_**nama file program : `11.2.Template.py`**_

Modul ini `string` mencakup kelas serbaguna `Template` dengan sintaks yang disederhanakan yang cocok untuk diedit oleh pengguna akhir.

Formatnya menggunakan nama placeholder yang dibentuk $dengan pengidentifikasi Python yang valid (karakter alfanumerik dan garis bawah). Mengelilingi placeholder dengan kurung memungkinkan untuk diikuti oleh lebih banyak huruf alfanumerik tanpa spasi. Menulis $$membuat satu pelarian $:

```python
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```

Metode `substitute()` memunculkan a `KeyError` ketika placeholder tidak disediakan dalam kamus atau argumen kata kunci. Untuk aplikasi gaya gabungan surat, data yang diberikan pengguna mungkin tidak lengkap dan `safe_substitute()` metodenya mungkin lebih tepat — ini akan membuat placeholder tidak berubah jika data tidak ada:

```python
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  ...
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'
```


Subkelas template dapat menentukan pembatas kustom. Misalnya, utilitas penggantian nama batch untuk browser foto dapat memilih untuk menggunakan tanda persen untuk placeholder seperti tanggal saat ini, nomor urut gambar, atau format file:

```python
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
...     delimiter = '%'
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
...     base, ext = os.path.splitext(filename)
...     newname = t.substitute(d=date, n=i, f=ext)
...     print('{0} --> {1}'.format(filename, newname))

img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
```

## 11.3. Working with Binary Data Record Layouts

_**nama file program : `11.3.Binary_data_record.py`**_

Modul `struct` menyediakan `pack()` dan `unpack()` berfungsi untuk bekerja dengan format record biner dengan panjang variabel. 

Contoh berikut menunjukkan cara mengulang informasi header dalam file ZIP tanpa menggunakan zipfilemodul. Kemas kode `"H"` dan `"I"` mewakili dua dan empat byte nomor unsigned masing-masing. Ini "<"menunjukkan bahwa mereka adalah ukuran standar dan dalam urutan byte little-endian:

```python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size
```

## 11.4. Multi-threading

_**nama file program : `11.4.Multi_threading.py`**_

Threading adalah teknik untuk memisahkan tugas yang tidak bergantung secara berurutan. Utas dapat digunakan untuk meningkatkan daya tanggap aplikasi yang menerima masukan pengguna saat tugas lain berjalan di latar belakang. Kasus penggunaan terkait menjalankan I/O secara paralel dengan perhitungan di utas lain.

Kode berikut menunjukkan bagaimana threadingmodul tingkat tinggi dapat menjalankan tugas di latar belakang sementara program utama terus berjalan:

```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```


## 11.5. Logging

_**nama file program : `11.5.Logging.py`**_


Modul `logging` ini menawarkan sistem `logging` berfitur lengkap dan fleksibel. Paling sederhana, pesan log dikirim ke file atau ke `sys.stderr` :

```python
>>> import logging
>>> logging.debug('Debugging information')
>>> logging.info('Informational message')
>>> logging.warning('Warning:config file %s not found', 'server.conf')
WARNING:root:Warning:config file server.conf not found
>>> logging.error('Error occurred')
ERROR:root:Error occurred
>>> logging.critical('Critical error -- shutting down')
CRITICAL:root:Critical error -- shutting down
>>>
```

Secara default, pesan informasi dan debugging ditekan dan output dikirim ke kesalahan standar. Opsi keluaran lainnya termasuk perutean pesan melalui email, datagram, soket, atau ke Server HTTP. Filter baru dapat memilih perutean yang berbeda berdasarkan prioritas pesan: `DEBUG`, `INFO`, `WARNING`, `ERROR`, dan `CRITICAL`.

## 11.6. Weak References

_**nama file program : `11.6.Weak_References.py`**_


Modul `weakref` menyediakan alat untuk melacak objek tanpa membuat referensi. Ketika objek tidak lagi diperlukan, objek tersebut secara otomatis dihapus dari tabel referensi lemah dan panggilan balik dipicu untuk objek referensi lemah. Aplikasi umum termasuk objek caching yang mahal untuk dibuat:

```python
>>> import weakref, gc
>>> class A:
...     def __init__(self, value):
...         self.value = value
...     def __repr__(self):
...         return str(self.value)
...
>>> a = A(10)                   # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a            # does not create a reference
>>> d['primary']                # fetch the object if it is still alive
10
>>> del a                       # remove the one reference
>>> gc.collect()                # run garbage collection right away
0
>>> d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entry was automatically removed
  File "C:/python310/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```

## 11.7. Tools for Working with Lists

_**nama file program : `11.7.Tools_for_working.py`**_

Modul `array` menyediakan `array()` objek yang seperti daftar yang hanya menyimpan data homogen dan menyimpannya lebih kompak. Contoh berikut menunjukkan larik angka yang disimpan sebagai dua byte angka biner tidak bertanda (typecode "H") daripada 16 byte biasa per entri untuk daftar reguler objek int Python:

```python
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
```


Modul ini `collections` menyediakan `deque()` objek yang seperti daftar dengan penambahan dan kemunculan yang lebih cepat dari sisi kiri tetapi pencarian yang lebih lambat di tengah. Objek-objek ini sangat cocok untuk mengimplementasikan antrian dan pencarian pohon pertama yang luas:

```python
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1
```

```python
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
```

modul `bisect`  untuk memanipulasi daftar yang diurutkan

```python
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
```

Modul `heapq`  untuk mengimplementasikan heap berdasarkan daftar reguler. Entri bernilai terendah selalu disimpan di posisi nol. Ini berguna untuk aplikasi yang berulang kali mengakses elemen terkecil tetapi tidak ingin menjalankan pengurutan daftar lengkap:

```python
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)                     
>>> heappush(data, -5)                 # tambahkan entri baru
>>> [heappop(data) for i in range(3)]  # ambil tiga yang terkecil
[-5, 0, 1]
```

## 11.8. Decimal Floating Point Arithmetic

_**nama file program : `11.8.decimal.py`**_

Modul `decimal` ini menawarkan `Decimal` tipe data untuk aritmatika titik mengambang desimal. Dibandingkan dengan float implementasi built-in dari floating point biner, kelas ini sangat membantu untuk
* aplikasi keuangan dan penggunaan lain yang memerlukan representasi desimal yang tepat,
* kontrol atas presisi,
* kontrol atas pembulatan untuk memenuhi persyaratan hukum atau peraturan,
* pelacakan tempat desimal yang signifikan, atau
* aplikasi di mana pengguna mengharapkan hasil yang sesuai dengan perhitungan yang dilakukan dengan tangan.


Misalnya, menghitung pajak 5% untuk biaya telepon 70 sen memberikan hasil yang berbeda dalam floating point desimal dan floating point biner. Perbedaan menjadi signifikan jika hasilnya dibulatkan ke sen terdekat:

```python
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
```

Hasilnya `Decimal` tetap nol, secara otomatis menyimpulkan signifikansi empat tempat dari perkalian dengan signifikansi dua tempat. Desimal mereproduksi matematika seperti yang dilakukan dengan tangan dan menghindari masalah yang dapat muncul ketika titik mengambang biner tidak dapat secara tepat mewakili jumlah desimal.


kelas `decimal` untuk melakukan perhitungan modulo dan tes kesetaraan yang tidak cocok untuk floating point biner:
```python
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995

>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> sum([0.1]*10) == 1.0
False
```

Modul ini decimalmenyediakan aritmatika dengan presisi sebanyak yang diperlukan:

```python
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
```
