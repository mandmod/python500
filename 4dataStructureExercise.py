from audioop import reverse
from turtle import clear

from unicodedata import numeric

numeric1 = 5
print('ชนิดของข้อมูล = ', type(numeric1))
print('numeric1 = ', numeric1)
print()
numeric2 = -3
print('numeric2 = ', numeric2)
print('ชนิดของข้อมูล = ', type(numeric2))
print()
numeric3 = 0
print('numeric3 = ', numeric3)
print('ชนิดของข้อมูล = ', type(numeric3))
print()
'''numeric = int(input('กรุณากรอกข้อมูล'))
print('numeric = ', numeric)
print(type(numeric))
'''
print()
numeric1 = 5.0
print('numeric1 = ', numeric1)
print(type(numeric1))
print()
numeric2 = -3.1
print('numeric2 = ', numeric2)
print(type(numeric2))
print()
numeric3 = 0.0
print('numeric3 = ', numeric3)
print(type(numeric3))
print()
'''numeric4 = float(input('กรุณากรอกข้อมูล'))
print('numeric4 = ', numeric4)
print(type(numeric4))
print()
'''
'''
int1 = int(input('กรุณากรอกจำนวนเต็มตัวที่ 1 (int1) : '))
int2 = int(input('กรุณากรอกจำนวนเต็มตัวที่ 2 (int2) : '))
a = int1 + int2
b = int1 - int2
c = int1 * int2
d = int1 / int2
print()
print('ผลบวก = %s, ชนิดของข้อมูล = %s' % (a, type(a)))
print('ผลลย = %s, ชนิดของข้อมูล = %s' % (b, type(b)))
print('ผลคูณ = %s, ชนิดของข้อมูล = %s' % (c, type(c)))
print('ผลหาร = %s, ชนิดของข้อมูล = %s' % (d, type(d)))
print()
'''
'''
float1 = float(input('กรุณากรอกจำนวนจริงตัวที่ 1 (float1) : '))
float2 = float(input('กรุณากรอกจำนวนจริงตัวที่ 2 (float2) : '))
a = float1 + float2
b = float1 - float2
c = float1 * float2
d = float1 / float2
print()
print('ผลบวก = %s, ชนิดของข้อมูล = %s' % (a, type(a)))
print('ผลลย = %s, ชนิดของข้อมูล = %s' % (b, type(b)))
print('ผลคูณ = %s, ชนิดของข้อมูล = %s' % (c, type(c)))
print('ผลหาร = %s, ชนิดของข้อมูล = %s' % (d, type(d)))
print()
'''
'''
int1 = int(input('กรุณากรอกจำนวนเต็มตัวที่ 1 (int1) : '))
float1 = float(input('กรุณากรอกจำนวนจริงตัวที่ 2 (float1) : '))
a = int1 + float1
b = int1 - float1
c = int1 * float1
d = int1 / float1
print()
print('ผลบวก = %s, ชนิดของข้อมูล = %s' % (a, type(a)))
print('ผลลย = %s, ชนิดของข้อมูล = %s' % (b, type(b)))
print('ผลคูณ = %s, ชนิดของข้อมูล = %s' % (c, type(c)))
print('ผลหาร = %s, ชนิดของข้อมูล = %s' % (d, type(d)))
print()
'''
logic1 = True
print(logic1)
print(type(logic1))
print()
logic2 = False
print(logic2)
print(type(logic2))
print()
logic1 = True
logic2 = False
print(logic1 and logic2)
print()
logic1 = True
logic2 = False
print(logic1 or logic)
print()
complex1 = 1 + 2j
print('complex1 = ', complex1)
print(type(complex1))
print()
complex1 = 1 + 2j
print(complex1.real)
print(complex1.imag)
print()
string1 = 'Python'
print(string1)
print(type(string1))
print(string1[0])
print(string1[1])
print(string1[-1])
print(string1[-2])
print(string1[2])
print(string1[3])
print(string1[1:4])
print(string1[2:-1])
print(string1[2:])
print(string1[-4:5])
print(string1[-6:5])
print(string1[-4:-1])
print()
# text1 = input('กรุณากรอกข้อมูล')
text1 = 'Python'
print(text1)
print(len(text1))
print()
# text1 = input('กรุณากรอกข้อมูล')
text1 = 'Python'
print(text1)
print('ก' in text1)
print()
# string1 = input('String1 : ')
# string2 = input('String2 : ')
string1 = 'happy'
string2 = 'app'
print(string2 in string1)
print()
# string1 = input('Please insert string : ')
string1 = 'a python string with a'
print(string1.replace('a', 'A'))
print()
# string1 = input('Please insert string : ')
string1 = 'a python string with a python'
print(string1)
string2 = string1.replace('a', 'A')
print(string2)
print()
# string1 = input('Please insert string : ')
sentence = 'We love Python'
# sentence = sentence.split(' ')
print(sentence.split(' '))
print(sentence)
print()
# sentence = input('Please insert sentence : ')
# c = input('Please insert sentence :')
sentence = 'Py-thon'
c = '-'
print(sentence.split(c))
print()
# str1 = input('Please insert string1')
# str2 = input('Please insert string2')
str1 = 'Fri'
str2 = 'day'
print(str1 + str2)
print()
list1 = [0, 1, 2, 'a', 'b', 'c']
print('list1 = ', list1)
print(type(list1))
print()
list1 = [0, 1, 2, 'a', 'b', 'c']
print(list1[2])
print(list1[-3])
print(list1[0])
print(list1[4])
print(list1[2:4])
print(list1[1:-1])
print(list1[3:])
print(list1[:3])
list2 = ['ant', 'bird', 'cat', 'dog', 'eagle']
print(list2)
list2[3] = 'duck'
print(list2)
print(51)
list2 = ['ant', 'bird', 'cat', 'dog', 'eagle']
list2[0] = 'ape'
print(list2)
print(52)
list2 = ['ant', 'bird', 'cat', 'dog', 'eagle']
list2.append('fish')
print(list2)
print(53)
# str1 = input('Please insert the text1 : ')
# str2 = input('Please insert the text2 : ')
# str3 = input('Please insert the text3 : ')
list1 = []
str1 = 'fish'
str2 = 'cat'
str3 = 'dog'
print(list1)
list1.append(str1)
print(list1)
list1.append(str2)
print(list1)
list1.append(str3)
print(list1)
print()
print(54)
list3 = ['apple', 'cherry', 'eggfruit']
print(list3)
list3.insert(1, 'banana')
print(list3)
print()
print(55)
print(list3)
list3.insert(-1, 'kiwi')
print(list3)
print()
print(56)
list4 = [0, 4, 2, 3, 1]
list4.sort()
print(list4)
print()
print(57)
list4 = [0, 4, 2, 3, 1]
list4.sort(reverse=True)
print(list4)
print()
print(58)
list4 = [0, 4, 2, 3, 1]
sorted_list4 = sorted(list4)
print(sorted_list4)
print()
print(59)
list4 = [0, 4, 2, 3, 1]
sorted_list4 = sorted(list4, reverse=True)
print(sorted_list4)
print()
print(60)
list5 = ['d', 'a', 'c', 'b', 'e']
list5.sort()
print(list5)
print()
print(61)
list5 = ['d', 'a', 'c', 'b', 'e']
sorted_list5 = sorted(list5, reverse=True)
print(sorted_list5)
print()
print(62)
list1 = ['a', 'b', 'c']
list2 = [0, 1, 2]
list1.extend(list2)
print(list1)
print()
print(63)
list1 = ['a', 'b', 'c']
list2 = [0, 1, 2]
list3 = list1 + list2
print(list1)
print(list2)
print(list3)
print()
print(64)
list1 = [1, 2, 3, 1, 2, 3]
print(list1)
del list1[1]
print(list1)
print()
print(65)
list1 = [1, 2, 3, 1, 2, 3]
del list1[5]
del list1[2]
print(list1)
print(66)
list1 = [1, 2, 3, 1, 2, 3]
list1.remove(1)
print(list1)
print()
print(67)
list1 = [1, 2, 3, 1, 2, 3]
list1.remove(1)
list1.remove(1)
print(list1)
print()
print(68)
list1 = [1, 2, 3, 1, 2, 3]
list1.clear()
print(list1)
list1 = [1, 2, 3, 'a', 'b', 'c']
print(len(list1))
print()
list1 = [0, 1, 2, 3, 4, 5]
list2 = 3
print(list2 in list1)
print()
print(71)
tuple1 = ('America', 'Brazil', 'China', 'Dominican', 'Egypt')
print(tuple1)
print(type(tuple1))
print()
print(72)
tuple1 = ('America', 'Brazil', 'China', 'Dominican', 'Egypt')
print(tuple1[1])
print()
print(73)
tuple1 = ('America', 'Brazil', 'China', 'Dominican', 'Egypt')
print(tuple1[-2])
print()
print(74)
tuple1 = ('America', 'Brazil', 'China', 'Dominican', 'Egypt')
print(tuple1[2])
print(tuple1[-3])
print()
print(75)
tuple1 = ('America', 'Brazil', 'China', 'Dominican', 'Egypt')
print(tuple1[4])
print(tuple1[-1])
print()
print(76)
tuple2 = ('one', 'two', 'three', 1, 2, 3)
print(tuple2[1:4])
print(tuple2[2:-1])
print(tuple2[2:-2])
print(tuple2[:3])
print(tuple2[3:])
print()
print(81)
tuple3 = ('one', 'two', 'three', 'four', 'five')
print(len(tuple3))
print()
print(82)
str1 = 'two'
print(str1 in tuple3)
print()
print(83)
dictionary1 = {'firstname': 'John', 'last_name': 'Doe'}
print(dictionary1)
print(type(dictionary1))
print()
print(84)
print(dictionary1['firstname'])
print(dictionary1['last_name'])
print(86)
print(dictionary1.keys())
print(87)
print(dictionary1.values())
print(88)
print(dictionary1)
dictionary1['firstname'] = 'jane'
print(dictionary1)
print(89)
dictionary1 = {'firstname': 'John', 'last_name': 'Doe'}
dictionary1['ate'] = 32
print(dictionary1)
print(90)
dict1 = {'firstname': 'John', 'last_name': 'Doe'}
dict1['ate'] = 32
dict1['hobby'] = ['coding', 'studying']
print(dict1)
dict1 = {'firstname': 'John', 'last_name': 'Doe'}
dict1.update({'age': 32, 'hobby': ['coding', 'studying']})
print(dict1)
print(91)
dict1 = {}
# str1=input('Please insert str1 : ')
# str2=input('Please insert str2 : ')
str1 = 'key'
str2 = 'value'
dict1[str1] = str2
print(dict1)
print(92)
dict1 = {'firstname': 'John', 'last_name': 'Doe', 'age': 32}
print(dict1)
del dict1['age']
print(dict1)
print(93)
dict1 = {'firstname': 'John', 'last_name': 'Doe', 'age': 32}
dict1.clear()
print(dict1)
print(94)
dict1 = {'firstname': 'John', 'last_name': 'Doe', 'age': 32}
print(len(dict1))
print(95)
dict1 = {'firstname': 'John', 'last_name': 'Doe', 'age': 32}
# str1=input('Please insert str1 : ')
str1 = 'firstname'
print(str1 in dict1.keys())
print(str1 in dict1)
print(96)
dict1 = {'firstname': 'John', 'last_name': 'Doe', 'age': 32}
# str1=input('Please insert str1 : ')
str1 = 'John'
print(str1 in dict1.values())
print(97)
set1 = {1, 2, 3, 'i', 'ii', 'iii'}
print('set1 = ', set1)
print(type(set1))
print(98)
set1 = {1, 2, 3, 'i', 'ii', 'iii'}
for s in set1:
    print(s)
print(99)
set1 = {1, 2, 3, 'i', 'ii', 'iii'}
set1.add('iv')
print(set1)
print(100)
set1 = {1, 2, 3, 'i', 'ii', 'iii'}
set1.add(1)
print(set1)
print()
print(101)
set1 = set()
print(type(set1))
# str1=input('Please insert str1 : ')
# str2=input('Please insert str2 : ')
# str3=input('Please insert str3 : ')
str1 = 'ant'
str2 = 'mod2'
str3 = 'cat'
set1.add(str1)
set1.add(str2)
set1.add(str3)
print(set1)
print()
print(102)
str1 = 'ant'
str2 = 'mod2'
str3 = 'cat'
set1.update({str1, str2, str3})
print(set1)
print()
print(103)
set1 = {1, 2, 3, 'i', 'ii', 'iii'}
print(set1)
set1.remove('i')
print(set1)
print()
print(104)
set1 = {1, 2, 3, 'i', 'ii', 'iii'}
print(len(set1))
print()
print(105)
set1 = {1, 2, 3, 'i', 'ii', 'iii'}
# int1=input('Please insert int1 : ')
int1 = 5
set1.add(int1)
print(set1)
print(int1 in set1)
print()
print(106)
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}
print(set1 | set2)
print()
print(107)
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}
print(set1 & set2)
print()
print(108)
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}
print(set1 - set2)
print()
print(109)
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}
print(set2 - set1)
print()
print(110)
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}
print(set1 ^ set2)
