number = int(input('Please insert Number : = '))
if number > 0:
    if number % 2 == 0:
        print('positive even')
    else:
        print('positive odd')
elif number < 0:
    if number % 2 == 0:
        print('negative even')
    else:
        print('negative odd')
else:
    print('zero')
