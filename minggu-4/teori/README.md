# 6. MODUL
Sumber : [tutorial python](https://docs.python.org/3.10/tutorial/modules.html)

Saat program semakin panjang, membaginya menjadi beberapa file untuk perawatan yang lebih mudah, juga ingin menggunakan fungsi praktis yang telah ditulis di beberapa program tanpa menyalin definisinya ke dalam setiap program.

Untuk mendukung ini, Python memiliki cara untuk menempatkan definisi dalam file dan menggunakannya dalam skrip atau dalam instance interpreter yang interaktif. File seperti itu disebut modul. Definisi dari sebuah modul dapat diimpor ke modul lain atau ke modul utama. 

Modul adalah file yang berisi definisi dan pernyataan Python. Nama file adalah nama modul dengan akhiran `.py` ditambahkan. Di dalam sebuah modul, nama modul (sebagai string) tersedia sebagai nilai dari variabel global `__name__`. 
Misalnya, membuat file yang dipanggil fibo.py di direktori saat ini dengan konten berikut:
_**nama file : `fibo.py`**_

```python
>>> def fib(n):    # write Fibonacci series up to n
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> def fib2(n):   # return Fibonacci series up to n
...     result = []
...     a, b = 0, 1
...     while a < n:
...         result.append(a)
...         a, b = b, a+b
...     return result
...
```

Memasukkan interpreter Python dan impor modul ini dengan perintah berikut:

```python
>>> import fibo
```

_**nama file : `6.py`**_

Menggunakan nama modul Anda dapat mengakses fungsi:

```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```

Jika ingin sering menggunakan suatu fungsi, dapat menetapkannya ke nama lokal:

```python
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

## 6.1 More on Modules
Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul. Mereka dieksekusi hanya saat pertama kali nama modul ditemukan dalam pernyataan impor. Mereka juga dijalankan jika file dieksekusi sebagai skrip.

Setiap modul memiliki tabel simbol pribadinya sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul. Dengan demikian, pembuat modul dapat menggunakan variabel global dalam modul tanpa mengkhawatirkan bentrokan yang tidak disengaja dengan variabel global pengguna. Di sisi lain  dapat menyentuh variabel global modul dengan notasi yang sama yang digunakan untuk merujuk ke fungsinya, `modname.itemname`.

Modul dapat mengimpor modul lain. Merupakan kebiasaan tetapi tidak diharuskan untuk menempatkan semua importpernyataan di awal modul (atau skrip, dalam hal ini). Nama modul yang diimpor ditempatkan di tabel simbol global modul pengimpor.

Ada varian dari **import** pernyataan yang mengimpor nama dari modul langsung ke tabel simbol modul pengimpor. Sebagai contoh:
_**nama file : `6.1.py`**_

```python
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Ini tidak memperkenalkan nama modul dari mana impor diambil dalam tabel simbol lokal (jadi dalam contoh, `fibo` tidak didefinisikan).

Varian untuk mengimpor semua nama yang didefinisikan oleh modul:

```python
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Ini mengimpor semua nama kecuali yang dimulai dengan garis bawah ( _ ). Dalam kebanyakan kasus, pemrogram Python tidak menggunakan fasilitas ini karena fasilitas ini memperkenalkan serangkaian nama yang tidak diketahui ke dalam juru bahasa, mungkin menyembunyikan beberapa hal yang telah ditetapkan.

Secara umum praktik mengimpor dari modul atau paket tidak disukai, karena sering menyebabkan kode yang tidak dapat dibaca dengan baik. Namun, tidak apa-apa menggunakannya untuk menyimpan pengetikan dalam sesi interaktif.

Jika nama modul diikuti oleh `as`, maka nama berikut `as` terikat langsung ke modul yang diimpor.

```python
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Ini secara efektif mengimpor modul dengan cara yang sama seperti yang akan dilakukan, dengan satu-satunya perbedaan tersedia sebagai `.import fibofib`


Juga dapat digunakan saat menggunakan fromdengan efek serupa:

```python
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

**Catatan** 
```
Untuk alasan efisiensi, setiap modul hanya diimpor sekali per sesi juru bahasa. Oleh karena itu, jika Anda mengubah modul, Anda harus memulai ulang penerjemah – atau, jika hanya satu modul yang ingin Anda uji secara interaktif, gunakan importlib.reload(), mis .import importlib; importlib.reload(modulename)
```

### 6.1.1 Executing modules as scripts
_**nama file : `6.1.1.py`**_
Saat menjalankan modul Python dengan

```python
python fibo.py <arguments>
```

kode dalam modul akan dieksekusi, sama seperti jika mengimpornya, tetapi dengan `__name__` set ke `"__main__"`. Berarti dengan menambahkan kode ini di akhir modul Anda:

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

Membuat file dapat digunakan sebagai skrip serta modul yang dapat diimpor, karena kode yang mem-parsing baris perintah hanya berjalan jika modul dijalankan sebagai file "utama":

```
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

Jika modul diimpor, kode tidak dijalankan:

```python
>>> import fibo
>>>
```

Ini sering digunakan baik untuk menyediakan antarmuka pengguna yang nyaman ke modul, atau untuk tujuan pengujian (menjalankan modul saat skrip mengeksekusi rangkaian pengujian).


### 6.1.2  The Module Search Path

Ketika sebuah modul bernama spamdiimpor, interpreter pertama mencari modul built-in dengan nama itu. Jika tidak ditemukan, maka akan mencari file bernama `spam.py` dalam daftar direktori yang diberikan oleh variabel `sys.path`. `sys.path` diinisialisasi dari lokasi ini:

* Direktori yang berisi skrip *input* (atau direktori saat ini ketika tidak ada file yang ditentukan).

* `PYTHONPATH` (daftar nama direktori, dengan sintaks yang sama dengan variabel shellPATH).

* Default yang bergantung pada instalasi (berdasarkan konvensi termasuk site-packagesdirektori, ditangani oleh sitemodul).

**Catatan** 
```
Pada sistem file yang mendukung symlink, direktori yang berisi skrip input dihitung setelah symlink diikuti. Dengan kata lain direktori yang berisi symlink tidak ditambahkan ke jalur pencarian modul.
```

Setelah inisialisasi, program Python dapat memodifikasi file `sys.path`. Direktori yang berisi skrip yang sedang dijalankan ditempatkan di awal jalur pencarian, di depan jalur pustaka standar. Ini berarti bahwa skrip di direktori itu akan dimuat alih-alih modul dengan nama yang sama di direktori perpustakaan. Ini adalah kesalahan kecuali penggantian dimaksudkan.


### 6.1.3  “Compiled” Python files

Untuk mempercepat pemuatan modul, Python menyimpan versi terkompilasi dari setiap modul dalam `__pycache__` direktori dengan nama , di mana versi mengkodekan format file yang dikompilasi; biasanya berisi nomor versi Python. 
Misalnya, di CPython rilis 3.3 versi kompilasi dari spam.py akan di-cache sebagai . Konvensi penamaan ini memungkinkan modul yang dikompilasi dari rilis yang berbeda dan versi Python yang berbeda untuk hidup berdampingan `.module.version.pyc__pycache__/spam.cpython-33.pyc`

Python memeriksa tanggal modifikasi sumber terhadap versi yang dikompilasi untuk melihat apakah itu kedaluwarsa dan perlu dikompilasi ulang. Ini adalah proses yang sepenuhnya otomatis. Juga, modul yang dikompilasi adalah platform-independen, sehingga perpustakaan yang sama dapat dibagi di antara sistem dengan arsitektur yang berbeda.

Python tidak memeriksa cache dalam dua keadaan. Pertama, selalu mengkompilasi ulang dan tidak menyimpan hasil untuk modul yang dimuat langsung dari baris perintah. Kedua, tidak memeriksa cache jika tidak ada modul sumber. Untuk mendukung distribusi non-sumber (hanya dikompilasi), modul yang dikompilasi harus berada di direktori sumber, dan tidak boleh ada modul sumber.

Beberapa tips :

* Anda dapat menggunakan `-O` atau `-OO` mengaktifkan perintah Python untuk mengurangi ukuran modul yang dikompilasi. Sakelar `-O` menghapus pernyataan tegas, `-OO` sakelar menghapus pernyataan tegas dan string `__doc__`. Karena beberapa program mungkin bergantung pada ketersediaannya, Anda hanya boleh menggunakan opsi ini jika Anda tahu apa yang Anda lakukan. Modul "Dioptimalkan" memiliki `opt-` tag dan biasanya lebih kecil. Rilis mendatang dapat mengubah efek pengoptimalan.

* Sebuah program tidak berjalan lebih cepat saat dibaca dari `.pyc` file daripada saat dibaca dari `.py` file; satu-satunya hal yang lebih cepat tentang `.pyc` file adalah kecepatan pemuatannya.

* Modul compilealldapat membuat file `.pyc` untuk semua modul dalam direktori.

* Ada lebih detail tentang proses ini, termasuk diagram alir keputusan, di*PP 3147* .



## 6.2 Modul Standar

Python hadir dengan pustaka modul standar, yang dijelaskan dalam dokumen terpisah, Referensi Pustaka Python (“Referensi Pustaka” selanjutnya). Beberapa modul dibangun ke dalam juru bahasa, menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke sistem operasi primitif seperti panggilan sistem. Kumpulan modul tersebut adalah opsi konfigurasi yang juga bergantung pada platform yang mendasarinya. 

Misalnya, `winreg` modul hanya disediakan pada sistem Windows. Satu modul tertentu patut mendapat perhatian: `sys`, yang dibangun ke dalam setiap juru bahasa Python. Variabel `sys.ps1` dan `sys.ps2` tentukan string yang digunakan sebagai prompt primer dan sekunder:
_**nama file : `6.2.py`**_

```python
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```

Kedua variabel ini hanya ditentukan jika interpreter dalam mode interaktif.

Variabel `sys.path` adalah daftar string yang menentukan jalur pencarian interpreter untuk modul. Ini diinisialisasi ke jalur default yang diambil dari variabel lingkungan `PYTHONPATH`, atau dari default bawaan jika `PYTHONPATH` tidak diatur. Dapat memodifikasinya menggunakan operasi daftar standar:

```python
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

## Fungsi dir()

Fungsi bawaan `dir()` digunakan untuk mengetahui nama mana yang didefinisikan oleh modul, mengembalikan daftar string yang diurutkan:
_**nama file : `6.3.py`**_

```python
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)  
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']
 ```

Tanpa argumen, buat `dir()` daftar nama yang telah ditetapkan saat ini:

```python
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

Bahwa ini mencantumkan semua jenis nama: variabel, modul, fungsi, dll.

`dir()` tidak mencantumkan nama fungsi dan variabel bawaan. Jika ingin daftarnya, mereka didefinisikan dalam modul standar `builtins`:

```python
>>> import builtins
>>> dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
 ```


## Packages

Paket adalah cara menyusun namespace modul Python dengan menggunakan **"nama modul bertitik"**. 
Misalnya, nama modul **A**. **B** menunjuk sebuah submodul yang dinamai Bdalam sebuah package bernama **A**. Sama seperti penggunaan modul yang menyelamatkan pembuat modul yang berbeda dari keharusan khawatir tentang nama variabel global satu sama lain, penggunaan nama modul bertitik menyelamatkan penulis package multi-modul seperti *NumPy* atau *Pillow* dari keharusan khawatir tentang nama modul masing-masing. .

Misalkan ingin merancang kumpulan modul (**"package"**) untuk penanganan file suara dan data suara yang seragam. Ada banyak format file suara yang berbeda (biasanya dikenali dari ekstensinya, misalnya: `.wav`, `.aiff`, `.au`), jadi mungkin perlu membuat dan memelihara koleksi modul yang terus bertambah untuk konversi antara berbagai format file. Ada juga banyak operasi berbeda yang mungkin ingin dilakukan pada data suara (seperti mencampur, menambahkan gema, menerapkan fungsi equalizer, membuat efek stereo buatan), jadi selain itu akan menulis aliran modul yang tidak pernah berakhir untuk dilakukan operasi ini. 

Berikut adalah kemungkinan struktur untuk package (dinyatakan dalam bentuk sistem file hierarkis):

```path
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

Saat mengimpor package, Python mencari melalui direktori untuk `sys.path` mencari subdirektori package.

File `__init__.py` diperlukan untuk membuat direktori memperlakukan Python yang berisi file sebagai **packages**. Ini mencegah direktori dengan nama umum, seperti *string*, secara tidak sengaja menyembunyikan modul valid yang muncul kemudian di jalur pencarian modul. Dalam kasus yang paling sederhana, `__init__.py` hanya dapat berupa file kosong, tetapi juga dapat mengeksekusi kode inisialisasi untuk package atau mengatur `__all__` variabel, yang dijelaskan kemudian.

Pengguna package dapat mengimpor modul individual dari package, misalnya:

```python
import sound.effects.echo
```

memuat submodule sound `.effects.echo`. Itu harus dirujuk dengan nama lengkapnya.

```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

Cara alternatif untuk mengimpor submodule adalah:

```python
from sound.effects import echo
```

Memuat submodule `echo`, dan membuatnya tersedia tanpa awalan paketnya, sehingga dapat digunakan sebagai berikut:

```python
echo.echofilter(input, output, delay=0.7, atten=4)
```

variasi lain mengimpor fungsi atau variabel yang diinginkan secara langsung:

```python
from sound.effects.echo import echofilter
```

memuat submodule `echo`, tetapi ini membuat fungsinya `echofilter()` tersedia secara langsung:

```python
echofilter(input, output, delay=0.7, atten=4)
```

Saat menggunakan , item dapat berupa submodul (atau subpaket) package, atau nama lain yang ditentukan dalam package, seperti fungsi, package, atau variabel. 

Pernyataan pertama menguji apakah item didefinisikan dalam package; jika tidak, ia menganggapnya sebagai modul dan mencoba memuatnya. Jika gagal menemukannya, pengecualian dimunculkan. `from package import itemimportImportError`

Sebaliknya, saat menggunakan sintaks seperti, setiap item kecuali yang terakhir harus berupa package; item terakhir dapat berupa modul atau package tetapi tidak dapat berupa package atau fungsi atau variabel yang ditentukan dalam item sebelumnya. `import item.subitem.subsubitem`


### 6.4.1 Importing  From a Package

Idealnya, orang akan berharap bahwa ini entah bagaimana keluar ke sistem file, menemukan submodul mana yang ada dalam package, dan mengimpor semuanya. Ini bisa memakan waktu lama dan mengimpor sub-modul mungkin memiliki efek samping yang tidak diinginkan yang seharusnya hanya terjadi ketika sub-modul diimpor secara eksplisit `.from sound.effects import *`

Satu-satunya solusi adalah bagi pembuat package untuk memberikan indeks eksplisit dari package tersebut. Pernyataan importmenggunakan konvensi berikut: jika `__init__.py` kode package mendefinisikan daftar bernama `__all__`, itu dianggap sebagai daftar nama modul yang harus diimpor ketika ditemui. Terserah pembuat package untuk tetap memperbarui daftar ini ketika versi baru dari package dirilis. Pembuat package juga dapat memutuskan untuk tidak mendukungnya, jika mereka tidak melihat kegunaan untuk mengimpor `*` dari package mereka. 

Misalnya, file dapat berisi kode berikut: `from package import *sound/effects/__init__.py`

```python
__all__ = ["echo", "surround", "reverse"]
```

Berarti bahwa akan mengimpor tiga submodul yang bernama dari package tersebut.`from sound.effects import *sound`

Jika `__all__` tidak didefinisikan, pernyataan tidak mengimpor semua submodul dari package ke namespace saat ini; itu hanya memastikan bahwa package telah diimpor mungkin menjalankan kode inisialisasi apa pun dan kemudian mengimpor nama apa pun yang ditentukan dalam package. Ini termasuk nama apa pun yang ditentukan dan submodul yang dimuat secara eksplisit oleh . Ini juga mencakup setiap submodul dari package yang secara eksplisit dimuat oleh pernyataan sebelumnya. Pertimbangkan kode ini: `from sound.effects import *sound.effectssound.effects__init__.py__init__.pyimport`

```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

Dalam contoh ini, modul `echo` dan `surround` diimpor ke namespace saat ini karena mereka didefinisikan dalam `sound.effects` package saat `from...import` pernyataan dijalankan. Ini juga berfungsi ketika `__all__` didefinisikan.

Meskipun modul tertentu dirancang untuk mengekspor hanya nama yang mengikuti pola tertentu saat Anda menggunakan , itu masih dianggap sebagai praktik buruk dalam kode produksi.`import *`

Sebenarnya, ini adalah notasi yang disarankan kecuali modul pengimpor perlu menggunakan submodul dengan nama yang sama dari package yang berbeda. `from package import specific_submodule`


### 6.4.2  Intra-package References

Ketika package disusun menjadi subpaket (seperti `sound` package dalam contoh), Anda dapat menggunakan impor absolut untuk merujuk ke submodul package saudara kandung. 

Misalnya, jika modul `sound.filters.vocoder` perlu menggunakan `echo` modul dalam `sound.effects` package, itu dapat menggunakan `.from sound.effects import echo`

Anda juga dapat menulis impor relatif, dengan bentuk pernyataan impor. Impor ini menggunakan titik awal untuk menunjukkan package saat ini dan induk yang terlibat dalam impor relatif. Dari modul misalnya, Anda dapat menggunakan: `from module import namesurround`

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

Impor relatif didasarkan pada nama modul saat ini. Karena nama modul utama selalu `"__main__"`, modul yang dimaksudkan untuk digunakan sebagai modul utama aplikasi Python harus selalu menggunakan impor absolut.


### 6.4.3 Packages in Multiple Directories

Package mendukung satu atribut khusus lagi, `__path__`. Ini diinisialisasi menjadi daftar yang berisi nama direktori yang menyimpan package `__init__.py` sebelum kode dalam file itu dieksekusi. Variabel ini dapat dimodifikasi; hal itu akan memengaruhi pencarian modul dan subpaket di masa mendatang yang terdapat dalam package.

Meskipun fitur ini tidak sering diperlukan, fitur ini dapat digunakan untuk memperluas kumpulan modul yang ditemukan dalam sebuah package.