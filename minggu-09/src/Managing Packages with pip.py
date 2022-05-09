# menginstall versi terbaru dari sebuah paket
(tutorial-env) C:\Users\HP>python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.5.tar.gz (135 kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3

# menginstal versi paket tertentu diikuti dengan no versi
(tutorial-env) C:\Users\HP>python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Downloading requests-2.6.0-py2.py3-none-any.whl (469 kB)
     ------------------------------------ 469.8/469.8 KB 841.7 kB/s eta 0:00:00
Installing collected packages: requests
Successfully installed requests-2.6.0


# mengupgrade paket  ke versi yang terbaru
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

# menampilkan informasi packages
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

# menampilkan semua packages yang diinstall
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

# menampilkan packages yang diinstall
# dengan menggunakan pip freeze
(tutorial-env) C:\Users\HP>pip freeze > requirements.txt
(tutorial-env) C:\Users\HP>type requirements.txt
certifi==2021.10.8
charset-normalizer==2.0.12
idna==3.3
requests==2.27.1
urllib3==1.26.9


# menginstall semua yang diperlukan dengan install-r
(tutorial-env) C:\Users\HP>python -m pip install -r requirements.txt
Requirement already satisfied: certifi==2021.10.8 in c:\users\hp\tutorial-env\lib\site-packages (from -r requirements.txt (line 1)) (2021.10.8)
Requirement already satisfied: charset-normalizer==2.0.12 in c:\users\hp\tutorial-env\lib\site-packages (from -r requirements.txt (line 2)) (2.0.12)
Requirement already satisfied: idna==3.3 in c:\users\hp\tutorial-env\lib\site-packages (from -r requirements.txt (line 3)) (3.3)
Requirement already satisfied: requests==2.27.1 in c:\users\hp\tutorial-env\lib\site-packages (from -r requirements.txt (line 4)) (2.27.1)
Requirement already satisfied: urllib3==1.26.9 in c:\users\hp\tutorial-env\lib\site-packages (from -r requirements.txt (line 5)) (1.26.9)

