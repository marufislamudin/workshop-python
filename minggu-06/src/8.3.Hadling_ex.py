# program yang menangani pengecualian yang dipilih
while true:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("oops! That was no valid number. Try again...")

# klausa pengecualian
except (RuntimeError, TypeError, NameError):
    pass

# Kelas dalam exceptklausa kompatibel dengan pengecualian
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# mencetak pesan kesalahan dan kemudian menaikkan kembali pengecualian
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

#  kode yang harus dijalankan jika klausa try tidak memunculkan eksepsi
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

#Klausa kecuali dapat menentukan variabel setelah nama pengecualian.
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print('x = ', x)
    print('y =' y)

# Penangan eksepsi tidak hanya menangani eksepsi jika terjadi segera di klausa try
def this_fails():
    x = 1/0 
try:
    this_fails()
except ZeroDivisionError as err:
    print('Hadling run-time error:', err)
