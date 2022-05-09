# BAB 12 Virtual Environments dan Packages
Sumber : [tutorial python](https://docs.python.org/3/tutorial/venv.html)


## 12.1. Introduction

Aplikasi Python akan sering menggunakan package dan modul yang bukan dari daftar pustaka standar. Aplikasi terkadang memerlukan versi pusta tertentu, karena aplikasi mungkin mengharuskan bug tertentu telah diperbaiki atau aplikasi mungkin ditulis menggunakan versi antarmuka pustaka yang sudah usang.

Ini berarti tidak mungkin satu instalasi Python memenuhi persyaratan setiap aplikasi. Jika aplikasi `A` membutuhkan versi `1.0` dari modul tertentu tetapi aplikasi `B` membutuhkan versi `2.0`, maka persyaratan tersebut bertentangan dan menginstal versi `1.0` atau `2.0` akan membuat satu aplikasi tidak dapat berjalan.

Solusi untuk masalah ini adalah dengan membuat **Virtual Environments** , struktur direktori mandiri yang berisi instalasi Python untuk versi Python tertentu, ditambah sejumlah paket tambahan.

Aplikasi yang berbeda kemudian dapat menggunakan **virtual environment** yang berbeda. Untuk mengatasi contoh masalah sebelumnya dari persyaratan yang bertentangan, aplikasi `A` dapat memiliki *virtual environment* sendiri dengan versi `1.0`. Sementara aplikasi `B` memiliki *virtual environment* lain dengan versi `2.0`. Jika aplikasi `B` memerlukan pustaka yang ditingkatkan ke versi `3.0`, ini tidak akan memengaruhi environment aplikasi `A`


## 12.2. Membuat Virtual Environments

Modul yang digunakan untuk membuat dan mengelola virtual environment disebut `venv`. 
`venv` biasanya akan menginstal versi terbaru Python yang dimiliki. Jika terdapat beberapa versi Python di sistem komputer, maka dapat memilih versi Python tertentu dengan menjalankan `python3` atau versi mana pun yang diinginkan.

Untuk membuat virtual environment, menentukan direktori tempat kita ingin meletakkannya, kemudian jalankan `venv` modul sebagai scrip dengan jalur direktori:

```python
python3 -m venv tutorial-env
```

*Ini akan membuat `tutorial-env` direktori jika tidak ada, dan juga membuat direktori di dalamnya yang berisi salinan interpreter Python dan berbagai file pendukung.*

Lokasi direktori umum untuk virtual environment adalah `.venv`. Nama ini membuat direktori biasanya tersembunyi di shell kita dan memberinya nama yang menjelaskan mengapa direktori itu ada. Ini juga mencegah bentrokan dengan `.env` file definisi virtual environment yang didukung oleh beberapa peralatan.

Untuk dapat mengaktifkannya.

Di Windows, jalankan:

```python
tutorial-env\Scripts\activate.bat
```

pada Unic atau MacOS, jalankan :

```python
source tutorial-env/bin/activate
```

*`(Skrip ini ditulis untuk bash shell. Jika Anda menggunakan csh atau  fish shells , ada alternatif activate.csh dan activate.fish skrip yang harus Anda gunakan.`*

Mengaktifkan virtual environment akan mengubah prompt shell Anda untuk menunjukkan virtual environment apa yang Anda gunakan, dan memodifikasi environment sehingga menjalankan `python` akan memberi Anda versi tertentu dan instalasi Python. Sebagai contoh:

```python
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) C:\Users\HP>py
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

>>> import sys
>>> sys.path
  ...
['', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.1264.0_x64__qbz5n2kfra8p0\\python310.zip', 
'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.1264.0_x64__qbz5n2kfra8p0\\DLLs', 
'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.1264.0_x64__qbz5n2kfra8p0\\lib', 
'C:\\Users\\HP\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0', 
'C:\\Users\\HP\\tutorial-env', 'C:\\Users\\HP\\tutorial-env\\lib\\site-packages']
```

## 12.3. Mengelola Packages with pip
Kita dapat menginstal, memutakhirkan, dan menghapus paket menggunakan program bernama `pip` . Secara default `pip` akan menginstal paket dari Python Package Index, `< https://pypi.org >`. Kita dapat menelusuri Indeks Packages Python dengan membukanya di browser web.

`pip` memiliki sejumlah sub-perintah: `“install”` , `“uninstall”`, `“freeze”`, dll. (Lihat panduan Instalasi Modul Python untuk dokumentasi lengkap untuk pip.)

Kita dapat menginstal versi terbaru dari sebuah paket dengan menentukan nama paket:

```
(tutorial-env) C:\Users\HP>python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.5.tar.gz (135 kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```

Menginstall versi paket tertentu dengan memberikan nama paket diikuti oleh `==` dan nomor versi:

```
(tutorial-env) C:\Users\HP>python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Downloading requests-2.6.0-py2.py3-none-any.whl (469 kB)
     ------------------------------------ 469.8/469.8 KB 841.7 kB/s eta 0:00:00
Installing collected packages: requests
Successfully installed requests-2.6.0
```

Jika kita menjalankan kembali perintah ini, `pip` akan melihat bahwa *versi yang diminta sudah diinstal* dan tidak melakukan apa-apa. Kita dapat memberikan nomor versi yang berbeda untuk mendapatkan versi tersebut, atau Kita dapat menjalankan untuk memutakhirkan packages ke versi terbaru: `pip install --upgrade`

```
(tutorial-env) C:\Users\HP>python -m pip install --upgrade requests
Requirement already satisfied: requests in c:\users\hp\tutorial-env\lib\site-packages (2.6.0)
Collecting requests
  Downloading requests-2.27.1-py2.py3-none-any.whl (63 kB)
     -------------------------------------- 63.1/63.1 KB 178.1 kB/s eta 0:00:00
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.9-py2.py3-none-any.whl (138 kB)
     ------------------------------------ 139.0/139.0 KB 515.0 kB/s eta 0:00:00
Collecting certifi>=2017.4.17
  Downloading certifi-2021.10.8-py2.py3-none-any.whl (149 kB)
     ------------------------------------ 149.2/149.2 KB 387.1 kB/s eta 0:00:00
Collecting charset-normalizer~=2.0.0
  Using cached charset_normalizer-2.0.12-py3-none-any.whl (39 kB)
Collecting idna<4,>=2.5
  Downloading idna-3.3-py3-none-any.whl (61 kB)
     -------------------------------------- 61.2/61.2 KB 652.8 kB/s eta 0:00:00
Installing collected packages: certifi, urllib3, idna, charset-normalizer, requests
  Attempting uninstall: requests
    Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed certifi-2021.10.8 charset-normalizer-2.0.12 idna-3.3 requests-2.27.1 urllib3-1.26.9
```

`pip uninstall` diikuti oleh satu atau lebih nama paket akan menghapus paket dari virtual environment.


`pip show` akan menampilkan informasi tentang paket tertentu:

```
(tutorial-env) C:\Users\HP>pip show requests
Name: requests
Version: 2.27.1
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Author-email: me@kennethreitz.org
License: Apache 2.0
Location: c:\users\hp\tutorial-env\lib\site-packages
Requires: certifi, charset-normalizer, idna, urllib3
Required-by:
```


`pip list` akan menampilkan semua paket yang diinstal di lingkungan virtual:

```
(tutorial-env) C:\Users\HP>pip list
Package            Version
------------------ ---------
certifi            2021.10.8
charset-normalizer 2.0.12
idna               3.3
pip                22.0.4
requests           2.27.1
setuptools         58.1.0
urllib3            1.26.9
```

`pip freeze` akan menghasilkan daftar paket yang diinstal serupa, tetapi output menggunakan format yang diharapkan. Konvensi umum adalah meletakkan daftar ini dalam `file:pip installrequirements.txt`

```
(tutorial-env) C:\Users\HP>pip freeze > requirements.txt
(tutorial-env) C:\Users\HP>type requirements.txt
certifi==2021.10.8
charset-normalizer==2.0.12
idna==3.3
requests==2.27.1
urllib3==1.26.9
```

Kemudian `requirements.txt` dapat dikomit ke kontrol versi dan dikirimkan sebagai bagian dari aplikasi. Pengguna kemudian dapat menginstal semua paket yang diperlukan dengan : `install -r`

```
(tutorial-env) C:\Users\HP>python -m pip install -r requirements.txt
Requirement already satisfied: certifi==2021.10.8 in c:\users\hp\tutorial-env\lib\site-packages (from -r requirements.txt (line 1)) (2021.10.8)
Requirement already satisfied: charset-normalizer==2.0.12 in c:\users\hp\tutorial-env\lib\site-packages (from -r requirements.txt (line 2)) (2.0.12)
Requirement already satisfied: idna==3.3 in c:\users\hp\tutorial-env\lib\site-packages (from -r requirements.txt (line 3)) (3.3)
Requirement already satisfied: requests==2.27.1 in c:\users\hp\tutorial-env\lib\site-packages (from -r requirements.txt (line 4)) (2.27.1)
Requirement already satisfied: urllib3==1.26.9 in c:\users\hp\tutorial-env\lib\site-packages (from -r requirements.txt (line 5)) (1.26.9)
```

`pip` memiliki lebih banyak pilihan. Lihat panduan Instalasi Modul Python untuk dokumentasi lengkap untuk `pip`. Ketika kita telah menulis sebuah paket dan ingin membuatnya tersedia di Python Package Index.


# CONDA

## Definisi dan Fungsi

Conda adalah sistem manajemen paket sumber terbuka dan sistem manajemen lingkungan yang berjalan di Windows, macOS, dan Linux. Conda dengan cepat menginstal, menjalankan, dan memperbarui paket dan dependensinya. Conda dengan mudah membuat, menyimpan, memuat, dan beralih antar envirolment di komputer lokal. Itu dibuat untuk program Python tetapi dapat mengemas dan mendistribusikan perangkat lunak untuk bahasa apa pun.

Dalam konfigurasi default, conda dapat menginstal dan mengelola lebih dari 7.500 paket di repo.anaconda.com yang dibuat, ditinjau, dan dikelola oleh Anaconda.

Conda dapat dikombinasikan dengan sistem integrasi berkelanjutan seperti Travis CI dan AppVeyor untuk menyediakan pengujian kode Anda yang sering dan otomatis.

Conda juga disertakan dalam Anaconda Enterprise , yang menyediakan paket perusahaan di tempat dan manajemen lingkungan untuk Python, R, Node.js, Java, dan tumpukan aplikasi lainnya. Conda juga tersedia di conda-forge , community channel.


## Konsep Dasar

### Conda commands

Perintah `conda` adalah antarmuka utama untuk mengelola instalasi berbagai paket. Bisa:

* Kueri dan cari indeks paket Anaconda dan instalasi Anaconda saat ini.
* Buat lingkungan conda baru.
* Instal dan perbarui paket ke lingkungan conda yang ada.

**TIPS**
*Kita dapat menyingkat banyak opsi perintah yang sering digunakan yang didahului oleh 2 tanda hubung ( `--` ) menjadi hanya 1 tanda hubung dan huruf pertama dari opsi tersebut. Jadi `--name` dan `-n` adalah sama, dan `--envs` dan `-e` adalah sama.*

### Conda Packages

Paket conda adalah file tarball terkompresi (.tar.bz2) atau file .conda yang berisi:

* perpustakaan tingkat sistem.
* Python atau modul lainnya.
* program yang dapat dieksekusi dan komponen lainnya.
* metadata di bawah info/direktori.
* kumpulan file yang diinstal langsung menjadi installawalan.


### Format file conda

Format file .conda diperkenalkan di conda 4.7 sebagai alternatif tarball yang lebih ringkas, dan dengan demikian lebih cepat.

Format file .conda terdiri dari wadah format ZIP luar yang tidak terkompresi, dengan 2 file .tar terkompresi dalam.

Untuk dukungan format kompresi internal awal format .conda,  Zstandard (zstd).


### Menggunakan Packages

* Mencari Packages
`conda search scipy`

* Menginstall Packages
`conda install scipy`

* Membuat paket setelah menginstal conda-build
`conda build my_fun_package`


### Struktur Packages

```
.
├── bin
│   └── pyflakes
├── info
│   ├── LICENSE.txt
│   ├── files
│   ├── index.json
│   ├── paths.json
│   └── recipe
└── lib
    └── python3.5
```

* bin berisi binari yang relevan untuk paket tersebut.
* lib berisi file perpustakaan yang relevan (mis. file .py).
* info berisi metadata paket.


### Metapackages

Ketika paket conda digunakan untuk metadata saja dan tidak berisi file apa pun, itu disebut sebagai metapackage. Metapackage mungkin berisi dependensi ke beberapa inti, perpustakaan tingkat rendah dan dapat berisi tautan ke file perangkat lunak yang diunduh secara otomatis saat dijalankan. Metapackages digunakan untuk menangkap metadata dan membuat spesifikasi paket yang rumit menjadi lebih sederhana.

Contoh metapackage adalah **"anaconda"**, yang mengumpulkan semua paket di penginstal Anaconda. Perintah menciptakan lingkungan yang sama persis dengan apa yang akan dibuat dari penginstal Anaconda. Anda dapat membuat paket meta dengan perintah. Sertakan nama dan versi dalam perintah : 
`.conda create -n envname anaconda`  `conda metapackage`


## Menginstall dengan conda

Untuk menginstal paket conda, di terminal atau Anaconda Prompt, jalankan:

```
conda install [packagename]
```

Menginstal file paket conda ke dalam environment dapat dianggap sebagai mengubah direktori ke environment, dan kemudian mengunduh dan mengekstrak artefak dan dependensinya --- semua dengan satu perintah. `conda install [packagename]`

## Pembaruan Conda

`conda update` digunakan untuk memperbarui ke versi terbaru yang kompatibel. dapat digunakan untuk menginstal versi apa pun. `conda install` 

Contoh:

* Jika Python 2.7.0 saat ini terinstal, dan versi terbaru Python 2 adalah 2.7.5, maka instal Python 2.7.5. Itu tidak menginstal Python 3.conda update python
* Jika Python 3.7.0 saat ini terinstal, dan versi terbaru Python adalah 3.9.0, maka instal Python 3.9.0.conda install python=3

Conda menggunakan aturan yang sama untuk paket lain. selalu menginstal versi tertinggi dengan nomor versi utama yang sama, sedangkan selalu menginstal versi tertinggi.


# Getting started with conda
Conda adalah pengelola paket dan pengelola environment andal yang digunakan dengan perintah baris perintah di Anaconda Prompt untuk Windows, atau di jendela terminal untuk macOS atau Linux.

Sebelum memulai pastikan sudah [menginstall Anaconda](https://docs.anaconda.com/anaconda/install/)

## Memulai Conda pada Windows

* Dari menu Start, cari dan buka "Anaconda Prompt."


## Mengelola Conda

Verifikasi bahwa conda diinstal dan berjalan di sistem dengan mengetik:

```
conda --version
```

Perbarui conda ke versi saat ini. Ketik berikut ini:

```
conda update conda
```

Conda membandingkan versi dan kemudian menampilkan apa yang tersedia untuk diinstal.
Jika versi conda yang lebih baru tersedia, ketik `y` untuk memperbarui:

```
Proceed ([y]/n)? y
```

## Mengelola environments

Conda memungkinkan untuk membuat environment terpisah yang berisi file, paket, dan dependensinya yang tidak akan berinteraksi dengan environment lain.

Saat Kita mulai menggunakan conda, Anda sudah memiliki environment default bernama `base`. Kita tidak ingin memasukkan program ke dalam environment dasar Anda. Buat environment terpisah untuk menjaga program Anda tetap terisolasi satu sama lain.

1. Membuat environment baru dan instal paket di dalamnya.
dengan nama environment `snowflakes` :

```
conda create --name snowflakes biopython
```

2. menggunakan, atau "mengaktifkan" environment baru

```
conda activate snowflakes
```

3. melihat daftar semua environment

```
conda info --envs
```

tampilan daftar environment

```
conda environments:

    base           /home/username/Anaconda3
    snowflakes   * /home/username/Anaconda3/envs/snowflakes

```

4. Ubah environment saat ini kembali ke default (basis): 

```
conda activate
```

## Mengelola Packages

Di bagian ini memeriksa paket mana yang telah diinstal, memeriksa mana yang tersedia dan mencari paket tertentu dan menginstalnya.

1.  Untuk menemukan paket yang telah terinstal, aktifkan terlebih dahulu environment yang ingin Anda cari.

2. Periksa untuk melihat apakah paket yang belum Anda instal bernama "beautifulsoup4" tersedia dari repositori Anaconda (harus terhubung ke Internet):

```
conda search beautifulsoup4
```

3. Install Packages

```
conda install beautifulsoup4
```

4. Periksa untuk melihat apakah program yang baru diinstal ada 

```
conda list
```
