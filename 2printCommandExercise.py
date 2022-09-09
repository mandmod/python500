print('Hello')
print("Hello")
print()
print('Hello world')
print("Hello world")
print()
print('hello_python')
print("hello_python")
print()
print('Merry X\'Mas')
print("Merry X'Mas")
print()
print('I Want to ask you \"Why don\'t you driver to work ?\"')
print("I Want to ask you \"Why don't you driver to work ?\"")
print()
print('\"I don\'t have a car\"')
print("\"I don't have a car\"")
print()
print('You got a nae job !? That\'s so exciting')
print("You got a nae job !? That's so exciting")
print()
print('สวัดดีวันจันทร์')
print("สวัดดีวันจันทร์")
print()
print('ความแตกต่างระหว่างคนเก่งกับคนไม่เก่ง คือ \"การใช้เวลาว่างให้เป็นประโยชน์\"')
print("ความแตกต่างระหว่างคนเก่งกับคนไม่เก่ง คือ \"การใช้เวลาว่างให้เป็นประโยชน์\"")
print()
print('/\\/\\/\\')
print("/\\/\\/\\")
print()
print('''
a
an
ant''')
print("""
a
an
ant""")
print()
print('''
    *
*   *   *
    *''')
print("""
    *
*   *   *
    *""")
print('''\t*
*\t*\t*\n
\t*''')
print('\t*\n*\t*\t*\n\t*')
print()
print('*\t+\t*\n+\t*\t+\n*\t+\t*')
print()
print('''*\t+\t*
+\t*\t+
*\t+\t*''')
print()
print('''Just because something
things differently from you,
does that mean it\'s not thinking ?''')
print()
print('\\\t\t/\n\tX\n/\t\t\\')
print('''\\\t\t/
\tX
/\t\t\\''')
print()
print(25)
print('%d' % 25)
print()
print('%f' % 100)
print('%.6f' % 100)
print()
print('%s' % 3.141592653589793)
import math

print(math.pi)
from math import pi

print(pi)
print('%.15f' % pi)
print()
a = 2
print(a)
print('%.0f' % a)
print()
a = 12.5
print(a)
print('%.1f' % a)
print()
a = 2
b = 3
print('2 x 3 = ', a * b)
print('2 x 3 = ', + a * b)
print('2 x 3 = ', str(a * b))
print('%d x %d = %d' % (a, b, a * b))
print(a, 'x', b, '=', a * b)
print()
a = 2
b = 3
print('2 + 3 = 3 + 2 = ', a + b)
print('%d + %d = %d + %d = %d' % (a, b, b, a, a + b))
print()
a = 2
b = 3
c = 5
print('%d*(%d+%d) = %d*%d + %d*%d' % (a, b, c, a, b, a, c))
print()
a = 2.4
b = 2.5
print('%s + %s = %.4f' % (a, b, a + b))
print()
a = 5
b = 2
print('%.2f - %.2f = %.4f' % (a, b, a - b))
print()
birthday = 25
print('ฉันเกิดวันที่', birthday, 'ธันวาคม')
print('ฉันเกิดวันที่ %d ธันวาคม' % birthday)
print('ฉันเกิดวันที่ ' + str(birthday) + ' ธันวาคม')
print()
a = 5
b = 100
print('%d เท่าของ %d มีค่าเท่ากับ %d' % (a, b, a * b))
print(a, 'เท่าของ', b, 'มีค่าเท่ากับ', a * b)
print(str(a) + ' เท่าของ ' + str(b) + ' มีค่าเท่ากับ ' + str(a * b))
print()
a = 3.5
print('เขามีเงินเยอะกว่าฉัน %.2f บาท' % a)
print()
a = 5
print('ฉันได้กำไร %d %%' % a)
print()
a = 2
b = 3.5
print('เมื่อวานฉันขาดทุน %d %% วันนี้ฉันได้กำไร %.2f %%' % (a, b))
