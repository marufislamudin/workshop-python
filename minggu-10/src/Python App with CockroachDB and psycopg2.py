# step 2 Kloning repo GitHub kode sampel:

'''
git clone https://github.com/cockroachlabs/hello-world-python-psycopg2
'''

# step 3 Instal driver psycopg2

'''
pip install psycopg2-binary
'''

# step 4 Jalankan kode

#setel DATABASE_URL envirolment variabel  ke string koneksi ke cluster CockroachDB Cloud:
'''
export DATABASE_URL="{connection-string}"
'''

#masuk direktori
'''
cd hello-world-python-psycopg2
'''

# menjalankan kode
'''
python example.py
'''

#output:
"""
Balances at Fri Oct 30 18:27:00 2020:
(1, 1000)
(2, 250)
Balances at Fri Oct 30 18:27:00 2020:
(1, 900)
(2, 350)
"""