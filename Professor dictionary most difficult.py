#Most difficult program from May 15 from kumarweb28
class Prof():
    
    def __init__(self,ID,name,sub):
        self.ID = ID
        self.name = name
        self.sub = sub

class Uni():
    
    def __init__(self,lst1):
        self.lst1 = lst1
    
    def GTE(self,givenid):
        
        gg = 0
        for i in self.lst1:
            if(i.ID == givenid):
                ss = i.sub.values()
                for item1 in ss:
                    gg = gg + int(item1)
                print(f"{gg} total years teaching exp of {i.name}")

    def SPBS(self,str1):
        
        c = 0
        t = ''
        for i in self.lst1:
            for item in i.sub.keys():
                if (item.lower() == str1.lower()):
                    if(c<(i.sub.get(item))):
                        c = int(i.sub.get(item))
                        t = i.name
        
        print(f"'{t}' is the senior faculty in '{str1}' having '{c}' of experience")
        
        for y in self.lst1:
            if(y.name == t):
                print(y.sub)
                    
if __name__ == '__main__':
    
    w = int(input("Number of Profs: "))
    lst1 = []
    for itm in range(w):
        name = input("Name of Prof: ")
        idd = int(input("ID of Prof: "))
        num = int(input("Number of Subjects: "))
        sub = {}
        for i in range(1,num+1):
            f = input(f"Subject {i}: ")
            g = int(input("Years of exp: "))
            sub[f] = g
        hj = Prof(idd,name,sub)
        lst1.append(hj)
    o = Uni(lst1)
    l = int(input("Give ID of Prof: "))
    str1 = input("Enter subject: ")
    o.GTE(l)
    o.SPBS(str1)