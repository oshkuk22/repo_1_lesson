flag = True

while flag:
    try:
        number = int(input('Input number:' ))
        flag = False
    except:
        print('No number entered!!!')

print(f'Total:{number+int(str(number)+str(number))+int(str(number)+str(number)+str(number))}')