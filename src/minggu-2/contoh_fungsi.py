def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# fungsi pertama, standard_arg, 
standard_arg(2)
standard_arg(arg=2)

#Fungsi kedua pos_only_arg
pos_only_arg(1)
pos_only_arg(arg=1)

#Fungsi ketiga kwd_only_args
kwd_only_arg(3)
kwd_only_arg(arg=3)

# menggunakan ketiga konvensi pemanggilan dalam definisi fungsi yang sama
combined_example(1, 2, 3)
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
combined_example(pos_only=1, standard=2, kwd_only=3)

def foo(name, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2})

def foo(name, /, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2})


# 4.8.4 
#fungsi dapat dipanggil dengan sejumlah argumen yang berubah-ubah.
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
concat("earth", "mars", "venus", sep=".")

# 4.8.5 
# Unpacking Argument Lists
list(range(3, 6))
args = [3, 6]
list(range(*args))

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

# 4.8.6. 
# Lambda Expressions
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
f(1)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs

# 4.8.7. 
# Documentation Strings
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

#4.8.8. 
# Function Annotations
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
