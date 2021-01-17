'''

Create a class called apartment with attributes flatnumber,owner name,electicity bill amount.

Create another class apartment_demo with def init(self): pass ​ to create a method getSecondMinBill that takes the list of objects and gives the second minimum electricity bill as output. 

​

​

input:

3(no of objects to be created) 

1000 

Hari 

5000 

1001 

Hena 

5002 

1002 

Harsha 

5001 

​

output:

5001 (since it is the second minimum bill amount among the bills)

'''
class Apartment():
    
    def __init__(self,flat_no,owner_name,electricity_bill):
        self.flat_no = flat_no
        self.owner_name = owner_name
        self.electricity_bill = electricity_bill
        

class Demo_apartment():
    
    def __init__(self,l1):
        self.l1 = l1
        
    def get_second_min_bill(self):
        
        min_list = []
        
        for i in self.l1:
            min_list.append(i.electricity_bill)
        
        myset = set(min_list)
        min_list = list(myset)
        f = min(min_list)
        min_list.remove(f)
        f = min(min_list)
        print(f)
        

if __name__ == '__main__':
    
    l1 = []
    n = int(input())
    for i in range(n):
        fn = int(input())
        nm = input()
        eb = int(input())
        obj = Apartment(fn,nm,eb)
        l1.append(obj)
    print("\n")
    o = Demo_apartment(l1)
    o.get_second_min_bill()