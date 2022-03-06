# menjalankan modul Python dengan
python fibo.py <arguments>

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

# dapat membuat file dapat digunakan sebagai skrip serta modul yang dapat diimpor
python fibo.py 50
# output
0 1 1 2 3 5 8 13 21 34

# Jika modul diimpor, kode tidak dijalankan
import fibo