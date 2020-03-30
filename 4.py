max_number = 0
flag = True
i = 0
positions=[]

while flag:
    try:
        number = int(input('Input number:' ))
        flag = False
    except:
        print('No number entered!!!')

while i < len(str(number)):

    if int(str(number)[i]) > max_number:
        max_number = int(str(number)[i])

    i += 1


for i in range(len(str(number))):
    if (max_number) == int(str(number)[i]):
        positions.append(i+1)

print(f'Max numeral: {max_number} \nPosition numeral: {positions}\nCount max numeral: {len(positions)}')