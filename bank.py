class Bank():
    
    def __init__(self,acc,name,bal):
        self.acc = acc
        self.bal = bal
        self.name = name
        
    
    def deposit(self,n):
        self.bal = self.bal + n
        print(f"{n} amount has been deposited!!")
        
    def withdraw(self,f):
        if((float(self.bal)-float(f))>1000):
            print(f"{f} amount can be withdrawn!")
            self.bal = float(self.bal) - float(f)
        else:
            print(f"{f} amount can't be withdrawn!")
            
            
if __name__ == "__main__":
    
    name = input("Enter account holder name: ")
    acc = input("Enter account number: ")
    bal = float(input("Enter amount to be deposited: "))
    
    cust1 = Bank(acc,name,bal)
    h = ""
    while(h.lower() == 'd' or h.lower() == 'w' or h == '' or h == 'b'):
        h = input("For deposit press 'd' and for withdrawal press 'w' and for balance check press 'b'......for no transaction press any key:  ")
        if(h.lower() == 'd'):
            k = float(input("Enter the deposit amount: "))
            cust1.deposit(k)
        elif(h.lower() == 'w'):
            y = float(input("Enter the withdrawal amount: "))
            cust1.withdraw(y)
        elif(h.lower() == 'b'):
            print(cust1.bal)