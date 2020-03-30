flag = True

while flag:
    try:
        sec = int(input('Input time in seconds:' ))
        flag = False
    except:
        print('Entered time is not a number!!!')


print(f'{sec//3600:02}:{(sec//60)%60:02}:{sec%60:02}')