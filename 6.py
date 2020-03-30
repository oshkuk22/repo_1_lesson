flag = True

while flag:
    try:
        km = int(input('Input first rezult in km: ' ))
        while km < 0:
            print('Error input')
            km = int(input('Input first rezult in km: '))
        flag = False
    except:
        print('No number entered!!!')

flag = True

while flag:
    try:
        km_2 = int(input('Input second rezult in km: ' ))
        while km_2 < 0 or km_2<km:
            print('Error input')
            km_2 = int(input('Input second rezult in km: '))
        flag = False
    except:
        print('No number entered!!!')

count_days = 0
km_= km

while km_ < km_2:
    km_=km_+km*0.1
    count_days +=1

print(f'on the {count_days}th day, the athlete achieved a result of at least {km_2} km')