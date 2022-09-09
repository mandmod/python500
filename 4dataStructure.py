print('<---------- Data Structure =>Numeric=>Integer ---------->')
print()
a = 1
b = 2
print(type(a))
print(type(b))
print()
print('<---------- Data Structure =>Numeric=>Floating-Point Number---------->')
print()
c = 0.5
d = 3 / 4
print(type(c))
print(type(d))
print(d)
print()
print('<---------- Data Structure =>Numeric=>boolean---------->')
print()
t = True
f = False
print(type(t))
print(type(f))
print()
print('<---------- Data Structure =>Numeric=>Complex Number---------->')
print()
z = 1 + 2j
print(z.real)
print(z.imag)
print()
print('<---------- Data Structure =>String=>Create String---------->')
print()
char1 = 'Hello, world!'
char2 = '0123456789'
print(type(char1))
print(type(char2))
print()
char3 = '0123456789'
print(char3[0])
print(char3[1])
print(char3[-1])
print(char3[-2])
print(char3[3:])
print(char3[:7])
print(char3[3:7])
print()
print('<---------- Data Structure =>string+Replace ---------->')
print()
char4 = 'abc'
print(char4)
print(char4.replace('a', 'A'))
print(char4.replace('bc', 'DE'))
print()
print('<---------- Data Structure =>string+len ---------->')
print()
char5 = '12345'
print(len(char5))
print()
print('<---------- Data Structure =>string+in ---------->')
print()
char6 = 'Python'
print('P' in char6)
print('p' in char6)
print()
print('<---------- Data Structure =>string+split ---------->')
print()
char7 = 'one-two-three'
print(char7.split('-'))
char8 = 'I love coding'
print(char8.split(' '))
print()
print('<---------- Data Structure =>string+Concatenation---------->')
print()
char9 = 'ab'
char10 = 'cd'
char11 = 'ef'
print(char9 + char10)
print(char9 + char11 + char10)
print()
print('<---------- Data Structure =>List=>Create List --------->')
print()
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd']
list3 = [1, 2, 3, 'a', 'b', 'c']
print(type(list1))
print(type(list2))
print(type(list3))
print()
print('<---------- Data Structure =>List=>Read List--------->')
list4 = [1, 2, 3, 'a', 'b', 'c']
print(list4[0])
print(list4[-1])
print(list4[-2])
print(list4[3:])
print(list4[:5])
print(list4[3:5])
print()
print('<---------- Data Structure =>List=>Update List : Replace --------->')
list6 = [1, 2, 3, 'a', 'b', 'c']
print(list6)
list6[0] = 0
print(list6)
list6[-1] = 'x'
print(list6)
print()
print('<---------- Data Structure =>List=>Update list : append --------->')
print()
list7 = [1, 2, 3, 'a', 'b', 'c']
print(list7)
list7.append('d')
print(list7)
list7.append('e')
print(list7)
print()
print('<---------- Data Structure =>List=>Update list : extend --------->')
print()
list8 = [1, 2, 3]
list9 = ['a', 'b', 'c']
list8.extend(list9)
print(list8)
print()
print('<---------- Data Structure =>List=>Update list : insert --------->')
list10 = [1, 2, 3, 'a', 'b', 'c']
print(list10)
list10.insert(1, 'one')
print(list10)
print()
print('<---------- Data Structure =>List=>Update list : del --------->')
print()
list11 = [1, 2, 3, 'a', 'b', 'c']
print(list11)
del list11[2]
print(list11)
del list11[-2]
print(list11)
print()
print('<---------- Data Structure =>List=>Update list : remove --------->')
print()
list12 = [1, 2, 3, 'a', 'b', 'c']
print(list12)
list12.remove(1)
print(list12)
list12.remove('a')
print(list12)
print()
print('<---------- Data Structure =>List=>Update list : Clear --------->')
list13 = [1, 2, 3, 'a', 'b', 'c']
print(list13)
list13.clear()
print(list13)
print()
print('<---------- Data Structure =>List + sort --------->')
print()
list14 = [1, 5, 4, 2, 3]
print(list14)
list14.sort()
print(list14)
list14.sort(reverse=True)
print(list14)
list14 = (1, 5, 4, 2, 3)
sorted_list14 = sorted(list14)
print(sorted_list14)
sorted_list14 = sorted(list14, reverse=True)
print(sorted_list14)
print()
print('<---------- Data Structure =>List + Len -------->')
print()
list15 = [1, 2, 3, 'a', 'b', 'c']
print(list15)
print(len(list15))
list16 = ['a', 'b', 'c', 'd', 'e']
print(list16)
print(len(list16))
print()
print('<---------- Data Structure =>List +in --------->')
print()
list17 = [1, 2, 3, 'a', 'b', 'c']
print(list17)
print('b' in list17)
print('4' in list17)
print()
print('<---------- Data Structure =>Tuple --------->')
print()
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c', 'd')
tuple3 = (1, 2, 3, 'a', 'b', 'c')
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print()
print('<---------- Data Structure =>Tuple Read ---------->')
tuple4 = tuple3
print(tuple4[0])
print(tuple4[-1])
print(tuple4[-2])
print(tuple4[3:])
print(tuple4[:5])
print(tuple4[3:5])
print()
print('<---------- Data Structure =>Tuple len ---------->')
print()
tuple6 = tuple3
print(tuple6)
print(len(tuple6))
tuple7 = tuple2
print(tuple7)
print(len(tuple7))
print()
print('<---------- Data Structure =>Tuple in ---------->')
tuple8 = tuple3
print('b' in tuple8)
print('4' in tuple8)
print()
print('<---------- Data Structure =>Dictionary=>Create---------->')
print()
dict1 = {'firstname': 'John', 'lastname': 'Doe', 'age': 32}
dict2 = {'firstname': 'John Done', 'hobby': ['coding', 'study']}
print(type(dict1))
print(type(dict2))
print()
print('<---------- Data Structure =>Dictionary => Read ---------->')
dict3 = {'firstname': 'John', 'lastname': 'Doe', 'age': 32}
print(dict3)
print(dict3['firstname'])
print(dict3['age'])
print()
print('<---------- Data Structure =>Dictionary => Updat ---------->')
dict4 = {'firstname': 'John', 'lastname': 'Doe', 'age': 32}
print(dict4)
dict4['firstname'] = 'Mario'
print(dict4)
print()
print('<---------- Data Structure =>Dictionary => add ---------->')
print()
dict5 = {'firstname': 'John', 'lastname': 'Doe', 'age': 32}
print(dict5)
dict5['blood_group'] = 'O'
print(dict5)
print()
print('<---------- Data Structure =>Dictionary => update ---------->')
dict6 = {'firstname': 'John', 'lastname': 'Doe', 'age': 32}
print(dict6)
dict6.update({'blood_group': 'O', 'height': 100})
print(dict6)
print()
print('<---------- Data Structure =>Dictionary => Del--------->')
print()
dict7 = {'firstname': 'John', 'lastname': 'Doe', 'age': 32}
print(dict7)
del dict7['lastname']
print(dict7)
print()
print('<---------- Data Structure =>Dictionary => Clear--------->')
print()
dict8 = {'firstname': 'John', 'lastname': 'Doe', 'age': 32}
print(dict8)
dict8.clear()
print(dict8)
print()
print('<---------- Data Structure =>Dictionary => len  --------->')
print()
dict9 = {'firstname': 'John', 'lastname': 'Doe', 'age': 32}
print(len(dict9))
print(len(dict9.keys()))
print(len(dict9.values()))
print()
print('<---------- Data Structure =>Dictionary => in  --------->')
print()
dict10 = {'firstname': 'John', 'lastname': 'Doe', 'age': 32}
print(dict10)
print('firstname' in dict10)
print('firstname' in dict10.keys())
print('john' in dict10.values())
print('weight' in dict10)
print('weight' in dict10.keys())
print('70' in dict10.values())
print()
print('<---------- Data Structure => Set => Create Set--------->')
print()
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 'a', 'b', 'c'}
print(type(set1))
print(type(set2))
print()
print('<---------- Data Structure => Set => Read set --------->')
print()
set3 = {'a', 'b', 'c', 'd', 'e'}
print(set3)
for i in set3:
    print(i)
print()
print('<---------- Data Structure => Set => update set : add --------->')
print()
set4 = set3
set4.add(1)
print(set4)
print()
print('<---------- Data Structure => Set => update set : update --------->')
print()
set5 = set3
set5.update({1, 2, })
print(set5)
print()
print('<---------- Data Structure => Set => update set : remove --------->')
print()
set6 = set3
print(set6)
set6.remove('a')
print(set6)
set6.remove('c')
print(set6)
print()
print('<---------- Data Structure => Set => update set : clear --------->')
print()
set7 = set3
print(set7)
set7.clear()
print(set7)
print()
print('<---------- Data Structure => Set => set + len --------->')
print()
set8 = {1, 2, 3, 4, 5}
len(set8)
print(len(set8))
print()
print('<---------- Data Structure => Set => set + in --------->')
print()
set9 = set8.copy()
print(set9)
print(1 in set9)
print('a' in set9)
print()
print('<---------- Data Structure => Set => set + Union ---------->')
print()
setA = {1, 2, 3, 4, 5}
setB = {3, 4, 5, 6, 7}
print(setA | setB)
print()
print('<---------- Data Structure => Set => set + Intersection ---------->')
print()
setA = {1, 2, 3, 4, 5}
setB = {3, 4, 5, 6, 7}
print(setA & setB)
print()
print('<---------- Data Structure => Set => set + Difference ---------->')
setA = {1, 2, 3, 4, 5}
setB = {3, 4, 5, 6, 7}
print(setA - setB)
print(setB - setA)
print()
print('<---------- Data Structure => Set => set + Symmetric Difference ---------->')
print()
setA = {1, 2, 3, 4, 5}
setB = {3, 4, 5, 6, 7}
print(setA ^ setB)
