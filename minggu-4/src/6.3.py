# Fungsi bawaan dir()digunakan untuk mengetahui nama mana yang didefinisikan oleh modul.
import fibo, sys
dir(fibo)

dir(sys)  

#Tanpa argumen, buat dir()daftar nama yang telah Anda tetapkan saat ini
a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
dir()

#dir()tidak mencantumkan nama fungsi dan variabel bawaan
#Jika ingin daftarnya, didefinisikan dalam modul standar builtins:
import builtins
dir(builtins)