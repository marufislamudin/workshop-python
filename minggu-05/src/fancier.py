# formatted string literals
year = 2016
event = 'Referendum'
f'Results of the {year} {event}'

# str.format()
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)

# repr() dan str()
s = 'Hello, world.'
str(s)
repr(s)
str(1/7)
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# repr() menambahkan tanda kutip string garis miring terbalik.
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# argumen repr() dapat berupa objek python apapun
repr((x, y, ('spam', 'eggs')))