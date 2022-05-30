# BAB 5 STRUKTUR DATA
Sumber : [tutorial python](https://docs.python.org/3.10/tutorial/controlflow.html)

## 5.1 DAFTAR
Tipe daftar memiliki beberapa metode sebagai berikut

`list.append(x)`
	Menambahkan item ke akhir daftar. setara dengan *a[len(a):]=[x]*

`list.extend(dapat diubah)`
	Memperluas daftar dengan menambahkan semua item dari iterable. Setara dengan *a[len(a):] = iterable*

`list.insert(saya , x)`
	Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen yang akan disisipkan sebelumnya, jadi disisipkan di bagian depan daftar, dan sama dengan 
	*a.insert(0, x)a.insert(len(a), x)a.append(x)*

`list.remove( x )`
	Mengapus item pertama dari daftar yang nilainya sama dengan *x* . Ini menimbulkan *ValueError* jika nilai tidak ada yang sama dengan *x*.

`list.pop( [ saya ] )`
	Mengapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, *a.pop()* hapus dan kembalikan item terakhir dalam daftar. (Kurung siku di sekitar i dalam tanda tangan metode menunjukkan bahwa parameternya opsional)

`list.clear( )`
	Hapus semua item dari daftar. Setara dengan *del a[:]*

`list.index( x [ , mulai [ , akhir ] ] )`
	Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x . Menaikkan a ValueErrorjika tidak ada item seperti itu.
	Argumen opsional mulai dan akhir ditafsirkan seperti dalam notasi irisan dan digunakan untuk membatasi pencarian ke urutan daftar tertentu. Indeks yang dikembalikan dihitung relatif terhadap awal urutan penuh daripada argumen awal .

`list.count( x )`
	Kembalikan berapa kali *x* muncul dalam daftar.

`list.sort( * , kunci=Tidak ada , terbalik=Salah )`
	Urutkan item dari daftar di tempat (argumen dapat digunakan untuk penyesuaian pengurutan.

`list.reverse( )`
	alikkan elemen daftar di tempatnya.

`list.copy( )`
	Kembalikan salinan daftar yang dangkal. Setara dengan *a[:]*.

Contoh penggunaan metode daftar 

```python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```

Metode seperti *insert*, *remove* atau *sort* yang hanya mengubah daftar tidak memiliki nilai kembalian yang dicetak – metode tersebut mengembalikan default *None*.

### 5.1.1. menggunakan List pada Stacks
Metode list membuatnya sangat mudah untuk menggunakan list sebagai stacks, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("masuk terakhir, keluar pertama"). 
Untuk menambahkan item ke bagian atas tumpukan, gunakan `append()`
Untuk mengambil item dari atas tumpukan, gunakan `pop()` tanpa indeks eksplisit.

Contoh program

```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

### 5.1.2 Menggunakan List pada Antrian
Menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("masuk pertama, keluar pertama"). 
Sementara itu melakukan sisipan atau muncul dari awal daftar lambat (karena semua elemen lain harus digeser satu).

Untuk mengimplementasikan antrian, gunakan `collections.deque` yang dirancang untuk menambahkan dan muncul dengan cepat dari kedua ujungnya. 
Contoh:

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # masuk Terry
>>> queue.append("Graham")          # masuk Graham
>>> queue.popleft()                 # Eric keluar pertama
'Eric'
>>> queue.popleft()                 # John keluar kedua
'John'
>>> queue                           # menampilkan yang masih berada dalam antrian
deque(['Michael', 'Terry', 'Graham'])
```


### 5.1.3 List Comprehensions
Common applications adalah untuk membuat list baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota dari urutan lain atau iterable, atau untuk membuat suburutan dari elemen-elemen yang memenuhi kondisi tertentu.

Misal membuat list kotak

```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

penulisan lebih ringkasnya

```python
squares = list(map(lambda x: x**2, range(10)))
```

atau

```python
squares = [x**2 for x in range(10)]
```

List Comprehensions terdiri dari tanda kurung yang berisi ekspresi diikuti oleh `for` klausa, lalu nol atau lebih foratau `if` klausa. Hasilnya adalah daftar baru yang dihasilkan dari evaluasi ekspresi dalam konteks `for` dan `if` klausa yang mengikutinya.

contoh listcomp menggabungkan elemen dari 2 list

```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

program diatas setara / ekuivalen dengan

```python
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
pernyataan `for` dan `if` jika ekspresi adalah *tuple* harus dikurung.*(x, y)*

```python
>>> vec = [-4, -2, 0, 2, 4]
>>> # buat daftar baru dengan nilai dua kali lipat
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter daftar untuk mengecualikan angka negatif
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # menerapkan fungsi ke semua element
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # memanggil method
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # buat daftar 2-tupel seperti (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # tupel harus dikurung, jika tidak, kesalahan akan muncul
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax
>>> # meratakan list menggunakan listcomp dengan 2 for
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

List Comprehensions dapat berisi ekspresi kompleks dan fungsi bersarang:

```python
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```


### 5.1.4. Nested List Comprehensions
Ekspresi awal dalam List Comprehensions dapat berupa ekspresi arbitrer, termasuk List Comprehensions lainnya.

Contoh matriks 3x4 diimplementasikan sebagai list 3 daftar panjang 4:

```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```

Listcomp berikut akan mengubah baris dan kolom:

```python
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

listcomp bersarang dievaluasi dalam konteks foryang mengikutinya, jadi program diatas setara dengan:

```python
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

penjabaran program sama dengan

```python
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

penulisan paling singkat menggunakan fungsi `zip()`, fungsi ini akan melakukan eksekusi seperti pada program diatas

```python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

## 5.2 Pernyataan **del**
Cara untuk menghapus item dari daftar yang diberikan indeksnya alih-alih nilainya dengan menggunakan  `del`.
Pernyataan `del` juga dapat digunakan untuk menghapus irisan dari daftar atau menghapus seluruh daftar.
contoh program

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]

>>> del a # del untu menghapus seluruh isi variabel
```

## 5.3 Tuples and Sequences
List dan string memiliki banyak properti umum, seperti operasi pengindeksan dan pengirisan. 
Karena Python adalah bahasa yang berkembang, tipe data urutan lainnya dapat ditambahkan. Ada juga tipe data urutan standar lainnya: *tuple*.
Tuple terdiri dari sejumlah nilai yang dipisahkan dengan koma.

contoh program

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # tuple bersarang :
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuple tidak dapat diubah:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> #tetapi mereka dapat berisi objek yang bisa berubah:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

Pada tupel keluaran selalu diapit tanda kurung, sehingga tupel bersarang diinterpretasikan dengan benar
Tanda kurung diperlukan jika tupel adalah bagian dari ekspresi yang lebih besar.
Hal ini untuk membuat tupel yang berisi objek yang bisa berubah, seperti list.


**Tupel** dengan **list** digunakan dalam situasi yang berbeda dan untuk tujuan yang berbeda.
Tuple tidak dapat diubah , dan biasanya berisi urutan elemen heterogen yang diakses melalui pembongkaran 
List bisa berubah , dan elemennya biasanya homogen dan diakses dengan mengulangi List.

Masalah khusus adalah konstruksi tupel yang berisi 0 atau 1 item: sintaks memiliki beberapa kebiasaan tambahan untuk mengakomodasi ini. Tupel kosong dibangun oleh sepasang tanda kurung kosong; tuple dengan satu item dibangun dengan mengikuti nilai dengan koma 

contoh :

```python
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```

Pernyataan tersebut adalah contoh pengepakan tuple : nilai , dan dikemas bersama dalam sebuah tupel. Operasi sebaliknya juga dimungkinkan: `t = 12345, 54321, 'hello!'1234554321'hello!'`

## 5.4 Sets
Himpunan adalah kumpulan yang tidak berurutan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Set objek juga mendukung operasi matematika sepertiunion, intersection, difference, and symmetric difference.

Kurung kurawal atau fungsi `set()` dapat digunakan untuk membuat himpunan. 
Catatan: untuk membuat set kosong Anda harus menggunakan **`set()`**, bukan `{}`.

contoh program

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)  # menunjukkan duplikan telah dihapus
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket   # menguji anggota himpunan
True
>>> 'crabgrass' in basket  # menguji anggota himpunan
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a   # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b    # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b    # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b    # letters in both a and b
{'a', 'c'}
>>> a ^ b    # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

Sama halnya dengan listcomp , pemahaman set juga didukung:

```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```

## 5.5 Kamus
Kamus kadang-kadang ditemukan dalam bahasa lain sebagai "ingatan asosiatif" atau "array asosiatif".
Tidak seperti urutan, yang diindeks oleh rentang angka, kamus diindeks oleh kunci , yang dapat berupa tipe apa pun yang tidak dapat diubah; string dan angka selalu bisa menjadi kunci. 
Tuple dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tupel; jika sebuah tuple berisi objek yang bisa berubah baik secara langsung maupun tidak langsung.


Operasi utama pada kamus adalah menyimpan nilai dengan beberapa kunci dan mengekstrak nilai yang diberikan kunci tersebut.
Dimungkinkan juga untuk menghapus pasangan key:value dengan `del`. Jika Anda menyimpan menggunakan kunci yang sudah digunakan, nilai lama yang terkait dengan kunci tersebut akan terlupakan. 

Melakukan `list(d)` di kamus mengembalikan daftar semua kunci yang digunakan dalam kamus, dalam urutan penyisipan. Jika ingin diurutkan, menggunakan `sorted(d)`. Untuk memeriksa apakah satu kunci ada dalam kamus, gunakan `in kata kunci`.

contoh program


```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

Konstruktor `dict()` membangun kamus langsung dari urutan pasangan nilai kunci:

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

pemahaman *dict* dapat digunakan untuk membuat kamus dari kunci arbitrer dan ekspresi nilai:

```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```
Jika kuncinya adalah string sederhana, terkadang lebih mudah untuk menentukan pasangan menggunakan argumen kata kunci:

```python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```


## 5.6 Teknik Looping

Saat mengulang melalui kamus, kunci dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan `items()`.

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

Saat mengulang melalui urutan, indeks posisi dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan fungsi `enumerate()`.

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```

Untuk mengulang dua atau lebih urutan pada saat yang sama, entri dapat dipasangkan dengan fungsi `zip()`.

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

Untuk mengulang urutan secara terbalik, pertama tentukan urutan dalam arah maju dan kemudian panggil fungsi `reversed()`.

```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```

Untuk mengulang urutan dalam urutan terurut, gunakan fungsi `sorted()` yang mengembalikan daftar terurut baru sambil membiarkan sumbernya tidak berubah.

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
```

Menggunakan `set()` pada urutan menghilangkan elemen duplikat. Penggunaan `sorted()` kombinasi dengan `set()` lebih dari urutan adalah cara idiomatik untuk mengulang elemen unik dari urutan dalam urutan yang diurutkan.

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```

Terkadang tergoda untuk mengubah daftar saat Anda mengulangnya; namun, seringkali lebih sederhana dan lebih aman untuk membuat daftar baru.

```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

## 5.7. More on Conditions
Kondisi yang digunakan dalam pernyataan `while` dan `if` dapat berisi operator apa pun, bukan hanya perbandingan.

Operator perbandingan `in` dan memeriksa apakah suatu nilai terjadi (tidak terjadi) secara berurutan. Operator membandingkan apakah dua objek benar-benar objek yang sama. Semua operator pembanding memiliki prioritas yang sama, yaitu lebih rendah dari semua operator numerik. *not inisis not*

Perbandingan dapat digabungkan menggunakan operator Boolean `and` dan `or`, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan *not*.

Operator Boolean `and` dan `or` yang disebut operator hubung singkat : argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. 


```python
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```


## 5.8 Comparing Sequences dan Tipe Lainnya
Objek urutan biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. 
Perbandingannya menggunakan  lexicographical =>
pertama dua item pertama dibandingkan, dan jika berbeda, ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai salah satu urutan habis. 
Jika dua item yang akan dibandingkan itu sendiri merupakan urutan dari jenis yang sama, perbandingan leksikografis dilakukan secara rekursif.
Jika semua item dari dua urutan membandingkan sama, urutan dianggap sama.
Jika satu barisan merupakan sub-urutan awal dari yang lain, barisan yang lebih pendek adalah yang lebih kecil. Urutan leksikografis untuk string menggunakan nomor titik kode Unicode untuk mengurutkan karakter individual.


```python
1, 2, 3)              < (1, 2, 4)
True
[1, 2, 3]              < [1, 2, 4]
True
'ABC' < 'C' < 'Pascal' < 'Python'
True
(1, 2, 3, 4)           < (1, 2, 4)
True
(1, 2)                 < (1, 2, -1)
True
(1, 2, 3)             == (1.0, 2.0, 3.0)
True
```

Membandingkan objek dari jenis yang berbeda dengan < atau > **legal** asalkan objek tersebut memiliki metode perbandingan yang sesuai. Misalnya, tipe numerik campuran dibandingkan menurut nilai numeriknya, jadi 0 sama dengan 0,0, dll. Jika tidak, alih-alih memberikan urutan arbitrer, juru bahasa akan memunculkan *TypeErrorpengecualian*.