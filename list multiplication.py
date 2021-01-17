str1 = input("Give the list: ")
n = str1.split(',')
k = list(range((len(n))))
h = []
j = []
for i,p in zip(n,k):
    if(p == 0):
        h = n[1::]
        mul = 1
        for u in h:
            mul = mul * int(u)
        j.append(mul)
    elif((int(n[-1])) == int(n[p])):
        h = n[0:(len(n)-1)]
        mul = 1
        for u in h:
            mul = mul * int(u)
        j.append(mul)
    else:
        leftmul = 1
        rightmul = 1
        left = n[:p:]
        right = n[p+1::]
        for itm in left:
            leftmul = leftmul * int(itm)
        for itm in right:
            rightmul = rightmul * int(itm)
        j.append(rightmul*leftmul)
print(j)