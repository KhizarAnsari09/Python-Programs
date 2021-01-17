'''Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).'''
import random
n = input("Give the list of numbers: ")
lst1 = n.split(',' or ' ')
lst1.sort()
j = input("Provide the number to be found: ")
x = random.randint(0,(len(lst1)-1))
print(x)
new_lst = []
for itm in lst1:
    new_lst.append(itm)
while(lst1[0] != new_lst[x-len(lst1)]):
    k = new_lst.pop(0)
    new_lst.append(k)
l = range(len(new_lst))
for itm,pos in zip(new_lst,l):
    if(itm == j):
        print(f"{j} is at index {pos}")
print(new_lst)