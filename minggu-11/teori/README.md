# FLASK
`Flask` adalah kerangka kerja aplikasi web WSGI yang ringan . Ini dirancang untuk memulai dengan cepat dan mudah, dengan kemampuan untuk meningkatkan aplikasi yang kompleks. Ini dimulai sebagai pembungkus sederhana di sekitar Werkzeug dan Jinja dan telah menjadi salah satu kerangka kerja aplikasi web Python paling populer.

`Flask` menawarkan saran, tetapi tidak menerapkan dependensi atau tata letak proyek apa pun. Terserah pengembang untuk memilih alat dan perpustakaan yang ingin mereka gunakan. Ada banyak ekstensi yang disediakan oleh komunitas yang memudahkan penambahan fungsionalitas baru.


## Install Flask dengan conda

mengaktifkan environments
```
(base) C:\Users\HP>conda activate workshopy
```

mengistall flask
```
(workshopy) C:\Users\HP>conda install flask
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\HP\miniconda3\envs\workshopy

  added / updated specs:
    - flask


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    certifi-2022.5.18.1        |  py310haa95532_0         157 KB
    click-8.0.4                |  py310haa95532_0         157 KB
    colorama-0.4.4             |     pyhd3eb1b0_0          21 KB
    jinja2-3.0.3               |     pyhd3eb1b0_0         106 KB
    markupsafe-2.0.1           |  py310h2bbff1b_0          24 KB
    ------------------------------------------------------------
                                           Total:         465 KB

The following NEW packages will be INSTALLED:

  click              pkgs/main/win-64::click-8.0.4-py310haa95532_0
  colorama           pkgs/main/noarch::colorama-0.4.4-pyhd3eb1b0_0
  dataclasses        pkgs/main/noarch::dataclasses-0.8-pyh6d0b6a4_7
  flask              pkgs/main/noarch::flask-2.0.3-pyhd3eb1b0_0
  itsdangerous       pkgs/main/noarch::itsdangerous-2.0.1-pyhd3eb1b0_0
  jinja2             pkgs/main/noarch::jinja2-3.0.3-pyhd3eb1b0_0
  markupsafe         pkgs/main/win-64::markupsafe-2.0.1-py310h2bbff1b_0
  werkzeug           pkgs/main/noarch::werkzeug-2.0.3-pyhd3eb1b0_0

The following packages will be UPDATED:

  certifi            pkgs/main/noarch::certifi-2020.6.20-p~ --> pkgs/main/win-64::certifi-2022.5.18.1-py310haa95532_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
click-8.0.4          | 157 KB    | ############################################################################ | 100%
colorama-0.4.4       | 21 KB     | ############################################################################ | 100%
jinja2-3.0.3         | 106 KB    | ############################################################################ | 100%
certifi-2022.5.18.1  | 157 KB    | ############################################################################ | 100%
markupsafe-2.0.1     | 24 KB     | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```

## TUTORIAL
Membuat aplikasi blog dasar yang disebut Flaskr. Pengguna akan dapat mendaftar, masuk, membuat posting, dan mengedit atau menghapus posting mereka sendiri.

### Project Layout

membuat direktori proyek
```
(workshopy) C:\Users\HP>mkdir flask-tutorial

(workshopy) C:\Users\HP>cd flask-tutorial
```

aplikasi flask sederhana dengan satu file

file : hello.py
```
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
```

Namun, ketika sebuah proyek semakin besar, menjadi sangat sulit untuk menyimpan semua kode dalam satu file. Proyek Python menggunakan paket untuk mengatur kode ke dalam beberapa modul yang dapat diimpor jika diperlukan, dan tutorial ini juga akan melakukannya.

Direktori proyek akan berisi:

* `flaskr/`, paket Python yang berisi kode aplikasi dan file Anda.

* `tests/`, direktori yang berisi modul pengujian.

* `venv/`, lingkungan virtual Python tempat Flask dan dependensi lainnya diinstal.

* File instalasi memberi tahu Python cara menginstal proyek Anda.

* Konfigurasi kontrol versi, seperti git . Anda harus membiasakan menggunakan beberapa jenis kontrol versi untuk semua proyek Anda, berapa pun ukurannya.

* File proyek lain yang mungkin Anda tambahkan di masa mendatang.

Tata letak folder proyek:

```
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```

### Application Setup

#### The Application Factory

membuat direktori `flaskr`

```
(workshopy) C:\Users\HP\flask-tutorial>mkdir flaskr
```

membuat file flaskr/__init__.py

```
import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```

`create_app` adalah fungsi pabrik aplikasi.

1. `app = Flask(__name__, instance_relative_config=True)` menciptakan **Flask** instance.

* `__name__` adalah nama modul Python saat ini. Aplikasi perlu mengetahui di mana lokasinya untuk menyiapkan beberapa jalur, dan `__name__` merupakan cara yang nyaman untuk memberitahukannya.

* instance_relative_config=Truememberi tahu aplikasi bahwa file konfigurasi relatif terhadap folder instance . Folder instans terletak di luar flaskrpaket dan dapat menyimpan data lokal yang tidak boleh dikomit ke kontrol versi, seperti rahasia konfigurasi dan file database.

2. `app.config.from_mapping()` menyetel beberapa konfigurasi default yang akan digunakan aplikasi:

* SECRET_KEYdigunakan oleh Flask dan ekstensi untuk menjaga keamanan data. Ini diatur untuk 'dev'memberikan nilai yang nyaman selama pengembangan, tetapi harus diganti dengan nilai acak saat digunakan.

* DATABASEadalah jalur tempat file database SQLite akan disimpan. Itu di bawah app.instance_path, yang merupakan jalur yang telah dipilih Flask untuk folder instance. Anda akan mempelajari lebih lanjut tentang database di bagian berikutnya.

3. a`pp.config.from_pyfile()` menimpa konfigurasi default dengan nilai yang diambil dari `config.py` file di folder instance jika ada. Misalnya, saat menerapkan, ini dapat digunakan untuk mengatur file `SECRET_KEY`.

* `test_config` juga dapat diteruskan ke pabrik, dan akan digunakan sebagai pengganti konfigurasi instans. Ini agar pengujian yang akan Anda tulis nanti dalam tutorial dapat dikonfigurasi secara independen dari nilai pengembangan apa pun yang telah Anda konfigurasikan.

4. `os.makedirs()` memastikan bahwa ada **app.instance_path** . Flask tidak membuat folder instance secara otomatis, tetapi perlu dibuat karena proyek Anda akan membuat file database SQLite di sana.

5. `@app.route()` membuat rute sederhana sehingga Anda dapat melihat aplikasi bekerja sebelum masuk ke tutorial selanjutnya. Ini membuat koneksi antara URL /hellodan fungsi yang mengembalikan respons, string dalam kasus ini.`'Hello, World!'`

#### Run Aplikasi

Dari terminal, beri tahu Flask di mana menemukan aplikasi yaitu pada folder `flaskr`, lalu jalankan dalam mode **development**. flask-tutorialIngat, kemudian masukkan perintah flask run

```

(workshopy) C:\Users\HP\flask-tutorial> set FLASK_APP=flaskr

(workshopy) C:\Users\HP\flask-tutorial>set FLASK_ENV=development

(workshopy) C:\Users\HP\flask-tutorial>flask run
 * Serving Flask app 'flaskr' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 555-183-053
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [24/May/2022 00:11:18] "GET /hello HTTP/1.1" 200 -
127.0.0.1 - - [24/May/2022 00:11:19] "GET /favicon.ico HTTP/1.1" 404 -
```

Kunjungi http://127.0.0.1:5000/hello di browser dan Anda akan melihat "Halo, Dunia!" pesan.