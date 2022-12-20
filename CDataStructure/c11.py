int1 = int(input('กรุณากรอกจำนวนเต็มตัวที่1 (int) : '))
float2 = float(input('กรุณากรอกจำนวนจริงที่2 (float) : '))
a = int1 + float2
b = int1 - float2
c = int1 * float2
d = int1 / float2
print('ผลบวก = %s, ชนิพของข้อมูล = %s' % (a, type(a)))
print('ผลลบ = %s, ชนิพของข้อมูล = %s' % (b, type(b)))
print('ผลคูณ = %s, ชนิพของข้อมูล = %s' % (c, type(c)))
print('ผลหาร = %s, ชนิพของข้อมูล = %s' % (d, type(d)))
