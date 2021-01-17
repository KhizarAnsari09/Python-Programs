def Palindrome(strr):
    list1 = strr.split()
    list2 = []
    add = False
    for item1 in list1:
        item2 = ''
        item2 = item1[::-1]
        list2.append(item2)
    for pos,ii in zip(list1,list2):
        if (pos.lower() == ii.lower()):
            print(f'{pos} is Palindrome')
            add = True
        else:
            None
    if (add == False):
        print('No Palindrome')
    else:
        None