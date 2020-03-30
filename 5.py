flag = True

while flag:
    try:
        revenue = int(input('Input amount of revenue:' ))
        flag = False
    except:
        print('No number entered!!!')

flag = True

while flag:
    try:
        costs = int(input('Input amount of costs:' ))
        flag = False
    except:
        print('No number entered!!!')

a = revenue - costs

if a > 0:
    print(f'Profit amounted to: {a}')
    print(f'Profitability: {revenue/costs:.4f}')

    flag = True
    while flag:
        try:
            count_employees = int(input('Input the number of employees:'))
            flag = False
        except:
            print('No number entered!!!')
    print(f'Profit per employee:{(revenue/costs)/count_employees:.4f}')
elif a < 0:
    print(f'Loss amounted to: {abs(a)}')
else:
    print('Revenue=costs')
#