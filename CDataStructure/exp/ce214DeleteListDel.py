list11 = [1, 2, 3, 'a', 'b', 'c']
print(list11)
del list11[2]
print(list11)

list11 = [1, 2, 3, 'a', 'b', 'c']
del list11[-2]
print(list11)

list12 = [1, 2, 3, 'a', 'b', 'c']
list12.remove(1)
print(list12)
list12.remove('a')
print(list12)

list13 = [1, 2, 3, 'a', 'b', 'c']
list13.clear()
print(list13)
