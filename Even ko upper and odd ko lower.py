def myfunc(*args):
    for item in args:
        list1 = list(item)
        for pos,item in enumerate(list1):
            if(pos%2 == 0):
                list1[pos] = item.lower()
            else:
                list1[pos] = item.upper()
    strr = ''
    return strr.join(list1)