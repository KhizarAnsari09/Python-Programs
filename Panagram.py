def panagram(str1):
    nl = []
    alpha = []
    pending = []
    l = list(str1)
    for i in l:
        if(i == ' '):
            l.remove(i)
    for i in l:
        nl.append(i.lower())
    set1 = set(nl)
    nl = list(set1)
    for p in range(97,122):
        alpha.append(chr(p))
    nl.sort()
    for u in nl:
        alpha.remove(u)
    if(len(set1) == 25):
        print("Panagram")
    else:
        print(f"{' '.join(alpha)} absent")
        
        
if __name__ == '__main__':
    str1 = input()
    panagram(str1)