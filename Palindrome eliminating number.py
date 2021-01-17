def pal_lst(lst1):
    
    new_lst = []
    for item in lst1:
        if(('1' in item) or ('2' in item) or ('3' in item) or ('4' in item) or ('5' in item) or ('6' in item) or ('7' in item) or ('8' in item) or ('9' in item) or ('0' in item)):
            continue
        elif((item.lower()) == (item[::-1].lower())):
            new_lst.append(item)
    print(' '.join(new_lst))

if __name__ == "__main__":
    
    n = input("Provide strings: ")
    lst1 = n.split()
    pal_lst(lst1)