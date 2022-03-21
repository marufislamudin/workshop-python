# BAB 8 PENANGANAN ERROR DAN EXCEPTION
Sumber : [tutorial python](https://docs.python.org/3/tutorial/errors.html)

Pesan kesalahan yang telah dijumpai jika salah dalam menuliskan program, terdapat 2 jenis kesalahan yang dapat dibedakan yaitu syntax errors dan exceptions.

## 8.1 Syntax Errors
Syntax Errors, juga dikenal dengan kesalahan penguraian, ini merupakan jenis keluhan paling umum yang sering ditemukan pada saat mulai belajar menggunakan program python.
contoh :

```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

pengurai mengulangi baris yang menyinggung dan menunjukkan pada titik paling awal di baris yang terdapat kesalahan. Kesalahan disebabkan oleh token sebelum panah: dalam contoh, kesalahan terdeteksi pada fungsi `print()`, karena titik dua **( ':')** hilang sebelumnya. Nama file dan nomor baris dicetak sehingga Anda tahu di mana mencarinya jika input berasal dari skrip.


## 8.2. Exceptions
Jika pada suatu pernyataan atau ekspresi secara sintak benar, juga dapat menyebabkan kesalahan pada saat dieksekusi. Kesalahan yang terdeteksi selama eksekusi disebut **exceptions** dan tidak fatal. 
Sebagian besar pengecualian tidak ditangani oleh program, dan menghasilkan pesan kesalahan seperti yang ditunjukkan pada contoh berikut :

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Baris terakhir dari pesan kesalahan menunjukkan apa yang terjadi.
Exceptions datang dalam tipe yang berbeda, dan tipe tersebut dicetak sebagai bagian dari pesan: tipe dalam contoh adalah `ZeroDivisionError`, `NameError` dan `TypeError`. String yang dicetak sebagai tipe exceptions adalah nama exceptions bawaan yang terjadi. Ini berlaku untuk semua exceptions bawaan, tetapi tidak harus benar untuk pengecualian yang ditentukan pengguna. Nama pengecualian standar adalah pengidentifikasi bawaan.

Sisa baris memberikan detail berdasarkan jenis pengecualian dan apa yang menyebabkannya.
Bagian pesan kesalahan sebelumnya menunjukkan konteks di mana pengecualian terjadi, dalam bentuk pelacakan balik tumpukan. Secara umum ini berisi baris sumber daftar traceback stack. Namun, itu tidak akan menampilkan baris yang dibaca dari input standar.


## 8.3. Handling Exceptions
Pada contoh berikut, program meminta pengguna untuk memasukkan  bilangan bulat yang valid , tetapi mengizinkan pengguna untuk menginterupsi program (menggunakan atau apa pun yang didukung sistem operasi). Interupsi yang dibuat pengguna ditandai dengan memunculkan exceptions. `Control-CKeyboardInterrupt`

```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```

Hasil output jika input angka

```python
Please enter a number: 34
```

Hasil output jika input bukan angka

```python
Please enter a number: bil
Oops!  That was no valid number.  Try again...
```

Pernyataan try tersebut berfungsi sebagai :
* Pertama, klausa try (pernyataan antara `try` dan `except` kata kunci) dieksekusi.
* Jika tidak ada exceptions yang terjadi, klausa except  dilewati dan eksekusi `try` pernyataan selesai.
* Jika exceptions terjadi selama eksekusi `try` klausa, sisa klausa akan dilewati. Kemudian, jika tipenya cocok dengan exceptions yang dinamai *except* kata kunci, klausa kecuali dieksekusi, dan kemudian eksekusi dilanjutkan setelah blok coba/except.
* Jika terjadi exceptions yang tidak cocok dengan pengecualian yang disebutkan dalam klausa except, itu diteruskan ke try pernyataan luar. Jika tidak ada penangan yang ditemukan, itu adalah pengecualian yang tidak tertangani dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.


pernyataan `try` memiliki lebih dari satu except clause.  Untuk menentukan penangan untuk exceptions yang berbeda. Paling banyak satu handler akan dieksekusi. Penangan hanya menangani exceptions yang terjadi di klausa `try` yang sesuai , bukan di penangan lain dari pernyataan try yang sama. Klausa exceptions dapat menyebutkan beberapa exceptions sebagai tupel dalam kurung, misalnya:

```python
... except (RuntimeError, TypeError, NameError):
...     pas
```

Kelas dalam klausa *except* kompatibel dengan exceptions jika itu adalah kelas yang sama atau kelas dasar daripadanya. Misalnya, kode berikut akan mencetak B, C, D dalam urutan itu:

```python
>>> class B(Exception):
...     pass
...
>>> class C(B):
...     pass
...
>>> class D(C):
...     pass
...
>>> for cls in [B, C, D]:
...     try:
...         raise cls()
...     except D:
...         print("D")
...     except C:
...         print("C")
...     except B:
...         print("B")
...
B
C
D
```

Semua pengecualian mewarisi dari `BaseException`, sehingga dapat digunakan sebagai karakter pengganti. Ini mudah untuk menutupi kesalahan pemrograman yang sebenarnya dengan cara ini. Itu juga dapat digunakan untuk mencetak pesan kesalahan dan kemudian menaikkan kembali pengecualian.

```python
>>> import sys
>>>
>>> try:
...     f = open('myfile.txt')
...     s = f.readline()
...     i = int(s.strip())
... except OSError as err:
...     print("OS error: {0}".format(err))
... except ValueError:
...     print("Could not convert data to an integer.")
... except BaseException as err:
...     print(f"Unexpected {err=}, {type(err)=}")
...     raise
...
OS error: [Errno 2] No such file or directory: 'myfile.txt'
```

Sebagai alternatif, klausa pengecualian terakhir dapat menghilangkan nama pengecualian, namun nilai pengecualian kemudian harus diambil dari `sys.exc_info()`[1].


Pernyataan *try...* memiliki klausa `else except` opsional, yang jika ada, harus mengikuti semua except clauses . Berguna untuk kode yang harus dijalankan jika klausa *try* tidak memunculkan eksepsi. Sebagai contoh:

```python
>>> for arg in sys.argv[1:]:
...     try:
...         f = open(arg, 'r')
...     except OSError:
...         print('cannot open', arg)
...     else:
...         print(arg, 'has', len(f.readlines()), 'lines')
...         f.close()
...
```

Penggunaan klausa `else`  lebih baik daripada menambahkan kode tambahan ke klausa `try`  karena menghindari secara tidak sengaja menangkap pengecualian yang tidak dimunculkan oleh kode yang dilindungi oleh pernyataan `try… except`.

Ketika pengecualian terjadi, jika memiliki nilai terkait, dikenal sebagai argumen pengecualian. Kehadiran dan tipe argumen bergantung pada tipe pengecualian.

Klausa except dapat menentukan variabel setelah nama excepttion. Variabel terikat ke instance pengecualian dengan argumen yang disimpan di `instance.args`. Untuk kenyamanan, instance pengecualian mendefinisikan `__str__()` sehingga argumen dapat dicetak secara langsung tanpa harus reference `.args`. Instance pengecualian juga dapat dibuat terlebih dahulu sebelum menaikkannya dan menambahkan atribut apa pun ke dalamnya seperti yang diinginkan.

```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

Jika exceptions memiliki argumen, akan dicetak sebagai bagian terakhir ('detail') dari pesan untuk exceptions yang tidak ditangani.

Exception handlers tidak hanya menangani exceptions jika exceptions muncul segera di klausa *try*, tetapi juga jika terjadi di dalam fungsi yang dipanggil dalam klausa *try*.
Sebagai contoh:

```python
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```


## 8.4. Raising Exceptions
Pernyataan `raise` memungkinkan programmer untuk memaksa pengecualian tertentu terjadi. Sebagai contoh:

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

Satu-satunya argumen untuk `raise` menunjukkan pengecualian yang akan diajukan. Harus berupa instance exception atau exception class. Jika kelas pengecualian dilewatkan, itu akan secara implisit dipakai dengan memanggil konstruktornya tanpa argumen:

```python
>>> raise ValueError #singkatan untuk 'raise ValueError()'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError
```

Jika perlu menentukan apakah exception telah dimunculkan tetapi tidak bermaksud untuk menanganinya, bentuk `raise` pernyataan yang lebih sederhana memungkinkan untuk menaikkan kembali exception:

```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```


##  Exception Chaining
Pernyataan `raise` memungkinkan opsional `from` yang memungkinkan exception rantai. Sebagai contoh:

```python
# exc harus berupa exception instance atau None.
raise RuntimeError from exc
```

Ini bisa berguna saat mengubah exception. Sebagai contoh:

```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

# The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

Rantai exception terjadi secara otomatis ketika exception dinaikkan di dalam *except* atau bagian *finally*. Ini dapat dinonaktifkan dengan menggunakan `from None` idiom:

```python
>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```


## 8.6. User-defined Exceptions
Program dapat memberi nama exception mereka sendiri dengan membuat exception class baru. Exception biasanya harus diturunkan dari Exception class, baik secara langsung maupun tidak langsung.

Exception class dapat didefinisikan yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya dibuat sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk exception.

Sebagian besar exception didefinisikan dengan nama yang diakhiri dengan "Error", mirip dengan penamaan exception standar.

Banyak modul standar mendefinisikan exception mereka sendiri untuk melaporkan kesalahan yang mungkin terjadi dalam fungsi yang mereka tetapkan.


## 8.7. Defining Clean-up Actions
Pernyataan `try` tersebut memiliki klausa opsional lain yang dimaksudkan untuk mendefinisikan tindakan pembersihan yang harus dilakukan dalam semua keadaan. Sebagai contoh:

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```

Jika ada klausa `finally`, klausa `finally` akan dieksekusi sebagai tugas terakhir sebelum pernyataan `try`  selesai. Klausa `finally` berjalan apakah pernyataan `try` menghasilkan exception atau tidak. 
Poin-poin berikut membahas kasus yang lebih kompleks ketika exception terjadi:

* Jika exception terjadi selama eksekusi klausa `try`, exception dapat ditangani oleh klausa `except`. Jika exception tidak ditangani oleh `except` klausa, exception dimunculkan kembali setelah *finally* klausa dieksekusi.
* Exception dapat terjadi selama eksekusi suatu `except` atau `else` klausa. Sekali lagi, exception dinaikkan kembali setelah finally klausa dieksekusi.
* Jika `finally` klausa mengeksekusi `break`, `continue` atau pernyataan `return` , exception tidak dimunculkan kembali.
* Jika pernyataan `try` mencapai `break`, `continue` atau pernyataan `return`,`finally`klausa akan dieksekusi tepat sebelum eksekusi *break, continueatau pernyataan return*.
* Jika `finally` klausa menyertakan pernyataan return, nilai yang dikembalikan akan menjadi nilai dari pernyataan `finally` klausa `return`, bukan nilai dari pernyataan `try` klausa `return` .

contoh
```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False
```

Contoh yang lebih rumit:

```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

`finally` klausa dieksekusi dalam acara apa pun. Dibangkitkan `TypeError` dengan membagi dua *string* tidak ditangani oleh `except` klausa dan karena itu dinaikkan kembali setelah `finally` klausa dieksekusi.

Dalam aplikasi dunia nyata, `finally` klausa ini berguna untuk melepaskan sumber daya eksternal (seperti file atau koneksi jaringan), terlepas dari apakah penggunaan sumber daya itu berhasil.


## 8.8. Predefined Clean-up Actions
Beberapa objek menentukan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal. 
Contoh berikut, mencoba membuka file dan mencetak isinya ke layar.

```python
>>> for line in open("myfile.txt"):
...     print(line, end="")
...
```

Masalah dengan kode ini adalah membiarkan file terbuka untuk waktu yang tidak ditentukan setelah bagian kode ini selesai dieksekusi. Bisa menjadi masalah untuk aplikasi yang lebih besar. Pernyataan `with` tersebut memungkinkan objek seperti file untuk digunakan dengan cara yang memastikan mereka selalu dibersihkan dengan cepat dan benar.

```python
>>> with open("myfile.txt") as f:
...     for line in f:
...         print(line, end="")
...
```

Setelah pernyataan dieksekusi, file `f` selalu ditutup, bahkan jika ada masalah saat memproses baris. Objek yang, seperti file, menyediakan tindakan pembersihan yang telah ditentukan sebelumnya akan menunjukkan hal ini dalam dokumentasinya.



