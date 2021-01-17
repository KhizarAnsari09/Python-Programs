list1 = []
n = input('What do you wanna convert to base 17 ?')
n = int(n)
while(n>=1):
    r = n%17
    r = str(r)
    list1.append(r)
    n = n/17
    n = int(n)
for pos,item in enumerate(list1):
    if(item == '10'):
        list1[pos] = 'A'
    elif(item == '11'):
        list1[pos] = 'B'
    elif(item == '12'):
        list1[pos] = 'C'
    elif(item == '13'):
        list1[pos] = 'D'
    elif(item == '14'):
        list1[pos] = 'E'
    elif(item == '15'):
        list1[pos] = 'F'
    elif(item == '16'):
        list1[pos] = 'G'
    else:
        None
print(''.join(list1[::-1]))