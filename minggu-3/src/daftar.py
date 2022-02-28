fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.count('tangerine')
fruits.index('banana')
fruits.index('banana', 4)
fruits.reverse()
fruits
fruits.append('grape')
fruits
fruits.sort()
fruits
fruits.pop()

# 5.1.1
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
stack.pop()
stack
stack.pop()
stack.pop()
stack

#5.1.2
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") 
queue.append("Graham")
queue.popleft()
queue.popleft()
queue 

#5.1.3
squares = []
for x in range(10):
    squares.append(x**2)
squares

squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
combs

vec = [-4, -2, 0, 2, 4]
#membuat list baru
[x*2 for x in vec]
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
# apply a function to all the elements
[abs(x) for x in vec]
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]
# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

from math import pi
[str(round(pi, i)) for i in range(1, 6)]


# 5.1.4
matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
[[row[i] for row in matrix] for i in range(4)]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
transposed

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed
