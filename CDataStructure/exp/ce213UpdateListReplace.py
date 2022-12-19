list6 = [1, 2, 3, 'a', 'b', 'c']
list6[0] = 0
print(list6)
list6[-1] = 'x'
print(list6)

list7 = [1, 2, 3, 'a', 'b', 'c']
list7.append('d')
print(list7)
list7.append('e')
print(list7)

list8 = [1, 2, 3]
list9 = ['a', 'b', 'c']
list8.extend(list9)
print(list8)

list10 = [1, 2, 3, 'a', 'b', 'c']
list10.insert(1, 'one')
print(list10)
