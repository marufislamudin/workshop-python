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
[program](minggu-3/src/daftar.py)

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
'''