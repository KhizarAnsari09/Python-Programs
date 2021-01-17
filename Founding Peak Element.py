num = [1,3,2,2,2,2,5,4]
for i in num:
    if(num.index(i) != num.index(num[-1])):
        if(i>num[(num.index(i)+1)] and i>num[(num.index(i)-1)]):
            print(f"'{i}' at index {num.index(i)}")