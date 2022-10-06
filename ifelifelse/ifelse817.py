hour = int(input('จำนวนชั่วโมง ที่จอดรถ: = '))
minute = int(input('จำนวนนาที ที่จอดรถ : ='))
if (hour < 0) or (minute < 0):
    print('โปรดใส่ข้อมูลที่ไม่ติดลง')
else:
    if minute > 0:
        hour = hour + 1
    fee = (hour - 1) * 30
    print(fee)
