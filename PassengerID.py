class Pass():
    
    def __init__(self,ID,name,gend,dist):
        self.ID = ID
        self.name = name
        self.gend = gend
        self.dist = dist


if __name__ == "__main__":
    
    found = False
    lst1 = []
    n = int(input("Number of passengers : "))
    for i in range(1,n+1):
        Id = int(input("Give Passenger ID : "))
        name = input("Give Passenger Name : ")
        gend = input("Give Passenger Gender : ")
        dist = int(input("Give Passenger Distance : "))
        pss = Pass(Id,name,gend,dist)
        lst1.append(pss)
    f1 = int(input("Provide Passenger ID which is to be discounted : "))
    f2 = int(input("Provide Discount which is to be given : "))
    for item in lst1:
        if(item.ID == f1):
            print(f"Discount of {item.ID} is {f2}")
            found = True
    if not(found):
        print("ID doesn't Exist!!")