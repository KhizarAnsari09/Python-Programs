'''

Create a class FoodItem with the below attributes:


item_id of type Number
item_name of type String
item_category of type String
item_price of type Number

​

Create the init method which takes all parameters in the above sequence. The method should set the value of attributes to parameter values.

​

Create a method inside the class with the name provideDiscount. This method takes a Number value as argument which is the percentage by which the item price should be discounted and discounts the item price of the food item by the given percentage amount. Returns the updated price of the given item.
e.g. If the food item price is 100 and the given percentage is 10, then the updated price of the food item should be 90.


Create another class Restaurant with the below attributes:
restaurant_name of type String
fooditem_list of type List having Foodltem objects


Create the init method which takes all parameters in the above sequence. The method should set the value of attributes to parameter values inside the method.


Create another method inside the class with the name retrieveUpdatedPrice. The method takes the update percentage as first argument and item id as the second argument . The method should find the respective food item, whose item id is given as in the argument , discount the price as per the given percentage and return the respective Foodltem object.

​

If the food item with given item id is not found , then the method returns None . Note: In Python None means NULL Object , Accordingly default maiN will display the message ‘No Food item exists which matches the search criteria’ (excluding the quotes)
If the update discount percent (argument to this function) is less than equals to zero , then return the object as it is , means there would not be any changes to the price.
Note: Use the method provideDiscount defined in the Foodltem class to calculate the discount price of the food items .

​

Instructions to write the main section of the code:
a. You would require to write the main section completely, hence please follow the below instructions for the same.
b. You would require to write the main program which is inline to the “sample input description section” mentioned below and to read the data in the same sequence.
c. Create the respective objects(Foodltem and Restaurant) with the given sequence of arguments to fulfill the Unit_ method requirement defined in the respective classes referring to the below instructions. i. Create a Foodltem object after reading the data related to it and add the object to the list of Foodltem objects which will be provided to the Restaurant class.This point repeats for the number of Foodltem objects(considered in the first line of input) . ii. Create Restaurant object by passing the Restaurant name(you can hard-code any name you want)and List of Foodltem objects ( created and as mentioned in above point# c.i ) as the arguments.
d. Take two number values as input depicting the item_id and the discount percentage to be provided as arguments to the method retrieveUpdatedPrice. e. Call the method retrieveUpdatedPrice mentioned above from the main section.
e. Display the Item Name and the Item Price separated by a ‘-‘ from the returned Foodltem object. Please refer to the sample output for more clarity on the display format.
f. If None is returned by the method retrieveUpdatedPrice ,then display the message No Food item exists which matches the search criterialexcluding the quotes).

​

• Input Format For Custom Testing
The 1st input taken in the main section is the number of Foodltem objects to be added to the list of FoodItems.
The next set of inputs are the item id, item name, item category and item price for each food item taken one after other and is repeated for number of objects given in the first line of input
The last but one line of input refers the item id , whose price needs to be discounted with the given percentage , mentioned in the last line

​

Sample Input


4
11
Pulao
Indian
80
12
Bhel
Snacks
50
13
Pasta
Italian
160
14
Burrito
Mexican
140
12
20


Sample Output


Bhel – 40.0

'''



class Food_item():
    
    def __init__(self,item_id,item_name,item_category,item_price):
        self.item_id = item_id
        self.item_name = item_name
        self.item_category = item_category
        self.item_price = item_price
        
    def Provide_Discount(self,discount):
        
        final_price = self.item_price - self.item_price * (discount/100)
        
class Restauraunt():
    
    def __init__(self,l1,Restauraunt_name = "Xpress Eats!"):
        self.l1 = l1
        
    def Retrieve_updated_price(self,discount,idd):
        
        for i in self.l1:
            
            final_price = 0
            if(idd == i.item_id):
                final_price = i.item_price * ((100-discount)/100)
                print(i.item_name.capitalize(),"-",final_price)
                
                
if __name__ == '__main__':
    
    n = int(input())
    l1 = []
    for i in range(n):
        item_id = int(input())
        item_name = input()
        item_category = input()
        item_price = float(input())
        obj = Food_item(item_id,item_name,item_category,item_price)
        l1.append(obj)
    idd = int(input())
    discount = float(input())
    print("\n")
    o = Restauraunt(l1)
    o.Retrieve_updated_price(discount,idd)