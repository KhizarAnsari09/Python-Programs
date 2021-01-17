class Employee():
    
    def __init__(self,ID,name,role,salary):
        self.ID = ID
        self.name = name
        self.role = role
        self.salary = salary
    


class Org():
    
    def __init__(self,lst1,JR,f):
        self.lst1 = lst1
        self.JR = JR
        self.f = f
        
    def calc_slry(self):
        lst2 = []
        h_lst = []
        h = 0.00
        for item in self.lst1:
            if ((item.role.lower()) == (self.JR.lower())):
                h = (item.salary*(self.f/100)) + item.salary
                lst2.append(item)
                h_lst.append(h)
        
        for i,h in zip(lst2,h_lst):
            print(f"{i.name}\n{h}")

            
            
if __name__ == "__main__":
    
    n = int(input("Number of Employees: "))
    lst1 = []
    for i in range(n):
        idd = input("Enter Employee ID: ")
        name = input("Enter Employee name: ")
        role = input("Enter Employee Role: ")
        salary = float(input("Enter Employee salary: "))
        
        emp = Employee(idd,name,role,salary)
        lst1.append(emp)
    
    r = input("Enter Employee role who should be incremented: ")
    incre = float(input("Enter percentage that salary should be incremented by: "))
    
    
    org1 = Org(lst1,r,incre)
    org1.calc_slry()