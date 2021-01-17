#Number hai 3 aur aise number display karneka jo position 7 par aa rahe lekin not divisible by 3.
#kuch toh number of sets bananeka jaise 1,2|4,5|7,8|10,11
#abhi isme 7 position par 10 hai jo 3 set cross karke fir ek number aage janeka hai
#set cross karneka logic yeh hai ki k/(n-1)
#bacha hua cross karneka hai toh remainder use karneka k%(n-1)
n = 9
k = 13
import math
if(k<n):
    print(k)
elif(k>n):
    t = math.floor(k/(n-1))
    r = n*t + (k%(n-1))
    print(r)